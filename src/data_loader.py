# src/data_loader.py
import requests
import pandas as pd
from config import API_URL_MATCHES, API_KEY_MATCHES, API_URL_RANKINGS, API_KEY_RANKINGS, API_URL_ODDS, API_KEY_ODDS, DATA_PATH

def fetch_from_api(url, params=None, headers=None):
    """Fonction utilitaire pour fetch d'une API."""
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API error: {response.status_code} - {response.text}")

def fetch_matches(from_date=None, to_date=None):
    """Fetch matchs de l'API principale (e.g., Sportradar)."""
    params = {'api_key': API_KEY_MATCHES}
    if from_date: params['from'] = from_date
    if to_date: params['to'] = to_date
    data = fetch_from_api(API_URL_MATCHES, params)
    df_matches = pd.DataFrame(data['matches'])  # Adaptez au format
    return df_matches

def fetch_rankings():
    """Fetch rankings actuels (e.g., ITTF API)."""
    headers = {'Authorization': f'Bearer {API_KEY_RANKINGS}'}
    data = fetch_from_api(API_URL_RANKINGS, headers=headers)
    df_rankings = pd.DataFrame(data['rankings'])  # Adaptez
    return df_rankings

def fetch_odds(match_ids):
    """Fetch odds pour des matchs spécifiques (e.g., OddsAPI)."""
    params = {'api_key': API_KEY_ODDS, 'match_ids': ','.join(map(str, match_ids))}
    data = fetch_from_api(API_URL_ODDS, params)
    df_odds = pd.DataFrame(data['odds'])  # Adaptez
    return df_odds

def fetch_all_data(from_date=None, to_date=None):
    """Agrège données de plusieurs APIs."""
    df_matches = fetch_matches(from_date, to_date)
    df_rankings = fetch_rankings()
    
    # Merge rankings dans matches (e.g., sur player_id)
    df_matches = df_matches.merge(df_rankings, left_on='player1_id', right_on='player_id', suffixes=('_match', '_rank1'))
    df_matches = df_matches.merge(df_rankings, left_on='player2_id', right_on='player_id', suffixes=('', '_rank2'))
    
    # Fetch odds pour les matchs fetchés
    match_ids = df_matches['match_id'].tolist()
    df_odds = fetch_odds(match_ids)
    
    # Merge odds
    df_all = df_matches.merge(df_odds, on='match_id')
    
    # Sauvegarde
    df_all.to_csv(DATA_PATH, index=False)
    return df_all

# Exemple d'usage: df = fetch_all_data('2023-01-01', '2023-12-31')