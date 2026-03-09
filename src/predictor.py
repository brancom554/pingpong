import joblib
from config import MODEL_PATH, FEATURES

def load_model():
    return joblib.load(MODEL_PATH)

def predict_match(features_dict, odds_win=2.5):  # Exemple odds
    """
    Gestion des prédictions: Input dict comme {'rank_diff': 10, ...}
    """
    model = load_model()
    X = [[features_dict[f] for f in FEATURES]]  # Convert to 2D array
    proba = model.predict_proba(X)[0][1]  # Proba win player1
    value = model.calculate_value_bet(proba, odds_win)
    return {
        'proba_win': proba,
        'value_bet': value,
        'recommendation': 'Bet if value >0' if value > 0 else 'No value'
    }

# Exemple: predict_match({'rank_diff': 5, 'recent_form1': 0.8, 'recent_form2': 0.6, 'head_to_head': 2})