from surprise import *

import pandas as pd


# function to train the model 
def train_model():
    df = pd.read_csv('laptops.csv')
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['user_id', 'laptop_id', 'rating']], reader)
    trainset = data.build_full_trainset()
    algo = SVD()
    algo.train(trainset)
