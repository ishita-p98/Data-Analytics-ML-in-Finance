# Empirical findings reported in the research

The following findings summarize the original paper **as presented by the student group**. No regression, portfolio backtest or independent replication was performed for this GitHub case study.

## 1. Sovereign CDS spread changes

**Question:** Does current news-implied risk predict subsequent changes in sovereign CDS spreads?

The slides describe predictive panel regressions of future CDS spread changes on the current NSRI. They report statistically significant predictive relationships over **one-, three- and six-month horizons**. The interpretation offered is that relevant news information can precede adjustment in sovereign credit-derivative prices.

*Presentation source: slide 13.*

## 2. Sovereign credit-rating downgrades

The group reports that higher current NSRI is associated with a greater probability of an **S&P or Moody's downgrade over the following 3–12 months**. This supports the proposed early-warning application, while not establishing perfect forecasting accuracy.

*Presentation source: slide 14.*

## 3. Spillovers to domestic firms

The paper examines aggregate firm credit risk, including **probability of default (PD)** and **actuarial spread (AS)**. The slides state that regressions account for domestic macroeconomic conditions and global financial factors, using within-country changes over time. NSRI reportedly remains informative for subsequent firm credit risk.

*Presentation source: slide 15.*

## 4. Equity valuation

The presentation describes monthly country-level equity-return regressions with controls and country/year fixed effects, studying contemporaneous and subsequent changes in NSRI.

| Relationship | Magnitude reported on the slides |
| --- | --- |
| Contemporaneous equity return for a +1 SD NSRI change | **−0.41%**, or **−0.19% with controls** |
| Next-month equity return for a +1 SD NSRI change | **−0.27% to −0.31%** |
| Country-specific NSRI next-month effect | Approximately **−0.18%** |
| Global NSRI effect | Approximately **−0.74%** in the slide's market-cap-weighted discussion |

These are **reported regression relationships**, not independently verified causal impacts. The slide also reports that the first five principal components explain approximately 66% of NSRI variation, suggesting a substantial global component.

*Presentation sources: slides 16–18.*

## 5. Stylized market-timing illustration

The paper's illustrated strategy switches a country's equity allocation into a risk-free asset when its NSRI rises by at least **15% relative to the recent three-month average**, otherwise remaining in equities. Country strategies are aggregated using market-capitalization or GDP weights.

The slides present the following illustrative terminal wealth from an initial **$1**:

| Strategy | Terminal wealth shown |
| --- | ---: |
| Global equity buy-and-hold | $2.60 |
| NSRI-based strategy | $3.20 |
| Tone-adjusted NSRI strategy | $3.70 |

The slides also report higher Sharpe ratios and alpha of about **2.4%**. The presentation does not provide all implementation details needed to independently assess investability, transaction costs or live trading performance.

*Presentation source: slide 19.*

## 6. Information environments and robustness

The presentation reports that the signal is especially informative for lower-income countries and that economic news contributes prominently to topic-specific results. Robustness checks discussed include removing one country at a time, longer horizons, alternative specifications and market-timing variants.

These tests were **performed in the underlying research**, not rerun here.

*Presentation sources: slides 20–23.*

## Summary

The paper argues that sovereign-default-related news contains information relevant to sovereign CDS, ratings, domestic firm credit risk and equity markets. The evidence is potentially useful for risk monitoring, but must be interpreted with attention to model stability, coverage and the difference between forecasting and causation.

[Return to case study](README.md)
