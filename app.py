import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

pickle_in = open("LR_model.pkl","rb")
classifier=pickle.load(pickle_in)

def predict_BookindCheckedIn(LodgingRevenue,RoomNights,DaysSinceLastStay,DaysSinceFirstStay):
    
    """Let's Predict if customer check-in to hotel after booking or not 
    This is using docstrings for specifications.
    ---
    parameters:  
      - LodgingRevenue
      - RoomNights
      - DaysSinceLastStay
      - DaysSinceFirstStay
        
    """
   
    prediction=classifier.predict([[LodgingRevenue,RoomNights,DaysSinceLastStay,DaysSinceFirstStay]])
    print(prediction)
    return prediction

def main():
    st.title("Customer Check-In Prediction System")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Predictor API</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    LodgingRevenue = st.text_input("LodgingRevenue","Type Here")
    RoomNights = st.text_input("RoomNights","Type Here")
    DaysSinceLastStay = st.text_input("DaysSinceLastStay","Type Here")
    DaysSinceFirstStay = st.text_input("DaysSinceFirstStay","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_BookindCheckedIn(LodgingRevenue,RoomNights,DaysSinceLastStay,DaysSinceFirstStay)
    st.success('Customer Check-In : {}'.format(result))
    if st.button("Explain Output"):
        st.text("[0] : Customer will not check-in")
        st.text("[1] : Customer will check-in")

if __name__=='__main__':
    main()
    