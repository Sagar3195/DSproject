from src.mlproject.logger import logging 
from src.mlproject.exception import CustomException 
from src.mlproject.components.data_ingestion import DataIngestionConfig 
from src.mlproject.components.data_ingestion import DataIngestion  
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.data_transformation import DataTransformationConfig 
from src.mlproject.components.model_tranier import ModelTrainer, ModelTrainingConfig 
import sys


if __name__== '__main__':
    logging.info("The Execution has started.")

    try:
        #Data Ingestion
        data_ingestion=DataIngestion()
        train_data_path, test_data_path = data_ingestion.inititate_data_ingestion()

        #Data Transformation
        data_transformation= DataTransformation()
        train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

        ##Model Trainer
        model_trainer= ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))

        
    except Exception as e:
        logging.info("Custome Exception")
        raise CustomException(e, sys)

        