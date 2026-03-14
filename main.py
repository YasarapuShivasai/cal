import streamlit as st 
st.title("Calculator Application")
a=st.number_input("Enter a Num:")
b=st.number_input("Enter b Num:")
is_clicked=st.button("Add",type='primary',use_container_width=True)

if is_clicked:
    st.write(int(a)+int(b))

    