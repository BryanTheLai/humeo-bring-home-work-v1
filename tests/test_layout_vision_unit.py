"""layout_vision parsing (no API calls)."""

import math

from humeo.layout_vision import _face_center_x, _instruction_from_gemini_json
from humeo_core.schemas import BoundingBox, LayoutKind


def test_instruction_from_gemini_json_split_with_bboxes():
    data = {
        "layout": "split_chart_person",
        "person_bbox": {"x1": 0.62, "y1": 0.05, "x2": 0.99, "y2": 0.95},
        "chart_bbox": {"x1": 0.02, "y1": 0.05, "x2": 0.58, "y2": 0.92},
        "reason": "webinar",
    }
    instr = _instruction_from_gemini_json("005", data)
    assert instr.layout == LayoutKind.SPLIT_CHART_PERSON
    assert instr.split_chart_region is not None
    assert instr.split_person_region is not None


def test_instruction_from_gemini_json_sit_center():
    data = {
        "layout": "sit_center",
        "person_bbox": {"x1": 0.3, "y1": 0.1, "x2": 0.7, "y2": 0.9},
        "chart_bbox": None,
        "reason": "talking head",
    }
    instr = _instruction_from_gemini_json("001", data)
    assert instr.layout == LayoutKind.SIT_CENTER
    assert instr.split_chart_region is None


def test_face_bbox_pulls_person_x_norm_toward_the_face():
    """Regression for the off-center subject bug.

    Reproduces clip 001 from the Dr. Mike failing run: subject sitting in
    profile, head around x≈0.23, tank top + arm extend the body bbox out
    to x2=0.75. The wide person_bbox center alone gave person_x_norm=0.415,
    which cropped the final 9:16 short on the torso and pushed the face off
    the left edge. With the face_bbox hint, person_x_norm must track the
    face instead.
    """
    data = {
        "layout": "sit_center",
        "person_bbox": {"x1": 0.08, "y1": 0.10, "x2": 0.75, "y2": 0.95},
        "face_bbox":   {"x1": 0.18, "y1": 0.12, "x2": 0.30, "y2": 0.32},
        "chart_bbox": None,
        "reason": "profile speaker off-center left",
    }
    instr = _instruction_from_gemini_json("001", data)
    assert instr.layout == LayoutKind.SIT_CENTER
    # Face center is 0.24. person-bbox center is 0.415. Must follow the face.
    assert math.isclose(instr.person_x_norm, 0.24, abs_tol=1e-6), (
        f"person_x_norm should track face center (0.24), got {instr.person_x_norm}"
    )


def test_face_bbox_missing_falls_back_to_person_bbox_center():
    data = {
        "layout": "sit_center",
        "person_bbox": {"x1": 0.30, "y1": 0.10, "x2": 0.70, "y2": 0.90},
        "face_bbox": None,
        "chart_bbox": None,
        "reason": "centered talking head",
    }
    instr = _instruction_from_gemini_json("002", data)
    assert math.isclose(instr.person_x_norm, 0.50, abs_tol=1e-6)


def test_face_bbox_rejected_when_as_wide_as_person_bbox():
    """If Gemini echoes the person bbox into face_bbox we get no new info.

    In that case fall back to the person-bbox center, not a spurious face
    center — we don't want the "fix" to regress the centered case.
    """
    data = {
        "layout": "sit_center",
        "person_bbox": {"x1": 0.10, "y1": 0.10, "x2": 0.90, "y2": 0.95},
        "face_bbox":   {"x1": 0.10, "y1": 0.10, "x2": 0.90, "y2": 0.95},
        "chart_bbox": None,
        "reason": "echoed bbox",
    }
    instr = _instruction_from_gemini_json("003", data)
    # Fall back to person-bbox center (0.5) — face_bbox too wide to trust.
    assert math.isclose(instr.person_x_norm, 0.50, abs_tol=1e-6)


def test_face_bbox_outside_person_bbox_is_ignored():
    """If face_bbox center sits outside person_bbox the model got confused."""
    data = {
        "layout": "sit_center",
        "person_bbox": {"x1": 0.60, "y1": 0.10, "x2": 0.95, "y2": 0.95},
        "face_bbox":   {"x1": 0.05, "y1": 0.10, "x2": 0.15, "y2": 0.25},
        "chart_bbox": None,
        "reason": "mismatched face and person",
    }
    instr = _instruction_from_gemini_json("004", data)
    # Person bbox center = 0.775; we must not jump to face center (0.10).
    assert math.isclose(instr.person_x_norm, 0.775, abs_tol=1e-6)


def test_face_center_helper_unit():
    # Clean case: tight face inside the body.
    face = BoundingBox(x1=0.20, y1=0.10, x2=0.30, y2=0.25)
    body = BoundingBox(x1=0.10, y1=0.10, x2=0.70, y2=0.95)
    assert _face_center_x(face, body) == 0.25

    # No face.
    assert _face_center_x(None, body) is None

    # Face suspiciously wide (> 40% of frame): ignore.
    wide = BoundingBox(x1=0.10, y1=0.10, x2=0.60, y2=0.95)
    assert _face_center_x(wide, body) is None
