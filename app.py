import streamlit as st
import joblib
import pandas as pd

# Set up the title and load the model
st.title('Fraud Catcher.ML 🦹‍♂')
model = joblib.load('dat.pkl')
sc=joblib.load('d.pkl')

    

col1, col2 = st.columns([1, 2])
col1.title('Result:')

with st.form('detection'):
    options = ['CASH_IN','CASH_OUT','DEBIT','PAYMENT','TRANSFER']
    columns = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'type_CASH_IN',	'type_CASH_OUT','type_DEBIT','type_PAYMENT','type_TRANSFER']
    # Collect inputs
    a = []
    a.append(float(st.text_input('Amount', '1254092.1')))
    a.append(float(st.text_input('Originating old Balance', '1254092.1')))
    a.append(float(st.text_input('Originating new Balance', '0')))
    a.append(float(st.text_input('Destination old Balance', '0')))
    a.append(float(st.text_input('Destination new Balance', '1254092.1')))
    transaction_type = st.selectbox("Choose a Payment Methods:", options)
    # Create DataFrame with specified columns
    for i in options:
        if i == transaction_type:
            a.append(1)
        else:
            a.append(0)    
    # Submit button
    df = pd.DataFrame([a], columns=columns)
    print(df)
    s = sc.transform(df)
    df1 = pd.DataFrame(s, columns=columns)
    print(df1.head())
    predict = st.form_submit_button('predict')

# Prediction and result display
if predict:
    t = model.predict(df1)
    print(t)
    if t:
        col2.title('Fraud Detected')
    else:
        col2.title('Safe Transaction')
