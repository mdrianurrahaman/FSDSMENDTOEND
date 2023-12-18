import os 
import sys 
import pandas as pd 
from src.DimondPricePrediction.exception import customexception
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.utils.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self):
        try:
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")
        

            


        except Exception as e:
             raise customexception(e,sys)