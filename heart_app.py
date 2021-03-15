import streamlit as st
import base64
import sklearn
import numpy as np
import pickle as pkl
from sklearn.preprocessing import MinMaxScaler
scal=MinMaxScaler()
#Load the saved model
model=pkl.load(open("cad_model.p","rb"))








st.set_page_config(page_title="Coronary Heart disease diagnosis App",page_icon="⚕️",layout="centered",initial_sidebar_state="expanded")



def preprocess(gender, hypertension, diabete, smokecurrent, hpgrade,chestpain, rccach, max_ccach, max_ccacl, ps ):   
 
    
    # Pre-processing user input   
    if gender=="male":
        gender=1 
    else: gender=0
    
    
    if chestpain=="Typical angina":
        chestpain=3
    elif chestpain=="Atypical angina":
        chestpain=2
    elif chestpain=="Non-anginal pain":
        chestpain=1
    elif chestpain=="Asymptomatic":
        chestpain=0
    
    if hypertension=="Yes":
        hypertension=1
    elif hypertension=="No":
        hypertension=0
        
    if hpgrade=="level 3":
        hpgrade=3
    elif hpgrade=="level 2":
        hpgrade=2
    elif hpgrade=="level 1":
        hpgrade=1
    elif hpgrade=="prehypertension":
        hpgrade=0.5
    elif hpgrade=="normal":
        hpgrade=0
        
    if diabete=="Yes":
        diabete=1
    elif diabete=="No":
        diabete=0
 
    if smokecurrent=="Yes":
        smokecurrent=1
    elif smokecurrent=="No":
        smokecurrent=0



    user_input=[gender, hypertension, diabete, smokecurrent, hpgrade,chestpain, rccach, max_ccach, max_ccacl, ps]
    user_input=np.array(user_input)
    user_input=user_input.reshape(1,-1)
    user_input=scal.fit_transform(user_input)
    prediction = model.predict(user_input)

    return prediction

    

       
    # front end elements of the web page 
html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Coronary Heart disease diagnosis App</h1> 
    </div> 
    """
      
# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True) 
st.subheader('by Bao xin ')


# following lines create boxes in which user can enter data required to make prediction

gender = st.radio("Select Gender: ", ('male', 'female'))
chestpain = st.selectbox('Chest Pain Type',("Typical angina","Atypical angina","Non-anginal pain","Asymptomatic")) 
hypertension=st.selectbox('hypertension',['Yes','No'])
hpgrade = st.selectbox('hygrade',("level 3","level 2","level 1","prehypertension","normal")) 
diabete=st.selectbox('diabete',['Yes','No'])
smokecurrent=st.selectbox('smokecurrent',['Yes','No'])
max_ccach=st.number_input('The maximum double carotid plaque height')
max_ccacl=st.number_input('The maximum double carotid plaque length')
rccach=st.number_input('right carotid plaque height')
ps=st.number_input('The addition of double carotid plaque height')



#user_input=preprocess(sex,cp,exang, fbs, slope, thal )
pred=preprocess(gender, hypertension, diabete, smokecurrent, hpgrade,chestpain, rccach, max_ccach, max_ccacl, ps)




if st.button("Predict"):    
  if pred[0] == 0:
    st.error('Warning! You have high risk of getting a heart attack!')
    
  else:
    st.success('You have lower risk of getting a heart disease!')
    
   



st.sidebar.subheader("About App")

st.sidebar.info("This web app is helps you to find out whether you are at a risk of a coronary heart disease.")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check whether you have a heart disease")
st.sidebar.info("Don't forget to rate this app")



feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=5,step=1)

if feedback:
  st.header("Thank you for rating the app!")
  st.info("Caution: This is just a prediction and not doctoral advice. Kindly see a doctor if you feel the symptoms persist.") 


    
    
    
    
    
    
    
    
