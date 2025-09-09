import sys
from src.logger import logging


def manual_exception_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    error_message = f"Error occurred in script: [{exc_tb.tb_frame.f_code.co_filename}] at line number: [{exc_tb.tb_lineno}] error message: [{str(error)}]"
    return error_message




class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(manual_exception_details(error_message, error_details))
        self.error_message = manual_exception_details(error_message, error_details)

    def __str__(self):
        return self.error_message
if __name__=="__main__":
    try:
        logging.info("division by zero")
        a=8/0
    except Exception as e:
        raise CustomException(e,sys)
