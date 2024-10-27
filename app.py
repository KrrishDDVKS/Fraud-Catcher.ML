import streamlit as st
import pickle
import pandas as pd
st.title('Fraud Catcher.ML 🦹‍♂')

with open('data_f.pkl', 'rb') as file:
    model = pickle.load(file)

col1,col2 = st.columns([1,2])
col1.title('Result: Fraud')
a=[]

with st.form('detection'):
    options = ["PAYMENT", "CASH_OUT", "TRANSFER","DEBIT","‘CASH_IN"]
    a.append(float(st.text_input('Amount','10.38')))
    a.append(float(st.text_input('Originating old Balance','122.8')))
    a.append(float(st.text_input('Originating new Balance','1001')))
    a.append(float(st.text_input('Destintion old Balance','0.1184')))
    a.append(float(st.text_input('Destintion new Balance','0.2776')))
    a.append(st.selectbox("Choose an option:", options))
    df=pd.DataFrame(a,columns=['amount','oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest','isFraud','type'])
    df1 = pd.get_dummies(df1, columns=['type'])
    predict=st.form_submit_button('predict')

if predict:
        t=model.predict(df1)
        df1=[]
        if t:
            col2.title('Breast Cancer Diagnoised')
            st.audio("witch.mp3", format="audio/mpeg",autoplay=True)
        else:
            col2.title('Safe')
