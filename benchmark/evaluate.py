import os
import numpy as np
import pandas as pd
import pickle
from rectools.metrics import Precision, Accuracy, NDCG, Serendipity, calc_metrics
from rectools import Columns
from rectools.dataset import Dataset

def load_data():
    all_data = pd.read_csv('../data/interim/all_data.csv', low_memory=False)

    occutation = all_data['occupation'].unique()
    occutation_dict = {occutation[i]: i for i in range(len(occutation))}
    all_data['occupation'] = all_data['occupation'].apply(lambda x: occutation_dict[x])

    return all_data

def load_data_fold(fold):
    ratings = pd.read_csv(f'../data/interim/u{fold}_base.csv', low_memory=False)
    ratings.columns = Columns.User, Columns.Item, Columns.Weight, Columns.Datetime

    ratings_test = pd.read_csv(f'../data/interim/u{fold}_test.csv', low_memory=False)
    ratings_test = ratings_test[['user_id', 'item_id']]
    ratings_test.columns = Columns.User, Columns.Item

    return ratings, ratings_test

def create_dataset(all_data, ratings):
    users = all_data[['user_id', 'gender', 'age', 'occupation', 'zip_code']].drop_duplicates()
    users = users[~users.user_id.isna()]
    users = users.loc[users["user_id"].isin(ratings["user_id"])].copy()

    user_features_frames = []
    for feature in ["gender", "age", "occupation"]:
        feature_frame = users.reindex(columns=["user_id", feature])
        feature_frame.columns = ["id", "value"]
        feature_frame["feature"] = feature
        user_features_frames.append(feature_frame)
    user_features = pd.concat(user_features_frames)

    dataset = Dataset.construct(
        ratings,
        user_features_df=user_features,
        cat_user_features=["gender", "occupation"],
        make_dense_user_features=False
    )

    return dataset

def evaluate_model(model, ratings, test_df, dataset):

    recomendos = model.recommend(ratings['user_id'].unique(), dataset, filter_viewed=True, k=5)
    
    metrics = {
        "precision": Precision(k=5),
        "accuracy@1": Accuracy(k=1),
        "accuracy@10": Accuracy(k=10),
        "ndcg": NDCG(k=5, log_base=3),
        "serendipity": Serendipity(k=5)
    }

    catalog = test_df[Columns.Item].unique()
    results = calc_metrics(metrics, reco=recomendos, interactions=test_df, prev_interactions=test_df, catalog=catalog)
    return results

def load_model(path):
    with open(path, 'rb') as f:
        model = pickle.load(f)
    return model

def main():
    all_data = load_data()

    for fold in ['a', 'b']:
        print(f"Starting Fold {fold}")
        ratings, ratings_test = load_data_fold(fold)
        dataset = create_dataset(all_data, ratings)

        model = load_model(f'../models/implicit_alsa.pkl')
        results = evaluate_model(model, ratings, ratings_test, dataset)
        print(f"Results for Fold {fold}: {results}")

if __name__ == "__main__":
    main()
