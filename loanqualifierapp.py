# loanqualifier.py
# This program get input from user and determin accetance or rejection of a loan application
import streamlit as st
st.title("Chad's Awesome Loan Qualifier")
# Set minimum salary and year or work
MINSALARY = 40000
MINYEAR = 5
# Get input from user about salary and year
SALARY = float(st.number_input("Please enter your annual salary: "))
YEAR = int(st.number_input("Please enter your year of work: "))
# Determine whether the loan application is accepted or jected
if st.button("SUBMIT"):
    if SALARY > MINSALARY and YEAR > MINYEAR:
        st.write("Congratulation, your application has accepted")
    else:
        st.write("Sorry, your application has rejected")
else:
    st.write("Please enter your information")