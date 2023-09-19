from src.mlproject.logger import logging 
from src.mlproject.exception import CustomException 
from src.mlproject.components.data_ingestion import DataIngestionConfig 
from src.mlproject.components.data_ingestion import DataIngestion  
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.data_transformation import DataTransformationConfig 
import sys

if __name__== '__main__':
    logging.info("The Execution has started.")

    try:
        data_ingestion=DataIngestion()
        train_data_path, test_data_path = data_ingestion.inititate_data_ingestion()

        data_transformation= DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path, test_data_path)

        
    except Exception as e:
        logging.info("Custome Exception")
        raise CustomException(e, sys)

        