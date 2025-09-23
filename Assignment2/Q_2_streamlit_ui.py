import streamlit as st
import pickle

with open("Engine_model.pkl","rb") as file:
    model=pickle.load(file)

st.header("Engine Price Predction")

engin_size=st.text_input("ENGINESIZE")
cylinders=st.text_input("CYLINDERS")
fuelconsumption_comp=st.text_input("FUELCONSUMPTION_COMB")

predict_button=st.button("Predict Engine Price")

if predict_button:
    engin_size=float(engin_size)
    cylinders=float(cylinders)
    fuelconsumption_comp=float(fuelconsumption_comp)

    price=model.predict([[engin_size,cylinders,fuelconsumption_comp]])
    st.text(f"Price=${price[0]:.2f}")