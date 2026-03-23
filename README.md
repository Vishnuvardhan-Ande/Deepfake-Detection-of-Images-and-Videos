
# 🧠 Deepfake Detection (Images & Videos)

## 📌 Overview

This project detects **deepfake images and videos** using deep learning models and provides a clean, interactive UI.

* ⚡ Backend powered by **FastAPI**
* 🌐 Frontend built with **React**
* 🧠 Uses CNN-based models for prediction

Users can upload media and instantly receive:

* ✅ Real / Fake classification
* 📊 Confidence score

---

## 🚀 Features

* 🔍 Deepfake detection for images
* 🎥 Deepfake detection for videos
* ⚡ High-performance FastAPI backend
* 🌐 Interactive React UI
* 🧠 CNN-based deep learning model
* 📊 Confidence score output
* 🔗 REST API integration

---

## 🛠️ Tech Stack

### 🔹 Frontend

* React.js
* HTML, CSS, JavaScript

### 🔹 Backend

* FastAPI
* Uvicorn

### 🔹 Machine Learning

* Python
* TensorFlow / PyTorch
* OpenCV
* NumPy, Pandas, Scikit-learn

---

## 📂 Project Structure

```bash
Deepfake-Detection/
│
├── frontend/                  # React App
│   └── deepfake-ui/
│       └── src/
│
├── backend/                   # FastAPI Server
│   ├── app.py
│   ├── model.py
│   ├── train.py
│   ├── video.py
│   ├── utils.py
│   ├── metrics.py
│   ├── agent.py
│   ├── requirements.txt
│   └── render.yml
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Vishnuvardhan-Ande/Deepfake-Detection-of-Images-and-Videos.git
cd Deepfake-Detection-of-Images-and-Videos
```

---

### 2️⃣ Backend Setup (FastAPI)

```bash
cd backend

# Create virtual environment
python -m venv venv
```

**Activate Environment**

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**Install Dependencies**

```bash
pip install -r requirements.txt
```

**Run Server**

```bash
uvicorn app:app --reload
```

📍 Backend: [http://127.0.0.1:8000](http://127.0.0.1:8000)
📍 API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 3️⃣ Frontend Setup (React)

```bash
cd frontend/deepfake-ui

npm install
npm start
```

📍 Frontend: [http://localhost:3000](http://localhost:3000)

---

## ▶️ Usage

1. Start the FastAPI backend
2. Start the React frontend
3. Upload an image or video
4. Model processes the file
5. Get result: **Real / Fake + Confidence Score**

---

## 🔗 API Endpoints

### 📤 Predict Image

```
POST /predict/image
```

### 📤 Predict Video

```
POST /predict/video
```

### 📥 Response Example

```json
{
  "prediction": "Fake",
  "confidence": 0.92
}
```

---

