# News-Implied Sovereign Default Risk — Research Paper Presentation

**Research question:** Can financial news provide an early signal of sovereign credit risk before traditional measures respond?

## Overview
Collaborative academic presentation for **Data Analytics & Machine Learning in Finance**, reviewing *Hot off the Press: News-implied Sovereign Default Risk* by C. Dim, K. Koerner, M. Wolski and S. Zwart (originally circulated in 2021; the presentation refers to an April 2024 revision).

The group presented and interpreted the paper's methods and reported findings. **This is a paper review, not an original implementation of the authors' NLP pipeline or an independent replication.** The original presentation identifies seven presenters; individual slide ownership has not been established, so this repository does not assign sole authorship.

## What the presentation covers
1. **Motivation:** official sovereign ratings and macroeconomic indicators may lag events, while CDS markets can be illiquid.
2. **NSRI methodology:** topic filtering with latent Dirichlet allocation, TF–IDF text representations and cosine similarity to a sovereign-default language library.
3. **Empirical tests summarized by the paper:** CDS spread changes, rating downgrades, firm credit risk, equity returns and market timing.
4. **Robustness:** alternative specifications, country exclusions and different forecast horizons.

## Selected findings reported in the slides
- Higher NSRI predicts CDS spread increases over one-, three- and six-month horizons.
- Higher NSRI is associated with a greater probability of a sovereign downgrade over the next three to twelve months.
- The presentation reports negative subsequent equity-return relationships and illustrates a hypothetical NSRI-based market-timing strategy.

These are **findings as summarized by the paper and group presentation**, not independently estimated or replicated in this repository.

## Materials and permissions
The 27-page group slide deck is not included because it identifies multiple collaborators and permission to redistribute it publicly has not been confirmed. The paper itself is also not redistributed; readers should consult the publisher or authors for the authoritative version.

## Attribution
Original research credit belongs to Dim, Koerner, Wolski and Zwart. This repository documents a collaborative student presentation and does not claim exclusive authorship or original empirical replication.
