import numpy as np
import pandas as pd
from sklearn.datasets import (
    fetch_openml,
    load_breast_cancer,
    load_wine,
    make_classification,
)


def load_german_credit() -> tuple[np.ndarray]:

    german_credit_df = fetch_openml(name="credit-g", version=1, as_frame=True).frame
    german_credit_df["sex"] = german_credit_df["personal_status"].apply(
        lambda x: 1 if "female" in x else 0
    )
    german_credit_df["single"] = german_credit_df["personal_status"].apply(
        lambda x: 1 if "single" in x else 0
    )
    german_credit_df.drop(columns=["personal_status"], inplace=True)

    german_credit_df = pd.get_dummies(
        german_credit_df,
        columns=german_credit_df.select_dtypes(include="category").columns,
        dtype=float,
        drop_first=True,
    )

    german_credit_df = german_credit_df[
        ["sex"] + [x for x in german_credit_df.columns if x != "sex"]
    ]
    target_class = [col for col in german_credit_df.columns if col.startswith("class")][
        0
    ]
    X = german_credit_df.drop(target_class, axis=1).values.astype(int)
    y = german_credit_df[target_class].values
    return X, y


def get_datasets_dict() -> dict[str, tuple[np.ndarray]]:
    breast_cancer_data = load_breast_cancer(return_X_y=True)
    wine_x, wine_y = load_wine(return_X_y=True)
    wine_y[wine_y >= 1] = 1  # good
    wine_y[wine_y < 1] = 0  # bad
    random_binary_data = make_classification(n_classes=2)

    return {
        "BreastCancer": breast_cancer_data,
        "WineQuality": (wine_x, wine_y),
        "RandomBinary": random_binary_data,
        "GermanCredit": load_german_credit(),
    }
