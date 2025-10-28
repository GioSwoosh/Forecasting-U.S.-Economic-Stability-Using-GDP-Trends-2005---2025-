import pandas as pd

file_path = "GDP_2005_2025_final.csv"
df = pd.read_csv(file_path)

print("Intial Data Preview")
print(df.head())
print("\nColumns: ", df.columns.tolist())

df.columns = df.columns.str.strip()
melted_df = df.melt(id_vars=["Country"], var_name="Year", value_name="GDP")

melted_df["Year"] = melted_df["Year"].astype(int)
melted_df["GDP"] = pd.to_numeric(melted_df["GDP"], errors="coerce")

filtered_df = melted_df[melted_df["Country"].isin(["China", "United States"])]

filtered_df = filtered_df.sort_values(by=["Country", "Year"]).reset_index(drop=True)
filtered_df = filtered_df.dropna(subset=["GDP"])
filtered_df["GDP_Trillions"] = filtered_df["GDP"] / 1_000_000_000
print("\nFiltered Data Preview:")
print(filtered_df.head(10))

print("\nData Summary:")
print(filtered_df.describe())

output_path = "cleaned_gdp_china_usa.csv"
filtered_df.to_csv(output_path, index=False)
print(f"\nCleaned data saved to: {output_path}")