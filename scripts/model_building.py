import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV


def main():
    model()


def model(
    path="../data/processed/preprocessed_E_Commerce.csv",
    model_path="../models/trained_model.pickle",
):
    # load preprocessed data
    df = pd.read_csv(path)

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        df.drop("Reached.on.Time_Y.N", axis=1),
        df["Reached.on.Time_Y.N"],
        test_size=0.2,
        random_state=42,
    )
    # Also, include the actual target values (y_test) with all the model's predicted value for comparison in webapp. And pass it then to the pipeline
    compare_df = pd.DataFrame({"actual": y_test.reset_index(drop=True)})

    ## RANDOM FOREST CLASSIFIER
    rfc = RandomForestClassifier()
    # Hyperparameter tuning using GridSearchCV
    param_grid = {
        "max_depth": [4, 8, 12, 16],
        "min_samples_leaf": [2, 4, 6, 8],
        "min_samples_split": [2, 4, 6, 8],
        "criterion": ["gini", "entropy"],
        "random_state": [42],
    }
    # GridSearchCV object
    grid = GridSearchCV(
        estimator=rfc,
        param_grid=param_grid,
        cv=5,
        n_jobs=-1,
        verbose=2,
        scoring="accuracy",
    )
    # Fit the model
    grid.fit(X_train, y_train)
    # Get the best parameters
    best_params = grid.best_params_

    # Random Forest Classifier with best parameters
    rfc = RandomForestClassifier(
        max_depth=best_params["max_depth"],
        min_samples_leaf=best_params["min_samples_leaf"],
        min_samples_split=best_params["min_samples_split"],
        criterion=best_params["criterion"],
        random_state=best_params["random_state"],
    )
    # Fit the model
    rfc.fit(X_train, y_train)
    # Include all the model's predicted value for comparison in webapp. And pass it then to the pipeline
    compare_df["rfc_pred"] = rfc.predict(X_test)

    ## Decision Tree Classifier
    # Decision Tree Classifier with default parameters
    dtc = DecisionTreeClassifier()
    # Hyperparameter tuning using
    param_grid = {
        "max_depth": [2, 4, 6, 8],
        "min_samples_leaf": [2, 4, 6, 8],
        "min_samples_split": [2, 4, 6, 8],
        "criterion": ["gini", "entropy"],
        "random_state": [42],
    }
    # GridSearchCV object
    grid = GridSearchCV(
        estimator=dtc,
        param_grid=param_grid,
        cv=5,
        n_jobs=-1,
        verbose=2,
        scoring="accuracy",
    )
    # Fit the model
    grid.fit(X_train, y_train)
    # Get the best parameters
    best_params = grid.best_params_

    # Decision Tree Classifier with best parameters
    dtc = DecisionTreeClassifier(
        max_depth=best_params["max_depth"],
        min_samples_leaf=best_params["min_samples_leaf"],
        min_samples_split=best_params["min_samples_split"],
        criterion=best_params["criterion"],
        random_state=best_params["random_state"],
        class_weight="balanced",
    )
    # Fit the model
    dtc.fit(X_train, y_train)
    # Include all the model's predicted value for comparison in webapp. And pass it then to the pipeline
    compare_df["dtc_pred"] = dtc.predict(X_test)

    ## Logistic Regression
    # Scale the data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    # Logistic Regression object with default parameters
    lr = LogisticRegression(max_iter=500)
    # Fitting the model
    lr.fit(X_train_scaled, y_train)
    # Include all the model's predicted value for comparison in webapp. And pass it then to the pipeline
    compare_df["lr_pred"] = lr.predict(X_test_scaled)

    ## K Nearest Neighbors Classifier
    # K Nearest Neighbors Classifier Object with default parameters
    knn = KNeighborsClassifier()
    # Fitting the model
    knn.fit(X_train, y_train)
    # Include all the model's predicted value for comparison in webapp. And pass it then to the pipeline
    compare_df["knn_pred"] = knn.predict(X_test)

    return rfc, dtc, lr, knn, compare_df


if __name__ == "__main__":
    main()
