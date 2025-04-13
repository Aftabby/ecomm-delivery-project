import pandas as pd
from sklearn.preprocessing import LabelEncoder


def main():
    preprocess()


def preprocess(
    path="../data/processed/cleaned_E_Commerce.csv",
    out_path="../data/processed/preprocessed_E_Commerce.csv",
):
    # Load the cleaned dataset
    df = pd.read_csv(path)
    # Get all the catogorical columns
    cat_cols = df.select_dtypes(include=["object"]).columns.tolist()
    # Label Encoder Object
    le = LabelEncoder()

    # Label encoding
    for col in cat_cols:
        le.fit(df[col])
        df[col] = le.transform(df[col])

    # Save the preprocessed dataset
    df.to_csv(out_path, index=False)

    return df


if __name__ == "__main__":
    main()
