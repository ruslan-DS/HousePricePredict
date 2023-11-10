import numpy as np
import pandas as pd
import streamlit as st
from sklearn import *
from prediction import predict
from model import cbr
from time import sleep
import joblib


st.write("""
 # Страница для запуска выбранной модели
""")

st.success('Загружаем уже закодированные, нормализованные и предобработанные данные в обоих файлах')


upload_train = st.file_uploader('Загрука тренировочной выборки с целевым признаком:')
upload_test = st.file_uploader('Загрузка тестовых данных без целевого признака:')

train = None
test = None

if upload_train is not None:
    train = pd.read_csv(upload_train)
    X = train.iloc[:, :-1]
    Y = np.log(train.iloc[:, -1])

    if st.button('Нажми, чтобы модель начала тренироваться:'):
        cbr.fit(X, Y)
        sleep(3)
        st.success("Тренировка прошла успешна. Модель обучена.")


if upload_test is not None:
    test = pd.read_csv(upload_test)
    x_test = test

    if st.button('Нажми, чтобы модель предсказала результат на тестовой выборке:'):
        results = np.exp(predict(x_test))
        results = pd.DataFrame({'Id': np.arange(1461, 2920), 'SalePrice': results})
        st.dataframe(results)