from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import shutil
import os

from agent import DeepfakeAgent
from metrics import calculate_metrics
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(
    title="DeepVisionAgent API",
    description="Agent-based Deepfake Detection System",
    version="1.0"
)

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create folders if not exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# Initialize Agent
agent = DeepfakeAgent()


# ---------------------------------------------------
# Root Endpoint
# ---------------------------------------------------
@app.get("/")
def home():
    return {
        "message": "DeepVisionAgent is running 🚀",
        "agent": "DeepVisionAgent v1.0"
    }


# ---------------------------------------------------
# Image Deepfake Detection
# ---------------------------------------------------
@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    try:
        file_path = f"uploads/{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = agent.analyze_image(file_path)

        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )


# ---------------------------------------------------
# Video Deepfake Detection
# ---------------------------------------------------
@app.post("/analyze-video")
async def analyze_video(file: UploadFile = File(...)):
    try:
        file_path = f"uploads/{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = agent.analyze_video(file_path)

        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )


# ---------------------------------------------------
# Grad-CAM Heatmap Endpoint
# ---------------------------------------------------

# ---------------------------------------------------
# Metrics Endpoint
# ---------------------------------------------------
#@app.get("/metrics")
#def metrics():
   # try:
    #    data = calculate_metrics()
 #       return data
#    except Exception as e:
#        return {"error": str(e)}


# ---------------------------------------------------
# Health Check Endpoint
# ---------------------------------------------------
@app.get("/health")
def health():
    return {"status": "online", "agent": "Active"}

import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)