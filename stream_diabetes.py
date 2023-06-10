import pickle
import streamlit as st

# membaca model
model_diabetes = pickle.load(open('model_diabetes.sav', 'rb'))

#judul web
st.title('Klasifikasi Diabetes')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ('Nilai Pregnancies')

with col1 :
    Glucose = st.text_input ('Nilai Glucose')

with col1 :
    BloodPressure = st.text_input ('Nilai Blood Pressure')

with col1 :
    SkinThickness = st.text_input ('Nilai Skin Thickness')

with col2 :
    Insulin = st.text_input ('Nilai Insulin')

with col2 :
    BMI = st.text_input ('Nilai BMI')

with col2 :
    DiabetesPedigreeFunction = st.text_input ('Nilai Diabetes Pedigree Function')

with col2 :
    Age = st.text_input ('Nilai Age')

# code untuk prediksi
diagnosis_diab = ''

# membuat tombol untuk prediksi
if st.button('Cek Hasil'):
    clas_diabetes = model_diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(clas_diabetes[0] == 1):
        diagnosis_diab = 'Pasien terkena Diabetes'
    else:
        diagnosis_diab = 'Pasien tidak terkena Diabetes'
st.success(diagnosis_diab)