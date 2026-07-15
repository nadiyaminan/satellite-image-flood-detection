# Flood Detection Platform

This project turns the flood detection notebook into a production-style application with:

- a FastAPI backend for image inference
- a modern React frontend for uploading images and viewing predictions
- deployment-ready files for local, Docker, and cloud hosting

## Project structure

- backend/app: FastAPI service and model loading logic
- frontend/src: React UI
- models/: place your trained model file here
- data/: the dataset used during experimentation

## Quick start

### 1. Backend

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.app.main:app --reload --port 8000
```

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

Then open the local Vite URL shown in the terminal.

## Model integration

Place your trained model file in the models folder and name it one of:

- models/flood_detection_model.keras
- models/flood_detection_model.h5

The backend automatically uses it when available. If no trained model is present, it falls back to a lightweight heuristic so the app still runs.

## Deployment ideas

- Backend: Render, Railway, Fly.io, Azure App Service
- Frontend: Vercel or Netlify
- Full stack: Docker Compose
