import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import io
def run():
    image_bytes = open('dna2.jpg', 'rb').read()
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, use_column_width=True)

    st.title("Home Page")
    st.write("Welcome to the home page!")

    st.write("Welcome to our IVF information portal. Here, you can find resources and tools related to IVF.")
    st.write("This is the home page. Choose a section from the sidebar to explore more.")
    st.header("IVF Process")
    st.write("The IVF process involves several steps, including ovarian stimulation, egg retrieval, fertilization, embryo transfer, and pregnancy testing.")
    st.write("We can provide detailed prediction about the fertility possibility of the male and female gamates in the IVF process.")
    return None