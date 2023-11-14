# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/asus/OneDrive/Desktop/Multiple Disease Prediction System/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/asus/OneDrive/Desktop/Multiple Disease Prediction System/saved models/heart_disease_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',],
                          icons=['activity','heart'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex,0 for Male and 1 for Female')
        
    with col3:
        cp = st.number_input('Chest Pain types: 0=Angina; 1=Asymtomatic; 2=Abnormal')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure,[Domain:94-200]')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl,[Domain:126-564]')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar,[Domain:0,1]')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results: 0=Normal; 1=Abnormal; 2=Hyper')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved,[Domain:72-202]')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina,[Domain:0,1]')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise,[Domain:0-6.2]')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment: 0=Up; 1=Flat; 2=Down')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy,[Domain:0,1,2,3]')
        
    with col1:
        thal = st.number_input('thal: 0 = Normal; 1 = Fixed defect; 2 = Reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

          


