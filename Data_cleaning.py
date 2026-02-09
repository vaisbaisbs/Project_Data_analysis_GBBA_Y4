import pandas as pd
import numpy as np

# 1. Charger
df = pd.read_csv('/Users/sachabreugnon/Desktop/pret_defaut/data/application_data_clean.csv', 
                 sep=';', header=0)

print(f"📊 Données: {df.shape[0]:,} lignes × {df.shape[1]} colonnes")
print(f"🔤 Noms des colonnes: {list(df.columns)[:10]}...")

# 2. Nettoie
# Doublons
doublons = df.duplicated().sum()
if doublons > 0:
    df = df.drop_duplicates()
    print(f"✅ {doublons} doublons supprimés")

# Missing values
missing = df.isnull().sum().sum()
print(f"🔍 {missing:,} valeurs manquantes")
df_clean = df.dropna()
print(f"Lignes supprimées: {len(df) - len(df_clean)}")

if 'TARGET' not in df.columns:
    print(f"\n❌ ERREUR: Colonne 'TARGET' non trouvée!")
    print(f"   Colonnes disponibles: {list(df.columns)}")

# 3. Analyse de TARGET
print(f"\n✅ Colonne TARGET trouvée!")
print(f"   Type de données: {df['TARGET'].dtype}")
print(f"   Valeurs uniques: {sorted(df['TARGET'].dropna().unique().tolist())}")

# 4. Compter positifs et négatifs
cas_positifs = (df['TARGET'] == 1).sum()   # Défauts
cas_negatifs = (df['TARGET'] == 0).sum()   # Non-défauts
total = cas_positifs + cas_negatifs

print(f"\n✅ ANALYSE TARGET:")
print("-" * 30)
print(f"Cas positifs (défauts = 1)   : {cas_positifs:,}")
print(f"Cas négatifs (non-défauts = 0): {cas_negatifs:,}")
print(f"Total échantillon            : {total:,}")

# 5. Calculer les proportions
proportion_positifs = (cas_positifs / total) * 100 if total > 0 else 0
proportion_negatifs = (cas_negatifs / total) * 100 if total > 0 else 0

print(f"\n📈 PROPORTIONS:")
print("-" * 30)
print(f"Proportion de défauts      : {proportion_positifs:.2f}%")
print(f"Proportion de non-défauts  : {proportion_negatifs:.2f}%")


# 6. regarder les types de données 
print("Types de données par colonne:")
for col in df.columns:
    dtype = df[col].dtype
    print(f"{col}: {dtype}")

# 4. Sauvegarde
df.to_csv('/Users/sachabreugnon/Desktop/pret_defaut/data/data_clean.csv', 
          index=False, sep=';')
print(f"\n💾 Données nettoyées sauvegardées")