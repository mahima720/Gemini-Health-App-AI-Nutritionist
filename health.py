import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

load_dotenv()

# Initialize the GenAI Client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to get response from Gemini
def get_gemini_repsonse(input_text, image, user_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[input_text, image, user_prompt]
    )
    return response.text

## Initialize our Streamlit app
st.set_page_config(page_title="Gemini Health App")

st.header("Gemini Health App")
user_input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", width="stretch")

submit = st.button("Tell me the total calories")

input_prompt = """
You are an expert nutritionist. Look at the food items in the image
and calculate the total calories. Provide details for every food item 
with its calorie count in the following format:

1. Item 1 - no of calories
2. Item 2 - no of calories
----
----
Finally, summarize whether the meal is healthy or not.
"""

## If submit button is clicked
if submit:
    if uploaded_file is not None:
        with st.spinner("Analyzing image..."):
            response = get_gemini_repsonse(input_prompt, image, user_input)
            st.subheader("The Analysis Result:")
            st.write(response)
    else:
        st.warning("Please upload an image first!")