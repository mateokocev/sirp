import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime

CSV_FILE_PATH = "Melbourne_housing.csv"
df = pd.read_csv(CSV_FILE_PATH, delimiter=',')

print("Veličina skupa (broj redaka, broj stupaca):", df.shape)

print("Nazivi stupaca:", df.columns.tolist())

print("Broj nedostajućih vrijednosti po stupcu:\n", df.isna().sum())

for column in df.columns:
    print(f"Jedinstvene vrijednosti u stupcu {column}: {df[column].nunique()}")

print("Tipovi podataka po stupcu:\n", df.dtypes)

for column in df.columns:
    print(f"Frekvencije vrijednosti u stupcu {column}:\n", df[column].value_counts())

print("\nAnaliza skupa podataka:")

print("Je li je skup podataka dovoljno velik?", df.shape[0] > 1000)

print("Je li skup ima dovoljno različite podatke?", df.nunique().sum() > df.shape[0])

missing_values = df.isna().sum().sum()
print("Je li skup ima puno nedostajućih vrijednosti?", missing_values > (df.shape[0] * df.shape[1] * 0.1))



#print("CSV size before: ", df.shape)

#df = df.dropna()
#print("CSV size after: ", df.shape)
#print(df.head())

#df20 = df.sample(frac=0.2, random_state=1)
#df = df.drop(df20.index)
#print("CSV size 80: ", df.shape)
#print("CSV size 20: ", df20.shape)

#df.to_csv("Melbourne_housing_PROCESSED.csv", index=False) # Spremanje predprocesiranog skupa podataka u novu CSV datoteku
#df20.to_csv("Melbourne_housing_PROCESSED_20.csv", index=False) # Spremanje 20% skupa podataka u novu CSV datoteku