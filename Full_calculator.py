import streamlit as st

st.title("Calculator")
st.subheader("Mini calculator")

a=st.number_input("Enter First Number:",min_value=0)
b=st.number_input("Enter Second Number:",min_value=0)
is_clicked=st.button("calculate",type='primary',use_container_width=True)  


operations=st.selectbox("select operation",
                        ["Addition","Substraction","Multiplication","Division"])


if is_clicked:

    if operations == "Addition":
        result = a+b

    elif operations == "Substraction":
        result = a-b

    elif operations == "Multiplication":
        result = a*b

    elif operations == "Division":
        if b != 0:
            result = a/b
        else:
            result = "cannot divide by zero"


    st.success(f"Result: {result}")

 