import joblib
import pandas as pd
from .preprocessor import preprocess_data
from .model import PingPongModel
#from .data_loader import fetch_data
from .data_loader import fetch_all_data  # Changé de fetch_data à fetch_all_data
from .config import PROCESSED_PATH, MODEL_PATH

def train_model(retrain=False, from_date=None, to_date=None):
    """
    Entraînement automatique: Fetch nouvelles data multi-sources si retrain, preprocess, train.
    """
    if retrain:
        df_raw = fetch_all_data(from_date=from_date, to_date=to_date)  # Utilise fetch_all_data avec filtres optionnels
    else:
        df_raw = pd.read_csv(PROCESSED_PATH)  # Ou load existant
    
    df = preprocess_data(df_raw)
    X = df.drop('outcome', axis=1)
    y = df['outcome']
    
    model = PingPongModel()
    model.train(X, y)
    joblib.dump(model, MODEL_PATH)
    print(f"Modèle entraîné et sauvé. Log-loss: {model.evaluate(X, y)}")
    
    return model

