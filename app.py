import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import pickle
from sklearn.preprocessing import MinMaxScaler
from finalized_with_libraries import *

st.set_page_config(page_title='Spectacles Predictor')
st.header('Spectacles Prediction for youngsters')

excel_file = 'Ageremoved_dataset.xlsx'
sheet_name = 'data'

data  = pd.read_excel(excel_file,
                    sheet_name = sheet_name,
                    usecols = 'A:F',
                    header = 0)

list_of_columns = data.columns
input_data=pd.DataFrame(columns=list_of_columns)
input_data.drop(['Specs'], axis='columns', inplace=True)

input_data.at[0, 'phone'] = st.slider('phone:',
                            min_value = 0,
                            max_value = 24,
                            )
input_data.at[0, 'Laptop'] = st.slider('Laptop:',
                            min_value = 0,
                            max_value = 24,
                            )
input_data.at[0, 'TV'] = st.slider('TV:',
                            min_value = 0,
                            max_value = 24,
                            )

input_data.at[0, 'Headaches'] = st.radio("Do you have headaches",
                                ('yes', 'no'))

input_data.at[0, 'Blurry vision'] = st.radio("Do you have blurry vision",
                                    ('yes', 'no'))

varlist =  ['Headaches', 'Blurry vision']

def binary_map(x):
    return x.map({'yes': 1, "no": 0})

input_data[varlist] = input_data[varlist].apply(binary_map)


if st.button("Predict"):

    y_pred =  lr_model.predict(input_data)

    if(y_pred[0]==1):
        st.text('You need specs')
    if(y_pred[0]==0):
        st.text('You do not need specs')