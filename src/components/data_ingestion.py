import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import os
import sys

from src.components.data_transformation import Datatransformation
from src.components.data_transformation import Dataprepocessorpath
from src.components.model_train import ModelTrainer


@dataclass
class IngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")

class DataIngestion:
    def __init__(self):
        self.config = IngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Starting the data ingestion process...")
        try:
        
            df = pd.read_csv("notebook/data/stud.csv")

        
            os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)


            df.to_csv(self.config.raw_data_path, index=False, header=True)

            logging.info("Splitting the data into train and test sets...")
            train_data, test_data = train_test_split(df, test_size=0.3, random_state=42)

    
            train_data.to_csv(self.config.train_data_path, index=False, header=True)
            test_data.to_csv(self.config.test_data_path, index=False, header=True)

            logging.info("Data ingestion completed successfully.")

            return (
                self.config.train_data_path,
                self.config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    
    data_transfomation=Datatransformation()
    train_arr,test_arr,_= data_transfomation.initiate_data_transformation(train_path=train_data,test_path=test_data)
    modeltrain=ModelTrainer()
    print( modeltrain.initiate_model_trainer(train_arr,test_arr))
