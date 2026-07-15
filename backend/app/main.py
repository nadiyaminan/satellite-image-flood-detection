import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.app.services.model_service import FloodDetector

app = FastAPI(title="Flood Detection API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_service = FloodDetector()


class PredictionResponse(BaseModel):
    label: str
    confidence: float
    model_type: str
    message: str


@app.get("/health")
def health_check():
    return {"status": "ok", "model_path": model_service.model_path}


@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    if not file.filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        raise HTTPException(status_code=400, detail="Only image files are supported")

    contents = await file.read()
    try:
        result = model_service.predict(contents)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return PredictionResponse(**result)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)
