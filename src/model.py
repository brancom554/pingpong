from sklearn.ensemble import RandomForestClassifier  # Ou LogisticRegression pour probas simples
from sklearn.metrics import log_loss
from config import HYPERPARAMS

class PingPongModel:
    def __init__(self):
        self.model = RandomForestClassifier(**HYPERPARAMS)
    
    def train(self, X, y):
        self.model.fit(X, y)
    
    def predict_proba(self, X):
        """
        Prédictions probabilistes: Retourne [P(loss), P(win)] pour player1.
        Formule sous-jacente: Probabilités issues du modèle (e.g., softmax pour RF).
        """
        return self.model.predict_proba(X)
    
    def evaluate(self, X, y):
        """
        Évaluation avec log-loss pour paris (métrique adaptée aux probas).
        Formule: -1/N sum [y log(p) + (1-y) log(1-p)]
        """
        preds = self.predict_proba(X)[:, 1]  # Proba de win
        return log_loss(y, preds)
    
    def calculate_value_bet(self, proba_win, odds_win):
        """
        Amélioration: Détecter value bets.
        Formule: Value = (proba_win * (odds_win - 1)) - (1 - proba_win)
        Si >0, value bet.
        """
        implied_prob = 1 / odds_win
        if proba_win > implied_prob + 0.05:  # Marge de 5%
            return (proba_win * (odds_win - 1)) - (1 - proba_win)
        return 0