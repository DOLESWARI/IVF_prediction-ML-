import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import io
from sklearn.linear_model import LinearRegression


def run():
    image_build()
    st.title("Female Fertility Prediction")
    formCreation()

    #return None
def formCreation():
    st.write("Please fill the details")
    with st.form(key="Registration Form"):
        age = st.text_input('Enter your Age')
        fsh = st.text_input('Enter Follicular Stimulating Hormone Level')
        lh = st.text_input('Enter Lutenizing Hormone Level')
        estra = st.text_input('Enter Estradiol Level')
        oq = st.text_input('Enter Ova Quality Level   [note: High: 3, Normal: 2, Low: 1]')
        oc = st.text_input('Enter Ova Count Level')
        om = st.text_input('Enter Ova Maturity Level')
        #of = st.text_input('Enter Ova Fertilization Level')
        #oi = st.text_input('Enter Ova Implantation Level')
        submit = st.form_submit_button(label="Submit")

        if submit== True:
            if age =="" or fsh=="" or  lh=="" or estra=="" or oq == "" or oc == "" or om == ""  :
                st.error("Fill in All Details")
                return
            st.success("Thankyou for the Details")
            #pr = st.form_submit_button(label="Show Prediction")
        #if st.form_submit_button():
            # Perform your prediction or other operations here
            user_input = [age, fsh, lh, estra, oq, oc, om]
            #st.write("User Input:", user_input[0],user_input[1],user_input[2],user_input[3],user_input[4],user_input[5],user_input[6],user_input[7],user_input[8])
            user_input1 = [float(x) for x in user_input]
            print(user_input1)
            # Load the pre-trained model
            ffp_model = pickle.load(open('Ovum_fertility.sav', 'rb'))
            f_prediction = ffp_model.predict([user_input])
            print(f_prediction)
            if (f_prediction[0] == 0):
                st.write("Ovum can't be fertile")
            else:
                st.write("Ovum can be fertile")



#def model():

def image_build():
    image_bytes = open('ivf1.jpg', 'rb').read()
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, use_column_width=True)