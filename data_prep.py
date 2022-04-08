import pandas as pd

df = pd.read_csv(r'data/database.csv')
print(df.head())

df.loc[3378, "Date"] = "02/23/1975"
df.loc[7512, "Date"] = "04/28/1985"
df.loc[20650, "Date"] = "03/13/2011"
df['date_parsed'] = pd.to_datetime(df['Date'], format="%m/%d/%Y")

df['year'] = df['date_parsed'].dt.year
df['month'] = df['date_parsed'].dt.year

print(df.head())
df.to_csv('data/kaggle_significant_earthquakes_database.csv', index=False)