import pandas as pd
import numpy as np
from .config import FEATURES, TARGET, PROCESSED_PATH  # Import relatif

def preprocess_data(df):
    """
    Prétraitement: Feature engineering, nettoyage.
    Formules: rank_diff = rank1 - rank2, recent_form = wins/last_5_matches, etc.
    """
    # Nettoyage basique
    df = df.dropna(subset=FEATURES + [TARGET])
    
    # Features mathématiques
    df['rank_diff'] = df['rank1'] - df['rank2']
    df['recent_form1'] = df['wins_last5_1'] / 5  # Assume colonne existante
    df['recent_form2'] = df['wins_last5_2'] / 5
    df['head_to_head'] = df['h2h_wins1'] - df['h2h_wins2']  # Différence de victoires head-to-head
    
    # Sélection
    processed_df = df[FEATURES + [TARGET]]
    processed_df.to_csv(PROCESSED_PATH, index=False)
    return processed_df