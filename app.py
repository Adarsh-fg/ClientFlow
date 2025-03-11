import pickle as pkl
import streamlit as st
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd

model = pkl.load(open('model.pkl', 'rb'))

st.title('Bank Churn Prediction App')
st.write('This is a simple Bank Churn Prediction App built with Streamlit')

# Collects user input features into dataframe
CreditScore = st.slider('Credit Score', 0, 1000, 500)
Age = st.slider('Age', 18, 100, 35)
Gender = st.selectbox('Gender',['Male','Female'])
Tenure = st.slider('Tenure', 0, 10, 5)
Balance = st.slider('Balance', 0, 5000000, 100000)
NumOfProducts = st.slider('Number of Products', 1, 5, 3)
HasCrCard = st.selectbox('Has Credit Card', [0, 1])
IsActiveMember = st.selectbox('Is Active Member', [0, 1])
EstimatedSalary = st.slider('Estimated Salary', 0, 500000, 100000)
Geography = st.selectbox('Country', ['France', 'Germany', 'Spain'])

input_dict = {'CreditScore': CreditScore, 'Age': Age, 'Gender': Gender, 'Tenure': Tenure, 'Balance': Balance,
              'NumOfProducts': NumOfProducts, 'HasCrCard': HasCrCard, 'IsActiveMember': IsActiveMember,
                'EstimatedSalary': EstimatedSalary, 'Geography': Geography}

input_df = pd.DataFrame([input_dict])

# Encoding categorical variables
input_df['Gender'] = input_df['Gender'].map({'Male':1,'Female':0})
input_df['Geography'] = input_df['Geography'].map({'France':0,'Spain':1,'Germany':2})

df = pd.read_csv("X.csv")
columns_list = [col for col in df.columns if col != 'Unnamed: 0']

input_df = input_df.reindex(columns=columns_list, fill_value=0)

# Apply model to make predictions
prediction = model.predict(input_df)

if st.button('Predict'):
    prediction = model.predict(input_df)

    # Output the prediction
    if prediction[0] == 1:
        st.error("Exited")
    else:
        st.success("Not Exited")