# Satellite Image Flood Detection

## Overview

Satellite Image Flood Detection is a deep learning–based web application that analyzes satellite imagery to classify flooded and non-flooded regions. The platform combines a convolutional neural network (CNN), a FastAPI backend, and a React frontend to provide an intuitive interface for image upload and real-time flood prediction.

This project demonstrates the practical application of artificial intelligence, computer vision, and web technologies for disaster monitoring and environmental analysis.

> **Project Note:** This repository is maintained as a portfolio copy of a final-year team project. The original team repository is linked below. This repository showcases my contribution to the project's implementation, deployment, and documentation.

---

## Live Demo & Repository

🌐 **Live Application**  
https://satellite-image-flood-detection-using-zqza.onrender.com/

📂 **Original Team Repository**  
https://github.com/farizest/Satellite-Image-Flood-Detection-using-VGGNET-19

📂 **My Portfolio Repository**  
https://github.com/nadiyaminan/satellite-image-flood-detection

---

## Features

- Satellite image flood detection
- AI-powered image classification
- Deep learning–based prediction
- FastAPI backend
- React frontend
- Image upload interface
- Automatic model loading
- Real-time prediction results
- Prediction confidence display
- Docker support
- Deployment-ready architecture
- Cloud hosting support

---

## Technologies Used

- Python
- TensorFlow / Keras
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

```text
backend/
frontend/
models/
data/
requirements.txt
render.yaml
README.md
```

---

## Installation

### Backend

```bash
python -m venv .venv

source .venv/bin/activate      # macOS/Linux
# OR
.venv\Scripts\activate         # Windows

pip install -r requirements.txt

uvicorn backend.app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Open the local Vite development URL displayed in the terminal.

---

## Model Integration

Place the trained model inside the **models** directory using one of the following names:

```
models/flood_detection_model.keras
```

or

```
models/flood_detection_model.h5
```

The backend automatically loads the trained model. If no trained model is available, it falls back to a lightweight heuristic so the application remains functional.

---

## Deployment

### Backend

- Render
- Railway
- Fly.io
- Azure App Service

### Frontend

- Vercel
- Netlify

### Containerization

- Docker
- Docker Compose

---

## Screenshots

Add screenshots of:

- Home Page
- Image Upload Interface
- Flood Prediction Result
- Model Output

---

## Future Enhancements

- Real-time satellite image analysis
- Multi-class flood severity prediction
- GIS integration
- Improved model accuracy
- Mobile application support
- Performance optimization
- Cloud-based monitoring dashboard

---

## My Contribution

As part of the final-year team project, my contributions included:

- Deep learning model implementation
- Image preprocessing and testing
- Model integration
- Web application development
- Deployment support
- Documentation and project presentation

---

## Skills Demonstrated

- Artificial Intelligence
- Deep Learning
- Computer Vision
- Image Classification
- TensorFlow
- FastAPI
- React
- Python
- Web Development
- REST APIs
- Git
- GitHub

---

## Author

**Nadiya Minan**

B.Tech in Artificial Intelligence & Data Science

GitHub: https://github.com/nadiyaminan

LinkedIn: *(Add your LinkedIn profile URL here)*

---

## License

This project is intended for educational and research purposes.
