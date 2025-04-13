from data_cleaning import clean
from data_preprocess import preprocess
from model_building import model
import pickle


def main():
    pipeline()


# & Run all the scripts and save/output necessary files
def pipeline(app_path="../app/static/data/"):
    cleaned_df = clean()
    preprocess()
    rfc_model, dtc_model, lr_model, knn_model, compare_df = model()

    # Save the clean data in the app folder for flask
    cleaned_df.to_csv(app_path + "cleaned_E_Commerce.csv", index=False)
    # Save the predicted data with actual values in the app folder for flask
    compare_df.to_csv(app_path + "compare_df.csv", index=False)

    # Save the models in both the app folder for flask and project's folder
    pckl = {
        "rfc_model": rfc_model,
        "dtc_model": dtc_model,
        "lr_model": lr_model,
        "knn_model": knn_model,
    }
    pickle.dump(
        pckl,
        open("../app/models/trained_models.pickle", "wb"),
    )  # Save the models in the app folder for flask
    pickle.dump(
        pckl,
        open("../models/trained_models.pickle", "wb"),
    )  # Save the models in the project's folder


if __name__ == "__main__":
    main()
