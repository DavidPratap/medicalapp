import streamlit as st
import pandas as pd
import pickle
st.title("The Medical Diagnostic App")
st.subheader("Does this Woman have the Outcome?")
# load the pickled model
# open the model for deployment
model=open('rfc.pickle', 'rb')
rfc_pickle=pickle.load(model)
model.close()

# prepare UI for front end user input
pregs=st.slider('Pregnancies',0, 20, step=1)
glucose=st.slider('Glucose',40, 200, 0)
bp=st.slider('BloodPressure',20, 140, 20)
skin=st.slider('SkinThickness',7.00, 99.00, 7.00)
insulin=st.slider('Insulin',10, 900, 10)
bmi=st.slider('BMI', 15, 70, 15)
dpf=st.slider('DiabetesPedigreeFunction',0.5, 3.0, 0.5)
age=st.slider('Age', 21, 90, 21)

#  prepare the user input for feeding in the model to get predictions
data={'Pregnancies':pregs,
      'Glucose':glucose, 
      'BloodPressure':bp, 
      'SkinThickness':skin, 
      'Insulin':insulin,
       'BMI': bmi,
      'DiabetesPedigreeFunction':dpf,
      'Age':age
}

input_data=pd.DataFrame([data])


# get the predictions and output the results
predictions=rfc_pickle.predict(input_data)[0]
st.subheader(predictions)
if st.button("Predict"):
    if predictions==1:
        st.write("Has the disease")
    if predictions==0:
        st.write("Disease Free")