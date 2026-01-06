import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("sree Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

prompt = st.chat_input("Say something...")

if prompt:
    st.session_state.chat.append(("user", prompt))

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    st.session_state.chat.append(("assistant", response.text))

for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.write(msg)
