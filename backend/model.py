import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Pretrained deepfake model
model_name = "prithivMLmods/Deep-Fake-Detector-Model"

processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)

model.to(device)
model.eval()


def predict_image(image_path):
    image = Image.open(image_path).convert("RGB")

    inputs = processor(images=image, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1)

    confidence, predicted = torch.max(probs, 1)

    label = model.config.id2label[predicted.item()]

    return label, float(confidence.item())