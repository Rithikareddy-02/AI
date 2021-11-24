import numpy as np
import pandas as pd

"""#Load Data"""
excel_file = 'Ageremoved_dataset.xlsx'
sheet_name = 'data'

data  = pd.read_excel(excel_file,
                    sheet_name = sheet_name,
                    usecols = 'A:F',
                    header = 0)

"""#Data Split"""

from sklearn.model_selection import train_test_split
df_train, df_test = train_test_split(data, train_size = 0.7, test_size = 0.3, random_state = 100)

"""#Dividing the training data set into X and Y

"""

y_train = df_train.pop('Specs')
X_train = df_train
y_test = df_test.pop('Specs')
X_test = df_test

"""#Model Training"""

from sklearn.linear_model import LogisticRegression
lr_model = LogisticRegression()
lr_model.fit(X_train,y_train)

y_pred_train = lr_model.predict(X_train)
y_pred_test = lr_model.predict(X_test)

train_accuracy = lr_model.score(X_train, y_train)
test_accuracy = lr_model.score(X_test, y_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred_test)

confusion_matrix(y_train, y_pred_train)