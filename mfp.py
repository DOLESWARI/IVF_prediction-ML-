import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import io
import pickle

def run():
    image_build()
    st.title("Male Fertility Prediction")
    formCreation()

    #return None

def image_build():
    image_bytes = open('ivf2.jpg', 'rb').read()
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, use_column_width=True)


def formCreation():
    st.write("Please fill the details")
    with st.form(key="Registration Form"):
        age = st.text_input('Enter your Age')
        sc = st.text_input('Enter Sperm count')
        mv = st.text_input('Enter Motility Value')
        v = st.text_input('Enter Volume')
        c = st.text_input('Enter Sperm Concentration')
        submit = st.form_submit_button(label="Submit")

        if submit== True:
            if age =="" or sc=="" or  mv=="" or v=="" or c == "":
                st.error("Fill in All Details")
                return
            st.success("Thankyou for the Details")
            #pr = st.form_submit_button(label="Show Prediction")
        #if st.form_submit_button():
            # Perform your prediction or other operations here
            user_input = [age, sc, mv, v, c]
            #st.write("User Input:", user_input[0],user_input[1],user_input[2],user_input[3],user_input[4],user_input[5],user_input[6],user_input[7],user_input[8])
            user_input1 = [float(x) for x in user_input]
            print(user_input1)
            # Load the pre-trained model
            ffp_model = pickle.load(open('Sperm_fertility.sav', 'rb'))
            f_prediction = ffp_model.predict([user_input])
            print(f_prediction)
            if (f_prediction[0] == 0):
                st.write("Sperm can't be fertile")
            else:
                st.write("Sperm can be fertile")