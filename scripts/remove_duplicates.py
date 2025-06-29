import pandas as pd

# Load the dataset
df = pd.read_csv('data/dataset.csv')

# Drop duplicates
df_clean = df.drop_duplicates()

# Save the cleaned dataset
df_clean.to_csv('data/processed_dataset.csv', index=False)

print("✅ Duplicates removed and saved as processed_dataset.csv")
