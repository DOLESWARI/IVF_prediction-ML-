import streamlit as st
from PIL import Image
import io
def calculate_fertility(age_female, age_male, bmi_female, bmi_male, ivf_attempts):
    # Perform fertility calculation based on input parameters
    # This is just a placeholder function, you would replace this with your actual calculation logic
    fertility_score = age_female + age_male + bmi_female + bmi_male + ivf_attempts
    return fertility_score


def assess_fertility_score(score,ivf_attempts):
    # Define threshold values for classifying fertility score
    good_threshold = 50
    bad_threshold = 30

    # Assess fertility score
    if score >= good_threshold  and ivf_attempts<=4:
        return "Good"
    elif score >= bad_threshold and ivf_attempts >4  and ivf_attempts<=9:
        return "Fair"
    else:
        return "Poor"



def image_build():
    image_bytes = open('dna1.jpg', 'rb').read()
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, use_column_width=True)

def run():
    image_build()
    # Page title and description
    st.title('IVF Fertility Calculator')
    st.write('This tool calculates the fertility score of couples undergoing in vitro fertilization (IVF).')

    # Input fields
    age_female = st.slider('Female Age', min_value=18, max_value=50, value=30, step=1)
    age_male = st.slider('Male Age', min_value=20, max_value=60, value=35, step=1)
    bmi_female = st.number_input('Female BMI', min_value=10.0, max_value=50.0, value=25.0, step=0.1)
    bmi_male = st.number_input('Male BMI', min_value=10.0, max_value=50.0, value=25.0, step=0.1)
    ivf_attempts = st.number_input('Number of IVF Attempts', min_value=1, value=1)

    # Calculate fertility score
    if st.button('Calculate Fertility'):
        fertility_score = calculate_fertility(age_female, age_male, bmi_female, bmi_male, ivf_attempts)
        st.success(f'Fertility Score: {fertility_score}')
        fertility_assessment = assess_fertility_score(fertility_score,ivf_attempts)
        st.success(f'Fertility Score: {fertility_score} ({fertility_assessment})')
    # Additional information or instructions
    st.write('The fertility score is calculated based on the input parameters. '
             'The higher the score, the better the predicted fertility outcome.')
    # Disclaimer or note
    st.write('Note: This tool provides an estimate only and should not replace medical advice.')
    return None