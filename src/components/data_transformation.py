from src.exception import CustomException
from src.logger import logging
import pandas as pd
import os
import sys
from dataclasses import dataclass
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder

from src.utils import save_obj

@dataclass
class Dataprepocessorpath:
    data_preprocessor_file_path=os.path.join("artifacts","data_preprocessor.pkl")


class Datatransformation:
    
    def __init__(self):
        self.preprocessor_obj=Dataprepocessorpath()
        
    def data_transformer_obj(self):
        try:
            num_columns=["reading_score","writing_score"]
            cat_columns = [
                        "gender",
                        "race_ethnicity",
                        "parental_level_of_education",
                        "lunch",
                        "test_preparation_course"
                         ]

            
            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("standard_scale",StandardScaler())
                ]
            )
            # num_pipeline= Pipeline(
            #     steps=[
            #     ("imputer",SimpleImputer(strategy="median")),
            #     ("scaler",StandardScaler())

            #     ]
            # )

            # cat_pipeline=Pipeline(
            #     steps=[
            #         ("imputer",SimpleImputer(strategy="most_frequent"))
            #         ("onehot_encoder",OneHotEncoder())
            #     ]
            # )
            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )
            tranfomation=ColumnTransformer(
                [
                    ("cat_pipeline",cat_pipeline,cat_columns),
                    ("num_pipeline",num_pipeline,num_columns)
                    
                    ]
            )
            logging.info("transforming categorical features and numerical feature are done")
            return tranfomation
        
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
        
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            target_column="math_score"
            
            x_train=train_df.drop(columns=[target_column],axis=1)
            y_train=train_df[target_column]
            
            x_test=test_df.drop(columns=[target_column],axis=1)
            y_test=test_df[target_column]
            
            logging.info("splitting data is done")
            
            preprocessor=self.data_transformer_obj()
            
            x_train_arr=preprocessor.fit_transform(x_train)
            x_test_arr=preprocessor.transform(x_test)
            
            test_arr=np.c_[
                x_test_arr,np.array(y_test)
            ]
            
            train_arr=np.c_[
                x_train_arr,np.array(y_train)
            ]
            save_obj(
                file_path=self.preprocessor_obj.data_preprocessor_file_path,
                file=preprocessor
                     )
            logging.info("saving pickle file is done")
            return(
                train_arr,test_arr,self.preprocessor_obj.data_preprocessor_file_path
            )
        
        except Exception as e:
           raise CustomException(e,sys)
            
            
            
            
            
        
        
    
    
    
        
        
    
    

    