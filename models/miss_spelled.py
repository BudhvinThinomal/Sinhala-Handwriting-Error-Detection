import os
from ultralytics import YOLO
import cv2
import pandas as pd
import numpy as np 

def miss_spelled_model(image_path):
    model = YOLO(r"E:\Study materials\IIT\4th year\FYP\Codes\sinhala_handwriting_error_detection-main\weigths\miss_spelled.pt")
    model_result = model.predict(image_path)
    for i in model_result:
        probabilities = (i.boxes.conf).cpu()
        classification = (i.boxes.cls).cpu()
        classification = ["normal" if i==1 else "miss spelled" for i in classification]
        df = pd.DataFrame({'probability': probabilities, 'class': classification})
        json_response = df.to_dict(orient="records")
        return(json_response)