# Movie Recommender System

## Arina Yartseva a.yartseva@innopolis.university B21_AAI01

## Overview
This repository contains all the components for a movie recommender system using model based on the Implicit Alternating Least Squares (ALS) algorithm.

## Contents
- `data/`: This directory contains datasets at different stages of processing:
  - `interim/`: Intermediate data that has been transformed.
  - `raw/`: The original, immutable data dump.
- `models/`: Includes the trained and serialized models, along with final checkpoints.
- `notebooks/`: Jupyter notebooks for data exploration, model training, and evaluation. The naming convention includes a number for ordering, followed by a description, e.g., `1.0-data-preprocessing.ipynb`.
- `references/`: Data dictionaries, manuals, and any other materials that provide additional context or explanations.
- `reports/`: Contains all reporting materials:
  - `figures/`: Graphics and figures generated during analysis.
  - `final_report.pdf`: Comprehensive report detailing all phases of the project.
- `benchmark/`: Scripts and datasets for evaluating the performance of the models.

## How to Run
To execute the model and evaluate its performance, follow these command-line steps:

1. Clone the repository to your local machine:
   ```bash
   git clone [URL of Your Repository]
   cd movie-recommender-system
    ```
2. (Optional) If you're using a virtual environment, set it up and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Navigate to the notebooks/ directory:
    ```bash
    cd notebooks/
    ```
5. Run the Jupyter notebooks in order. 


For model evaluation:

1. Navigate back to the root directory and then to the benchmark/ directory:
    ```bash
    cd ../benchmark/
    ```

2. Run the evaluation script:
    ```bash
    python3 evaluate.py
    ```

## Results
The system's performance was evaluated using various metrics, which are organized in the report in a multi-column format for clarity.

| Metric        | u1_base and u1_test | ua_base and ua_test | ub_base and ub_test |
|---------------|---------------------|---------------------|---------------------|
| Precision     | 0.5137              | 0.2986              | 0.0776              |
| Accuracy@10   | 0.9692              | 0.9849              | 0.9832              |
| Accuracy@1    | 0.9693              | 0.9910              | 0.9905              |
| NDCG          | 0.5424              | 0.3253              | 0.0758              |
| Serendipity   | 0.0023              | 0.0045              | 0.0013              |
