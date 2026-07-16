import io
import os
from pathlib import Path
from typing import Dict, Any

import numpy as np
from PIL import Image


class FloodDetector:
    def __init__(self, model_path: str | None = None):
        self.model_path = self._resolve_model_path(model_path)
        self.model = None
        self.model_type = "heuristic"
        self._load_model()

    def _resolve_model_path(self, model_path: str | None = None) -> str | None:
        explicit_path = model_path or os.getenv("MODEL_PATH")
        if explicit_path:
            path = Path(explicit_path)
            if path.exists():
                return str(path)

        repo_root = Path(__file__).resolve().parents[2]
        candidates = [
            repo_root / "models" / "vgg16_damage_detection.h5",
            repo_root / "models" / "flood_detection_model.keras",
            repo_root / "models" / "flood_detection_model.h5",
            Path("models/vgg16_damage_detection.h5"),
            Path("models/flood_detection_model.keras"),
            Path("models/flood_detection_model.h5"),
        ]
        for candidate in candidates:
            if candidate.exists():
                return str(candidate)

        return None

    def _load_model(self) -> None:
        if not self.model_path:
            print("Model path is not configured or resolved.")
            return

        path = Path(self.model_path)
        if not path.exists():
            print(f"Model file does not exist at: {path}")
            return

        try:
            import tensorflow as tf
            print(f"Attempting to load full Keras model from: {path} using TensorFlow {tf.__version__}")
            self.model = tf.keras.models.load_model(str(path))
            self.model_type = "tensorflow"
            print("Model loaded successfully using load_model!")
            return
        except Exception as exc:
            print(f"Standard load_model failed: {exc}. Trying load_weights fallback...")

        # Fallback: Construct architecture and load weights
        try:
            import tensorflow as tf
            print("Reconstructing VGG16 sequential architecture...")
            
            # Recreate base VGG16 model without downloading weights since h5 contains them
            base_model = tf.keras.applications.vgg16.VGG16(
                input_shape=(128, 128, 3),
                include_top=False,
                weights=None
            )
            base_model.trainable = False
            
            # Reconstruct the sequence matching the notebook
            self.model = tf.keras.Sequential([
                base_model,
                tf.keras.layers.GlobalAveragePooling2D(),
                tf.keras.layers.Dense(1)
            ])
            
            # Compile model (using same parameters as notebook)
            self.model.compile(
                optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
                loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                metrics=['accuracy']
            )
            
            # Load weights
            print(f"Loading weights from H5 file: {path}")
            self.model.load_weights(str(path))
            self.model_type = "tensorflow"
            print("Model loaded successfully using weights fallback!")
        except Exception as fallback_exc:
            import traceback
            print(f"Failed to load model using weights fallback: {fallback_exc}")
            traceback.print_exc()
            self.model = None
            self.model_type = "heuristic"

    def _preprocess_image(self, image_bytes: bytes) -> np.ndarray:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image = image.resize((128, 128))
        array = np.array(image, dtype=np.float32) / 255.0
        return array

    def _heuristic_prediction(self, array: np.ndarray) -> Dict[str, Any]:
        # Lightweight rule-based fallback that works without a trained model.
        brightness = float(array.mean())
        blue_channel = float(array[:, :, 2].mean())
        water_score = 0.55 + (0.25 * (1 - brightness)) + (0.20 * (1 - blue_channel))
        water_score = float(np.clip(water_score, 0.0, 1.0))

        if water_score > 0.6:
            label = "flood"
            confidence = round(float(water_score), 3)
        else:
            label = "no_flood"
            confidence = round(float(1 - water_score), 3)

        return {
            "label": label,
            "confidence": confidence,
            "model_type": self.model_type,
            "message": "Fallback mode is active because no trained model file is available yet. Add your .keras or .h5 model to the models folder to enable full inference.",
        }

    def predict(self, image_bytes: bytes) -> Dict[str, Any]:
        array = self._preprocess_image(image_bytes)

        if self.model is not None:
            import tensorflow as tf

            expanded = np.expand_dims(array, axis=0)
            prediction = self.model.predict(expanded, verbose=0)[0][0]
            probability = float(1.0 / (1.0 + np.exp(-prediction)))
            if probability >= 0.5:
                label = "flood"
                confidence = round(float(probability), 3)
            else:
                label = "no_flood"
                confidence = round(float(1.0 - probability), 3)
            return {
                "label": label,
                "confidence": confidence,
                "model_type": self.model_type,
                "message": "Prediction generated by your trained TensorFlow model.",
            }

        return self._heuristic_prediction(array)
