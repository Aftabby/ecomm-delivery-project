import pandas as pd


def main():
    clean()


def clean(
    path="../data/raw/E_Commerce.csv",
    out_path="../data/processed/cleaned_E_Commerce.csv",
):
    # Load the data
    df = pd.read_csv(path)
    # Drop index column
    df.drop(["ID"], axis=1, inplace=True)
    # Drop duplicates
    df.drop_duplicates(inplace=True)
    # Save the cleaned data
    df.to_csv(out_path, index=False)

    return df


if __name__ == "__main__":
    main()
