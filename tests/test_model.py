# tests/test_model.py
import pytest
import pandas as pd
from src.model import PingPongModel
from src.config import FEATURES

@pytest.fixture
def sample_data():
    # Données mock pour tests
    data = {
        'rank_diff': [10, -5, 0],
        'recent_form1': [0.8, 0.6, 0.7],
        'recent_form2': [0.5, 0.7, 0.6],
        'head_to_head': [2, -1, 0],
        'outcome': [1, 0, 1]
    }
    return pd.DataFrame(data)

def test_model_train_predict(sample_data):
    X = sample_data[FEATURES]
    y = sample_data['outcome']
    
    model = PingPongModel()
    model.train(X, y)
    
    # Test prédiction
    proba = model.predict_proba(X)
    assert proba.shape == (3, 2)  # 3 samples, 2 classes
    
    # Test évaluation
    logloss = model.evaluate(X, y)
    assert logloss >= 0  # Log-loss positive
    
    # Test value bet
    value = model.calculate_value_bet(0.7, 2.0)  # Proba 0.7, odds 2.0 (implied 0.5)
    assert value > 0  # Devrait être positive car 0.7 > 0.5 + marge