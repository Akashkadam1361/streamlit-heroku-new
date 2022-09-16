import streamlit as st

st.header("Addition of 2 given numbers")

number1 = st.number_input('Insert first number',value=0) 

number2 = st.number_input('Insert second number',value=0)

if number1 is not None and number2 is not None:
    st.write("Sum of the numbers is: {}".format((number1+number2)))
    st.write("Subtraction of the numbers is: {}".format((number1-number2)))
    st.write("multiplication of the numbers is: {}".format((number1*number2)))
if number2 != 0:
    st.write("division of the numbers is: {}".format((number1/number2)))

