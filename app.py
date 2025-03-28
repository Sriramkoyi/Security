import sys
import os

import certifi
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()
mongo_db_url = os.getenv("MONGODB_URL_KEY")
print(mongo_db_url)
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile,Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd
import traceback

from networksecurity.utils.main_utils.utils import load_object

from networksecurity.utils.ml_utils.model.estimator import NetworkModel


client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

from networksecurity.constant.trainingpipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constant.trainingpipeline import DATA_INGESTION_DATABASE_NAME

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="./templates")

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline=TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training is successful")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
import traceback

@app.post("/predict")
async def predict_route(request: Request, file: UploadFile = File(...)):
    try:
        print(f"Received file: {file.filename}")

        df = pd.read_csv(file.file)
        print(f"Dataframe shape: {df.shape}")
        print(f"Dataframe head: \n{df.head()}")

        preprocessor = load_object("final_models/preprocessor.pkl")
        print("Preprocessor loaded")

        final_model = load_object("final_models/model.pkl")
        print("Model loaded")

        network_model = NetworkModel(preprocessor=preprocessor, model=final_model)
        y_pred = network_model.predict(df)
        print(f"Predictions: {y_pred}")

        df['predicted_column'] = y_pred
        df.to_csv('prediction_output/output.csv')
        print("Prediction saved to output.csv")

        table_html = df.to_html(classes='table table-striped')
        return templates.TemplateResponse("table.html", {"request": request, "table": table_html})

    except Exception as e:
        print("Exception occurred:", str(e))
        traceback.print_exc()
        return {"error": str(e)}


    
if __name__=="__main__":
    app_run(app,host="0.0.0.0",port=8000)
