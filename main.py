# main.py (updated)
from src.trainer import train_model
from src.predictor import predict_match
from apscheduler.schedulers.background import BackgroundScheduler  # Pour auto-retrain

def main():
    # Entraînement initial
    model = train_model(retrain=True)
    
    # Exemple prédiction
    sample_features = {'rank_diff': 10, 'recent_form1': 0.7, 'recent_form2': 0.5, 'head_to_head': 1}
    print(predict_match(sample_features))
    
    # Scheduling pour retraining auto (e.g., tous les 7 jours)
    scheduler = BackgroundScheduler()
    scheduler.add_job(train_model, 'interval', days=7, args=[True])
    scheduler.start()
    # Run forever ou intégrez à app

if __name__ == "__main__":
    main()