from sklearn.linear_model import LinearRegression
import pickle
import streamlit as st
import pandas as pd
import numpy as np
 
# loading the trained model
pickle_in = open('SPO2Model.pkl', 'rb') 
regressor = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(HeartRate):   
 
    # Making predictions 
    prediction = regressor.predict(np.array([HeartRate]).reshape(-1,1))
     

    return prediction
      
  # this is the main function in which we define our webpage  

def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:white;padding:13px"> 
    <h1 style ="color:black;text-align:center;">SPO2 Level ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    HeartRate = st.number_input("Heart Rate")
    result = 0
    final_result = ""


      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(HeartRate) 
        if result[0][0] > 100:
            final_result = "Your blood oxygen saturation level is: 100%"
        elif result[0][0] < 95:
            final_result = "Your blood oxygen saturation level is: 95%"
        else:
            final_result = "Your blood oxygen saturation level is: " + str(result[0][0]) + "%"
            
        if HeartRate < 60:
            final_result = "Consider re-recording heart rate"
            
        st.success(final_result)
        print(HeartRate)
    
    
if __name__=='__main__': 
    main()
    
