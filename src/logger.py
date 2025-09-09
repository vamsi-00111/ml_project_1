import os
import logging
from datetime import datetime


file_name=f'{datetime.now().strftime("%d_%m_%y_%H_%M_%S")}.log'
file_path=os.path.join(os.getcwd(),'logs',file_name)
os.makedirs(file_path,exist_ok=True)


log_file=os.path.join(file_path,file_name)


logging.basicConfig(
    filename=log_file,
    format="%(asctime)s - [%(levelname)s] - %(filename)s:%(lineno)d - %(message)s",
    level=logging.INFO
    
    
)