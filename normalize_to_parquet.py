import pandas as pd

df1 = pd.read_csv('World Important Dates.csv')  
print("Первый датасет загружен. Строк:", len(df1))

df1['Year'] = pd.to_numeric(df1['Year'], errors='coerce')
df1 = df1.dropna(subset=['Year'])
df1['Year'] = df1['Year'].astype(int)

df1.to_parquet('events_cleaned.parquet', index=False)
print("События сохранены в events_cleaned.parquet")

df2 = pd.read_csv('Road Accident Data.csv')  
print("Второй датасет загружен. Строк:", len(df2))

df2 = df2.drop_duplicates()

df2.to_parquet('accidents_cleaned.parquet', index=False)
print("ДТП сохранены в accidents_cleaned.parquet")