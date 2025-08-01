# -*- coding: utf-8 -*-
"""StudentScoreDatasetUsingLinearRegressionModel.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QwuYC3R_7jF_vxwNAM7h0RRjbhovlz-3

Project : Student Score Dataset using Linear Regression Model
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#from google.colab import files

# Upload multiple files
#uploaded_files = files.upload()

df =pd.read_csv("/content/rounded_hours_student_scores.csv")
df.head()
#df.info()

#X = df[['Hours']]
#y = df['Scores']

df_array = np.array(df)
X = df_array[:, 0].reshape(-1, 1)  # first column = Hours
y = df_array[:, 1]

#split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42) #Using test_size=0.1 instead of 0.2 giving better results

#train the model (Linear Regression)
model = LinearRegression()
model.fit(X_train,y_train)

import matplotlib.pyplot as plt
import seaborn as sns

y_pred = model.predict(X_test)
plt.scatter(y_test, y_pred)
plt.xlabel('Tested Score')
plt.ylabel('Predicted Score')
plt.title('Tested Vs Predicted Score')
plt.grid(True)
plt.show()

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('Mean Squared Error:', mse)
print('R-squared:', r2)

def predict_score(hours):
    # Convert input to 2D array because model expects it
    hours_array = np.array([[hours]])

    # Predict the score using the trained model
    predicted_score = model.predict(hours_array)[0]

    # Return the predicted score (as a number or formatted string)
    return predicted_score  # or: return f"Predicted Score: {predicted_score:.2f}"

!pip install gradio
import gradio as gr

interface = gr.Interface(
    fn=predict_score,
    inputs = [

        #gr.Number(label='Total Score'),
        gr.Number(label='Number of Hours of Study'),
    ],
    outputs = gr.Textbox(label='Predicted Score'),
    title = 'Project 1 - Score Prediction',
    description = "Student Score Dataset"
    )
interface.launch(debug=True)
