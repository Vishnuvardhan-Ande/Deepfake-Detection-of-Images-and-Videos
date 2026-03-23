📌 Overview

This project detects deepfake images and videos using deep learning models and provides a user-friendly React interface.

The backend is powered by FastAPI, enabling fast and efficient communication between the frontend and the machine learning model.

Users can upload media files and instantly get predictions indicating whether the content is Real or Fake, along with confidence scores.

🚀 Features
🔍 Deepfake detection for images
🎥 Deepfake detection for videos
⚡ High-performance FastAPI backend
🌐 Interactive React frontend UI
🧠 CNN-based deep learning model
📊 Confidence score output
🔗 REST API integration
🛠️ Tech Stack
🔹 Frontend
React.js
HTML, CSS, JavaScript
🔹 Backend
FastAPI
Uvicorn
🔹 Machine Learning
Python
TensorFlow / PyTorch
OpenCV
NumPy, Pandas, Scikit-learn
📂 Project Structure
Deepfake-Detection/
│
├── frontend/              # React application
│   ├── deepfake-ui/
│       └── src/
│
├── backend/               # FastAPI server
│   ├── app.py
│   ├── metrics.py
|   ├── requirements.txt  
│   ├── model.py
|   ├── render.yml
│   ├── train.py
│   ├── utils.py
│   ├── video.py
│   └── agent.py
│                  
└── README.md              
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/Vishnuvardhan-Ande/Deepfake-Detection-of-Images-and-Videos.git
cd deepfake-detection
2️⃣ Setup Backend (FastAPI)
cd backend

# Create virtual environment
python -m venv venv

# Activate
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r ../requirements.txt

# Run server
uvicorn main:app --reload

📍 Backend runs on: http://127.0.0.1:8000
📍 API Docs (Swagger): http://127.0.0.1:8000/docs

3️⃣ Setup Frontend (React)
cd frontend
npm install
npm start

📍 Frontend runs on: http://localhost:3000

▶️ Usage
Start FastAPI backend
Start React frontend
Upload an image or video
Backend processes file using ML model
Get result: Real / Fake + Confidence Score
🔗 API Endpoints
📤 Upload Image
POST /predict/image
📤 Upload Video
POST /predict/video
📥 Response Example
{
  "prediction": "Fake",
  "confidence": 0.92
}
