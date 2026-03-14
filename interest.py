
import streamlit as st

st.title("Simple Interest Calculator")
st.subheader("Loan")

p = st.number_input("Enter Principal Amount")
r = st.number_input("Enter Interest Rate")
t = st.number_input("Enter Time (Years)")

if st.button("Calculate Interest"):
    interest = (p * r * t) / 100
    st.success(f"Simple Interest = {interest}")
