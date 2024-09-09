import pickle
import streamlit as st
from PIL import Image
import io

import li


def run():

    image_build()
    submit = st.button(label="Register")
    if submit == True:
        #li.run()
        st.success("Successfully Registered")
        return 1
    else:
        return 0


def image_build():
    image_bytes = open('sign_in.jpg', 'rb').read()
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, use_column_width=True)
