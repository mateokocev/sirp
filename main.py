import pandas as pd

CSV_FILE_PATH = "Melbourne_housing.csv"
df = pd.read_csv(CSV_FILE_PATH, delimiter=',')

print("Veličina skupa (broj redaka, broj stupaca):", df.shape)

print("Nazivi stupaca:", df.columns.tolist())

for column in df.columns:
    print(f"Jedinstvene vrijednosti u stupcu {column}: {df[column].nunique()}")

print("Tipovi podataka po stupcu:\n", df.dtypes)

print("Broj nedostajućih vrijednosti po stupcu:\n", df.isna().sum())

print("CSV size before: ", df.shape)

df = df.dropna()
print("CSV size after: ", df.shape)
print(df.head())

df20 = df.sample(frac=0.2, random_state=1)
df = df.drop(df20.index)
print("CSV size 80: ", df.shape)
print("CSV size 20: ", df20.shape)

df.to_csv("Melbourne_housing_PROCESSED.csv", index=False)
df20.to_csv("Melbourne_housing_PROCESSED_20.csv", index=False)