import numpy as np
import pandas as pd
import streamlit as st
import joblib
from sklearn.metrics import mean_squared_error
from catboost import CatBoostRegressor


train = pd.read_csv('data/train_house.csv')
test = pd.read_csv('data/test_house.csv')
x_train = train.iloc[:, :-1]
y_train = np.log(train.iloc[:, -1])
x_test = test

cbr = CatBoostRegressor(
    iterations=800,
    learning_rate=0.1,
    max_depth=4,
    l2_leaf_reg=2
)

cbr.fit(x_train, y_train)

y_pred = cbr.predict(x_test)

joblib.dump(cbr, 'cbr_model.sav')