"""
Lee data/raw/california_housing.csv, aplica preprocesamiento y guarda
los splits de entrenamiento y prueba en data/processed/.
"""
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


RAW_PATH = Path(__file__).parents[2] / "data" / "raw" / "california_housing.csv"
PROCESSED_DIR = Path(__file__).parents[2] / "data" / "processed"
TARGET = "MedHouseVal"


def preprocess(test_size: float = 0.2, random_state: int = 42):
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_PATH)

    # Eliminar duplicados y filas con nulos
    df = df.drop_duplicates().dropna()

    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Escalar features (fit solo en train para evitar data leakage)
    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X.columns)

    # Guardar splits
    X_train_scaled.to_csv(PROCESSED_DIR / "X_train.csv", index=False)
    X_test_scaled.to_csv(PROCESSED_DIR / "X_test.csv", index=False)
    y_train.reset_index(drop=True).to_csv(PROCESSED_DIR / "y_train.csv", index=False)
    y_test.reset_index(drop=True).to_csv(PROCESSED_DIR / "y_test.csv", index=False)

    print(f"Train: {len(X_train_scaled)} filas | Test: {len(X_test_scaled)} filas")
    print(f"Archivos guardados en {PROCESSED_DIR}")


if __name__ == "__main__":
    preprocess()
