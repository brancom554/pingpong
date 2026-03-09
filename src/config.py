# Configurations globales
API_URL = "https://api.tennis-data.com/v1/matches"  # Exemple, remplacez par l'API réelle
API_KEY = "votre_api_key_ici"  # Stockez en env var pour sécurité


API_URL_MATCHES = "https://api.sportradar.com/tennis-table/matches"
API_KEY_MATCHES = "votre_cle_sportradar"
API_URL_RANKINGS = "https://api.ittf.com/rankings"
API_KEY_RANKINGS = "votre_cle_ittf"
API_URL_ODDS = "https://api.oddsapi.com/odds"
API_KEY_ODDS = "votre_cle_oddsapi"


DATA_PATH = "../data/raw/matches.csv"
PROCESSED_PATH = "../data/processed/processed_matches.csv"
MODEL_PATH = "../models/pingpong_model.joblib"

HYPERPARAMS = {
    'n_estimators': 100,  # Pour RandomForest, par exemple
    'max_depth': 10
}

# Features pour le modèle
FEATURES = ['rank_diff', 'recent_form1', 'recent_form2', 'head_to_head']
TARGET = 'outcome'  # 1 si player1 gagne, 0 sinon


