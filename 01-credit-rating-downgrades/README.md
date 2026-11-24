# Predicting Credit Rating Downgrades with Machine Learning

**Research question:** Can lagged firm financial characteristics help identify future credit-rating downgrades?

## Overview
An individual course assignment for **Data Analytics & Machine Learning in Finance**. The exercise studies binary downgrade prediction using six firm-level financial indicators and several classification methods. It is an academic exercise, not a production credit-risk model.

## Data and evaluation
- Course workbook: 1,877 firm-year observations from 2017–2021, six explanatory financial variables and a binary downgrade indicator.
- Training period: 2017–2020 (1,516 observations); held-out test: 2021 (361 observations).
- Downgrade prevalence: 24.7% in training versus 13.3% in testing. A majority-class predictor therefore has deceptively high test accuracy.
- Models: elastic-net and L1 logistic regression, random forest and gradient boosting, with a majority-class baseline.
- Metrics: accuracy, ROC AUC, balanced accuracy and average precision.

## Reproduce
1. Obtain the course dataset through an authorized source.
2. Place `credit_rating_hw.xlsx` in `data/` locally. The workbook is intentionally excluded from Git.
3. Install dependencies with `pip install -r requirements.txt`.
4. From this folder run `python src/run_analysis.py` or open `notebooks/credit_rating_analysis.ipynb`.
5. The script writes model metrics to `outputs/model_comparison.csv`.

## Findings from the submitted assignment
The submitted notebook reported test ROC AUC around 0.61 for both logistic models and the shallow random forest, and around 0.56 for 300-stage gradient boosting. Gradient boosting's reported training ROC AUC (around 0.99) was substantially higher than its test ROC AUC, consistent with overfitting or temporal instability. These are original submission outputs, not a claim of validated forecasting performance.

The published `outputs/model_comparison_untuned.csv` records the untuned comparison reproduced during preparation. The full tuning workflow is available in the script and should be rerun with the authorized workbook before relying on tuned metrics.

## Limitations
- The dataset is small; outputs are not calibrated probabilities of actual default.
- The downgrade rate changes substantially between training and test periods.
- The assignment specifies shuffled stratified five-fold CV for tuning. For deployment-oriented model selection, forward-chaining validation would better respect time ordering.
- Some firms recur across years, so observations are not fully independent.
- The source describes financial inputs as lagged, but their precise availability dates cannot be verified independently from the workbook alone.

## Attribution and sharing
Adapted from an individual course submission. The original assignment handout, source workbook and student-ID notebook are not redistributed. The public-facing notebook removes the student identifier. No open-source license is granted by default.
