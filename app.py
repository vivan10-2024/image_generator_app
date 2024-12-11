import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit app UI
st.title("Image Generator App")
st.subheader("Generate stunning images with AI")

# Input from user
prompt = st.text_input("Enter a prompt for the image:")
image_size = st.selectbox(
    "Select image size:",
    ["256x256", "512x512", "1024x1024"]
)

if st.button("Generate Image"):
    if prompt.strip():
        st.write("Generating image... Please wait.")
        try:
            # Call OpenAI DALL·E API
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size=image_size
            )
            image_url = response['data'][0]['url']

            # Display the generated image
            st.image(image_url, caption="Generated Image", use_column_width=True)
            st.write(f"[Download Image]({image_url})")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Prompt cannot be empty. Please enter a description.")


