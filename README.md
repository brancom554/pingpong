# PingPong Predictor

Une application Python pour prédire les pronostics de paris sportifs en tennis de table. Intègre des APIs de données, un modèle ML pour l'entraînement automatique, et la gestion des prédictions.

## Structure
- `data/`: Données brutes et traitées.
- `models/`: Modèles sauvegardés.
- `src/`: Code source principal.
- `api/`: API FastAPI pour exposer les prédictions.
- `tests/`: Tests unitaires.

## Installation
1. Clonez le repo: `git clone <url>`
2. Installez les dépendances: `pip install -r requirements.txt`
3. Configurez `src/config.py` avec votre API key et URL.

## Usage
- Entraîner le modèle: `python main.py`
- Prédire: Utilisez `predict_match()` dans `predictor.py` ou lancez l'API avec `uvicorn api.main:app --reload` et POST sur `/predict`.

## Améliorations
- Ajoutez plus de features (e.g., surface, fatigue).
- Passez à un modèle deep learning (e.g., avec TensorFlow).
- Intégrez à une app frontend.

## Tests
Exécutez `pytest tests/`.