import os
import requests

# Get token from environment variable
HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/prithivMLmods/Deepfake-Detector-Model"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def predict_image(image_path):
    
    with open(image_path, "rb") as f:
        data = f.read()

    response = requests.post(API_URL, headers=headers, data=data)

    if response.status_code != 200:
        return "Error", 0.0

    result = response.json()

    if isinstance(result, list) and len(result) > 0:
        prediction = result[0]["label"]
        confidence = result[0]["score"]
    else:
        prediction = "Unknown"
        confidence = 0.0

    return prediction, confidence