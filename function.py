import os
import joblib
from django.conf import settings

BASE_DIR = settings.BASE_DIR
MODEL_PATH = os.path.join(BASE_DIR, 'Model')
ENCODER_PATH = os.path.join(BASE_DIR, 'Encoder')
SCALER_PATH =os.path.join(BASE_DIR, 'Scaler')

def load_prediction(model_name):
    try:
        PREDICTION_PATH = os.path.join(MODEL_PATH, model_name)
        model = joblib.load(PREDICTION_PATH)
        return model
    except Exception as e:
        print(f'Prediction Model Load Error: {e}')
        return None

def load_encoder(encoder_name):
    try:
        ENCODER_PATH_WITH_FILE = os.path.join(ENCODER_PATH, encoder_name)
        encoder = joblib.load(ENCODER_PATH_WITH_FILE)
        return encoder
    except Exception as e:
        print(f'Prediction Model Load Error: {e}')
        return None

def load_scaler(scaler_name):
    try:
        SCALER_PATH_WITH_FILE = os.path.join(SCALER_PATH, scaler_name)
        scaler = joblib.load(SCALER_PATH_WITH_FILE)
        return scaler
    except Exception as e:
        print(f'Prediction Model Load Error: {e}')
        return None