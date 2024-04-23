from fastapi import FastAPI, Path, File, UploadFile
from typing import Optional
from pydantic import BaseModel
import sys
import os
from models.mirror_image import mirrormodel
from models.singleline import process_image_single
from models.multiline import process_image
from models.miss_spelled import miss_spelled_model
from models.risk_detection import risk_detection
from typing import List
from Notebooks.database.routes import database_router
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(database_router)

# add this code to allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define input data model
class InputData(BaseModel):
    data: List[List[int]]

@app.get("/get-posts")
def get_posts():
    return {"data": 11}


@app.post("/predict/mirror-images")
async def predict_image_mirror(file: UploadFile = File(...)):
    file_name = file.filename
    file_path = rf"E:\Study materials\IIT\4th year\FYP\Codes\sinhala_handwriting_error_detection-main\temp_images\{file_name}"
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
        response = mirrormodel(rf"{file_path}")
        f.close()
        os.remove(file_path)
        return response


@app.post("/predict/single-line")
async def predict_image_single(file: UploadFile = File(...)):
    file_name = file.filename
    file_path = rf"E:\Study materials\IIT\4th year\FYP\Codes\sinhala_handwriting_error_detection-main\temp_images\{file_name}"
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
        response = process_image_single(rf"{file_path}")
        f.close()
        os.remove(file_path)
        return response


@app.post("/predict/multi-line")
async def predict_image_multi(file: UploadFile = File(...)):
    file_name = file.filename
    file_path = rf"E:\Study materials\IIT\4th year\FYP\Codes\sinhala_handwriting_error_detection-main\temp_images\{file_name}"
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
        response = process_image(rf"{file_path}")
        f.close()
        os.remove(file_path)
        return response


@app.post("/predict/miss-spelled")
async def predict_image_mirror(file: UploadFile = File(...)):
    file_name = file.filename
    file_path = rf"E:\Study materials\IIT\4th year\FYP\Codes\sinhala_handwriting_error_detection-main\temp_images\{file_name}"
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
        response = miss_spelled_model(rf"{file_path}")
        f.close()
        os.remove(file_path)
        return response


@app.post("/predict/risk-detection")
async def predict_risk_detection(input_data: InputData):
    response = risk_detection(input_data.data)
    return JSONResponse(content={"output": response[0]})
