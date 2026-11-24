# Paper review: News-implied Sovereign Default Risk

## Research question
Can news text capture sovereign risk promptly in settings where conventional ratings are slow and sovereign CDS data are unavailable or illiquid?

## Method described in the presentation
The authors' NSRI uses country-linked English-language news. Latent Dirichlet allocation filters articles into relevant topic groups. TF–IDF-weighted unigram and bigram representations are compared with a library of sovereign-default-related text using cosine similarity. Article scores are aggregated into country-day indices; the slides also discuss a tone-adjusted variant.

## Evidence discussed by the group
The presentation summarizes analyses of CDS spreads, sovereign rating downgrades, firm-level credit-risk spillovers, equity returns and a stylized market-timing strategy. It reports that current NSRI predicts subsequent CDS spread changes and higher downgrade risk, alongside negative equity-return relationships and robustness checks.

## Critical interpretation
Text-based measures may provide timely signals, particularly in less transparent markets. However, predictive association is not automatically causal. News-source coverage, language selection, publisher composition, changing market regimes, look-ahead risk in backtests and transaction costs all matter for practical use. These are analytical caveats, not independent replications or refutations of the paper.

## Source and scope
Based on the group's 27-slide presentation, especially slides 5–10 (motivation and measurement), 13–20 (empirical results), and 21–24 (robustness and conclusions). The original slide deck is not redistributed pending collaborator permission. The paper is *Hot off the Press: News-implied Sovereign Default Risk* by C. Dim, K. Koerner, M. Wolski and S. Zwart.
