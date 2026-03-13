import cv2
import os
from model import predict_image

def predict_video(video_path, frame_skip=10):
    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    fake_count = 0
    total_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_skip == 0:
            temp_path = "temp_frame.jpg"
            cv2.imwrite(temp_path, frame)

            label, conf = predict_image(temp_path)
            total_frames += 1

            if label == "FAKE":
                fake_count += 1

            os.remove(temp_path)

        frame_count += 1

    cap.release()

    fake_ratio = fake_count / max(total_frames, 1)
    final_label = "FAKE" if fake_ratio > 0.5 else "REAL"

    return final_label, fake_ratio