import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import time
from PIL import Image
import io

import ffp
import mfp
import idp
import home
import cf
import si
import li

st.balloons()
# time.sleep(20)

st.title("IVF Prediction System And Genetical Inherited Diseases Prediction")

# Initialize authenticate in session state
if 'authenticate' not in st.session_state:
    st.session_state.authenticate = 0

def show_authentication_menu():
    with st.sidebar:
        selected = option_menu('Genetic Wellness',
                               ['Sign_In', 'Log_in'],
                               menu_icon='hospital-fill',
                               icons=['person-circle', 'person-check'],
                               default_index=0)

    if selected == 'Sign_In':
        a = si.run()
        if a == 1:
            st.session_state.authenticate = 1
            st.rerun()  # Rerun to update the sidebar

    elif selected == 'Log_in':
        b = li.run()
        if b == 1:
            st.session_state.authenticate = 1
            st.rerun()  # Rerun to update the sidebar

def show_main_menu():
    with st.sidebar:
        selected = option_menu('Genetic Wellness',
                               ['Home', 'Female Fertility Prediction',
                                'Male Fertility Prediction', 'Composite Fertility Score',
                                'Inherited Diseases Prediction'],
                               menu_icon='hospital-fill',
                               icons=['house', 'person-standing-dress', 'person-standing', 'activity', 'people-fill'],
                               default_index=0)

    if selected == 'Home':
        home.run()

    elif selected == 'Female Fertility Prediction':
        ffp.run()

    elif selected == 'Male Fertility Prediction':
        mfp.run()

    elif selected == 'Composite Fertility Score':
        cf.run()

    elif selected == 'Inherited Diseases Prediction':
        idp.run()
        st.subheader('Select Inherited Diseases Type')
        sub_selected = st.radio("Genetical Diseases", ['HaemophiliaA', 'HaemophiliaB', 'DuchenneMuscularDystropy(DMH)',
                                                       'FragileXSyndrome', 'RettSyndrome', 'X-LinkedLchthyosis',
                                                       'X-LinkedHypophosphatemia', 'X-LinkedRetinitisPigmentosa',
                                                       'X-LinkedAdrenoleukodystrophy(X-ALD)'])

# Display the appropriate menu based on authentication state
if st.session_state.authenticate == 1:
    show_main_menu()
else:
    show_authentication_menu()
    if st.session_state.authenticate != 1:
        st.warning("At first, sign in or log in")
