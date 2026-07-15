from pathlib import Path

from backend.app.services.model_service import FloodDetector


def test_resolves_uploaded_model_path():
    detector = FloodDetector(model_path="")
    resolved = detector._resolve_model_path()

    assert resolved is not None
    assert Path(resolved).exists()
    assert Path(resolved).name == "vgg16_damage_detection.h5"
