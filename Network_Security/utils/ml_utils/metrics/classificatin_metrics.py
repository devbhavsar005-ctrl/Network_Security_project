import sys 
import os 
import numpy as np 

from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging

from Network_Security.entity.artifacts_entity import ClassificationMetricArtifacts
from sklearn.metrics import f1_score,recall_score,precision_score

def Get_classification_score(y_true,y_predict)->ClassificationMetricArtifacts:
    try:
        model_f1_score=f1_score(y_true,y_predict)
        model_recall_score=recall_score(y_true,y_predict)
        model_precision_score=precision_score(y_true,y_predict)

        classification_metrics=ClassificationMetricArtifacts(
            f1_score=model_f1_score,
            recall_score=model_recall_score,
            precision_score=model_precision_score
        )
        return classification_metrics
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)