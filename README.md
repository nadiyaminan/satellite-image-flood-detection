# Satellite Image Flood Detection using VGG19

## Overview

This project is a deep learning–based flood detection platform that analyzes satellite images to classify flooded and non-flooded regions. It combines a VGG19 convolutional neural network with a FastAPI backend and a React frontend, providing a complete web application for image-based flood prediction.

> **Project Note:** This repository contains a portfolio copy of a final-year team project and is maintained to showcase my contribution to the implementation and deployment.

---

## Features

- Flood detection using satellite imagery
- Deep learning with VGG19
- FastAPI backend for inference
- React frontend for image upload and prediction
- Automatic model loading
- Prediction confidence display
- Deployment-ready architecture
- Docker support
- Cloud deployment support

---

## Technologies Used

- Python
- TensorFlow / Keras
- VGG19
- FastAPI
- React
- JavaScript
- HTML
- CSS
- OpenCV
- NumPy
- Docker

---

## Project Structure

```
backend/
frontend/
models/
data/
requirements.txt
render.yaml
```

---

## Installation

### Backend

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux

pip install -r requirements.txt

uvicorn backend.app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Model Integration

Place your trained model inside the `models` directory using either of these names:

- flood_detection_model.keras
- flood_detection_model.h5

The backend automatically loads the trained model. If no model is found, it falls back to a lightweight heuristic for demonstration purposes.

---

## Deployment

Backend

- Render
- Railway
- Fly.io
- Azure App Service

Frontend

- Vercel
- Netlify

Containerization

- Docker
- Docker Compose

---

## Screenshots

Add screenshots of:

- Home Page
- Image Upload
- Prediction Result
- Model Output

---

## Future Enhancements

- Real-time satellite image analysis
- Multi-class flood severity prediction
- GIS integration
- Improved model accuracy
- Mobile application support

---

## My Contribution

- Deep learning implementation
- Model integration
- Testing and evaluation
- Web application development
- Project deployment and documentation

---

## Author

**Nadiya Minan**

B.Tech Artificial Intelligence & Data Science

---

## License

This project is intended for educational and research purposes.
