import streamlit as st

with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)
st.logo("hsma_logo.png")

st.title("Welcome to the Clinic Simulation App")

st.write("This app uses discrete event simulation to model a GP clinic. "
         "Please go to the Clinic Simulation page to test out " 
         "different scenarios")