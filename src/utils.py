
import os
import pandas as pd
import numpy as np
from src.exception import CustomException
import pickle
import sys
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_obj(file_path,file):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            pickle.dump(file,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
    
def evalute_models(x_train,x_test,y_train,y_test,models,param):
    try:
        report={}
        for i in range(len(models)):
            model=list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(x_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(x_train,y_train)
            # model.fit(x_train,y_train)
            
            y_test_pred=model.predict(x_test)
            
            y_test_score=r2_score(y_test,y_test_pred)
            report[list(models)[i]]=y_test_score
        return report
    except Exception as e:
        raise CustomException(e,sys)
    
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
        
        
        
    
    