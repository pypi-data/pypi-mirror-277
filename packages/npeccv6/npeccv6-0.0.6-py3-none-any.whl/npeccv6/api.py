import os
import shutil
from typing import List, Optional

from fastapi import FastAPI, File, HTTPException, UploadFile
from pydantic import BaseModel

try:
    from .model_func import load_pretrained_model
    from .predict import predict
    from .train import main as train
    from .utils import setup_logger
except:
    from model_func import load_pretrained_model
    from predict import predict
    from train import main as train
    from utils import setup_logger

UPLOAD_DIRECTORY = "to_predict"

app = FastAPI()
logger = setup_logger()

# Move your existing prediction code here
# Ensure that `load_pretrained_model`, `predict`, and all other required functions are imported


class PredictionResult(BaseModel):
    predicted_mask: List[List[int]]
    mean_conf_score: float


@app.post("/predict", response_model=List[PredictionResult])
async def predict_image(
    user_folder: str = "anonymous",
    files: List[UploadFile] = File(...),
    model_name: str = "test",
) -> List[PredictionResult]:
    results = []
    try:
        
        print(files)
        for file in files:
            # Make sure folders exist
            os.makedirs(os.path.dirname(UPLOAD_DIRECTORY), exist_ok=True)
            os.makedirs(os.path.dirname(user_folder + "/images/"), exist_ok=True)
            os.makedirs(os.path.dirname(user_folder + "/masks/"), exist_ok=True)
            print('-----')
            print("Uploda directory" + UPLOAD_DIRECTORY)
            # Save the uploaded file locally
            image_file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)

            with open(image_file_path, "wb") as f:
                f.write(await file.read())

            # Get filename without extension
            base = os.path.basename(file_path)
            base_file_name = os.path.splitext(base)[0]

            # Load the pretrained model
            model = load_pretrained_model(model_name)

            # Predict using your existing function and save mask in history
            predicted_mask, mean_conf_score = predict(
                model,
                file_path,
                save_path=user_folder + "/masks/" + base_file_name + "_root_mask.tif",
            )

            # Move base image to history
            shutil.move(
                image_file_path, user_folder + "/images/" + base_file_name + ".png"
            )

            # Append the prediction result
            results.append(
                PredictionResult(
                    predicted_mask=predicted_mask, mean_conf_score=mean_conf_score
                )
            )

        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")

print('dupa')