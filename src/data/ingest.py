"""
Descarga el dataset California Housing y lo guarda en data/raw/.
"""
import pandas as pd
from pathlib import Path
from sklearn.datasets import fetch_california_housing


RAW_DIR = Path(__file__).parents[2] / "data" / "raw"


def ingest():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    dataset = fetch_california_housing(as_frame=True)
    df = dataset.frame  # features + target en un solo DataFrame

    output_path = RAW_DIR / "california_housing.csv"
    df.to_csv(output_path, index=False)
    print(f"Dataset guardado en {output_path}  ({len(df)} filas, {len(df.columns)} columnas)")


if __name__ == "__main__":
    ingest()
