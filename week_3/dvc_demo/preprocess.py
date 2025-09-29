import pandas as pd

df = pd.read_csv("raw_data.csv")
df["age_plus_5"] = df["age"] + 5
df.to_csv("processed_data.csv", index=False)

# index=False means don’t write the row index into the CSV file
