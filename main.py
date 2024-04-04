import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime

CSV_FILE_PATH = "Melbourne_housing.csv"
df = pd.read_csv(CSV_FILE_PATH, delimiter=',')

print("CSV size before: ", df.shape)

df = df.dropna()
print("CSV size after: ", df.shape)
print(df.head())

df20 = df.sample(frac=0.2, random_state=1)
df = df.drop(df20.index)
print("CSV size 80: ", df.shape)
print("CSV size 20: ", df20.shape)

df.to_csv("Melbourne_housing_PROCESSED.csv", index=False) # Spremanje predprocesiranog skupa podataka u novu CSV datoteku
df20.to_csv("Melbourne_housing_PROCESSED_20.csv", index=False) # Spremanje 20% skupa podataka u novu CSV datoteku