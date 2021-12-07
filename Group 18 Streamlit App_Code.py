import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import pickle
from sklearn.preprocessing import MinMaxScaler
from Random_forest_regression import *
import joblib, os
st.set_page_config(page_title='Package Prediction')
st.header('Package Predictor')

excel_file = 'AI_Project_data_final.xlsx'
sheet_name = 'data'

data  = pd.read_excel(excel_file,
                    sheet_name = sheet_name,
                    usecols = 'A:N',
                    header = 0)

list_of_columns = data.columns
input_data=pd.DataFrame(columns=list_of_columns)
input_data.drop(['Package'], axis='columns', inplace=True)


input_data.at[0, 'SSC'] = st.slider('SSC Percentage : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'Inter'] = st.slider('Inter Percenatge : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'B.Tech 3-1'] = st.slider('B.tech Percenatge : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'IP'] = st.slider('IP Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'PSP'] = st.slider('PSP Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'ELCS LAB'] = st.slider('ELCS Lab Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'ENGLISH 1'] = st.slider('English 1 : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'DS'] = st.slider('DS Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'OS'] = st.slider('OS Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'DBMS'] = st.slider('DBMS Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'OOPC'] = st.slider('OOPC Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'CN'] = st.slider('CN Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )
input_data.at[0, 'WT'] = st.slider('WT Marks : ',
                                        min_value = 0,
                                        max_value = 100,
                                        )

if st.button("Predict the Package"):
    result =  regressor.predict(input_data)
    Package=result*(package_max-package_min)+package_min
    st.text('Predicted  Package = ')
    st.text(Package)