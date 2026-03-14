import streamlit as st

st.title("Temperature Converter")

temp=st.number_input('Enter Temperature')
is_clicked=st.button("Convert")
option=st.selectbox("Convert to", 
                    ["Celsius to Fahrenheit","Fahrenheit to Celsius"])

if is_clicked:
    if option == "Celsius to Fahrenheit":
        result = (temp * 9/5)+32

    elif option == "Fahrenheit to Celsius":
        result = (temp-32)*5/9


    st.success(f"Converted To{result}")
    