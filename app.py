import streamlit as st
import os
from google.generativeai import GenerativeModel, configure
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("API Key Gemini tidak ditemukan. Silakan set variabel lingkungan GEMINI_API_KEY atau file .env.")
    st.stop()

configure(api_key=GEMINI_API_KEY)
model = GenerativeModel("gemini-1.5-flash")

# Prompt filter agar hanya menjawab seputar komputer
def filter_prompt(user_input):
    instruction = (
        "Jawab hanya jika pertanyaan berkaitan dengan komputer, teknologi, pemrograman, perangkat keras, perangkat lunak, atau internet. "
        "Jika tidak, tolak dengan sopan dan katakan bahwa chatbot hanya melayani pertanyaan seputar dunia komputer."
    )
    return f"{instruction}\nPertanyaan: {user_input}"

st.title("Chatbot AI Gemini - Dunia Komputer")

user_input = st.text_input("Tanyakan seputar komputer/teknologi:")
if st.button("Tanya") and user_input:
    prompt = filter_prompt(user_input)
    with st.spinner("Memproses..."):
        try:
            response = model.generate_content(prompt)
            st.success(response.text)
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
