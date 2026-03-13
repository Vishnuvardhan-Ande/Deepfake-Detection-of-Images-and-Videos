import torch
from model import predict_image
from video import predict_video

#from metrics import calculate_metrics

class DeepfakeAgent:

    def __init__(self):
        self.name = "DeepVisionAgent v1.0"

    def analyze_image(self, image):
        prediction, confidence = predict_image(image)


        #calculate_metrics(prediction)

        return {
            "agent": self.name,
            "type": "image",
            "prediction": prediction,
            "confidence": confidence,
            "explanation": "Grad-CAM heatmap generated",
            "risk_level": self.risk_score(confidence)
        }

    def analyze_video(self, video):
        prediction, confidence = predict_video(video)

        #calculate_metrics(prediction)

        return {
            "agent": self.name,
            "type": "video",
            "prediction": prediction,
            "confidence": confidence,
            "risk_level": self.risk_score(confidence)
        }

    def risk_score(self, confidence):
        if confidence > 0.8:
            return "High Risk"
        elif confidence > 0.5:
            return "Medium Risk"
        else:
            return "Low Risk"