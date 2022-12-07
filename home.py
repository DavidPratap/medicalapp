import streamlit as st
import pandas as pd
st.title("The Home Page")
st.subheader("Preparing the data and Viewing it for the Web Application")

data=pd.read_csv('data.csv')
# drop the Unnamed column 
data.drop("Unnamed: 0", axis=1, inplace=True)
# impute zero errors
zerofiller=lambda x: x.replace(0, x.median())
cols=data.columns[1:6]
data[cols]=data[cols].apply(zerofiller, axis=0)
df=data.copy()
d={"Yes":1, "No":0}
df["Outcome"]=df["Outcome"].map(d)

st.write(df.head())
st.write(df.describe().T)