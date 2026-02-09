import pandas as pd

df = pd.read_csv('/Users/sachabreugnon/Desktop/pret_defaut/data/application_data.csv', header=0)

# Nettoye d'abord (découpe par virgules)
if df.shape[1] == 1:
    df = df[0].str.split(',', expand=True)
    df.columns = df.iloc[0]  # Première ligne = entêtes
    df = df.iloc[1:]         # Données

# Sauvegarde en CSV PROPRE (séparateur point-virgule)
df.to_csv('/Users/sachabreugnon/Desktop/pret_defaut/data/application_data_clean.csv', 
          index=False, sep=';')

print(f"✅ CSV propre créé: {df.shape[0]:,} lignes × {df.shape[1]} colonnes")