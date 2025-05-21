from src.ingest import load_csv_to_df
from src.transform import preprocess_air_quality_uci
import os

RAW_PATH = "data/raw/AirQualityUCI.csv"
PROCESSED_PATH = "data/processed/air_quality_clean.parquet"

if __name__ == "__main__":
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    print("Loading raw data...")
    df = load_csv_to_df(RAW_PATH)
    print("Columns:", df.columns.tolist())
    print("First few rows:")
    print(df.head())

    print("Transforming data...")
    clean_df = preprocess_air_quality_uci(df)
    print(f"Cleaned data shape: {clean_df.shape}")

    print("Saving clean data...")
    clean_df.to_parquet(PROCESSED_PATH)

    print("Done. Clean data saved to:", PROCESSED_PATH)
