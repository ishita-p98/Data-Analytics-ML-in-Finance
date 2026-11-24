from pathlib import Path

import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    balanced_accuracy_score,
    roc_auc_score,
)
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "credit_rating_hw.xlsx"
OUTPUT = ROOT / "outputs" / "model_comparison.csv"
FEATURES = [
    "debt_to_assets", "current_ratio", "roa",
    "interest_coverage", "log_assets", "book_to_market",
]
RANDOM_STATE = 37


def evaluate(name, model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)
    probabilities = model.predict_proba(X_test)[:, 1]
    predictions = model.predict(X_test)
    return {
        "model": name,
        "test_accuracy": accuracy_score(y_test, predictions),
        "test_roc_auc": roc_auc_score(y_test, probabilities),
        "test_balanced_accuracy": balanced_accuracy_score(y_test, predictions),
        "test_average_precision": average_precision_score(y_test, probabilities),
    }


def main():
    if not DATA.exists():
        raise FileNotFoundError(
            "Place the authorized course workbook at "
            "01-credit-rating-downgrades/data/credit_rating_hw.xlsx"
        )

    df = pd.read_excel(DATA, index_col="company_id")
    required = FEATURES + ["downgrade", "year"]
    if df[required].isna().any().any():
        raise ValueError("Missing values found in required modelling columns.")
    if set(df["downgrade"].unique()) != {0, 1}:
        raise ValueError("Expected binary downgrade labels 0 and 1.")

    train = df.loc[df["year"] <= 2020]
    test = df.loc[df["year"] == 2021]
    if train.empty or test.empty:
        raise ValueError("Expected training years through 2020 and test year 2021.")

    X_train, y_train = train[FEATURES], train["downgrade"]
    X_test, y_test = test[FEATURES], test["downgrade"]
    print(f"Observations: {len(df)} | Train: {len(train)} | Test: {len(test)}")
    print(
        "Downgrade prevalence (train/test): "
        f"{y_train.mean():.3f} / {y_test.mean():.3f}"
    )

    models = [
        ("Majority-class baseline", DummyClassifier(strategy="prior")),
        (
            "Elastic-net logistic regression",
            make_pipeline(
                StandardScaler(),
                LogisticRegression(
                    l1_ratio=0.7, solver="saga",
                    max_iter=4000, random_state=RANDOM_STATE,
                ),
            ),
        ),
        (
            "L1 logistic regression",
            make_pipeline(
                StandardScaler(),
                LogisticRegression(
                    l1_ratio=1.0, solver="liblinear",
                    random_state=RANDOM_STATE,
                ),
            ),
        ),
        (
            "Random forest (100 trees, depth 3)",
            RandomForestClassifier(
                n_estimators=100, max_depth=3, random_state=RANDOM_STATE
            ),
        ),
        (
            "Gradient boosting (300 stages)",
            GradientBoostingClassifier(
                n_estimators=300, random_state=RANDOM_STATE
            ),
        ),
    ]

    results = [
        evaluate(name, model, X_train, y_train, X_test, y_test)
        for name, model in models
    ]

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    searches = [
        (
            "Tuned random forest",
            GridSearchCV(
                RandomForestClassifier(random_state=RANDOM_STATE),
                {"max_depth": [2, 3, 4, 5], "n_estimators": [100, 200, 300]},
                cv=cv, scoring="accuracy", n_jobs=-1,
            ),
        ),
        (
            "Tuned gradient boosting",
            GridSearchCV(
                GradientBoostingClassifier(random_state=RANDOM_STATE),
                {"n_estimators": [100, 200, 300, 400, 500]},
                cv=cv, scoring="accuracy", n_jobs=-1,
            ),
        ),
    ]

    for name, search in searches:
        search.fit(X_train, y_train)
        print(f"{name}: {search.best_params_}; CV accuracy={search.best_score_:.3f}")
        results.append(
            evaluate(name, search.best_estimator_, X_train, y_train, X_test, y_test)
        )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(results).to_csv(OUTPUT, index=False)
    print(f"Saved results to {OUTPUT}")


if __name__ == "__main__":
    main()
