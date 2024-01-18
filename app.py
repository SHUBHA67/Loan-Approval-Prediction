import pickle
import streamlit as st
import numpy as np
import pandas as pd


model =  pickle.load(open('ML_Model.pkl', 'rb'))

def main():
    html_temp="""
    <div style = "background-color:light-blue;padding;16px">
    <h1 styple = "color:black;text-align:center;">Loan approval Prediction</h2>
    </div>
"""
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.write(' ')

    st.write(' ')

    s1 = st.selectbox("Please Select Gender",('Male','Female'))  #Male =1 Female =0
    if s1 == 'Male':
        p1 = 1
    else:
        p1 =2
    s2 = st.selectbox("Whether you are Married or not ?",('Yes','No')) #No = 1 Yes = 0
    if s2 == 'No':
        p2 =1
    else:
        p2 =0
    s3 = st.selectbox("Select No. of Dependents ?",('0','1','2','3+')) # 0 = 0 ,1=1,2=2,3+=3
    if s3 == "0":
        p3 = 0
    elif s3 == "1":
        p3 = 1
    elif s3 == "2":
        p3 = 2
    elif s3 =="3+":
        p3 = 3
    s4 = st.selectbox("Select Eduaction whether you are Graduate or not ?",('Graduate','NotGraduate')) # G =0 ,N.G =1
    if s4 == "Graduate":
        p4 = 0
    else:
        p4 = 1
    s5 = st.selectbox("Select whether you are Self Employed or not ?",('Yes','No')) # no =0 ,yes =1
    if s5 == "No":
        p5 = 0
    elif s5 == "Yes":
        p5 = 1
    p6 = st.number_input("Enter Applicant's Income ")

    p7 = st.number_input("Enter Co-Applicants's Income ")

    p8 = st.number_input("Enter Loan Amount (in lakhs)")

    p9 = st.number_input("Enter Loan Amount Term (days) ")

    s10 = st.selectbox("Select Credit History",('1.0','0.0')) # 1= 1 0=0
    if s10 =="0.0":
        p10 = 0
    elif s10 =="1.0":
        p10 = 1
    s11 =st.selectbox("Select the Property Area ",('Urban','Semi-Urban','Rural')) # U = 2 R = 0 S=1
    if s11 == "Urban":
        p11 = 2
    elif s11 == "Rural":
        p11 = 0
    else :
        p11 = 1



    if st.button('Predict'):
        X = ([[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]])
        prediction = model.predict(X)
        if prediction[0] == 1:
            st.balloons()
            st.success("Your Loan will be approved")
        elif prediction[0] == 0:
            st.write("Your Loan wil not be approved")
main()
