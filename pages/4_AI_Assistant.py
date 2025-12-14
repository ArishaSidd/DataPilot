import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

st.set_page_config(page_title="DataPilot - AI Assistant")

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

st.title("🤖 AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.session_state.get("chat_mode") == "code_explanation":
    user_input = f"Explain this Python code:\n\n{st.session_state.get('code_to_explain')}"
    st.session_state.chat_mode = None
    st.session_state.code_to_explain = None
else:
    user_input = st.chat_input("Ask your question...")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response_holder = st.empty()
        collected_response = ""

        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[{"role": "user", "content": user_input}],
            stream=True,
        )
        for chunk in completion:
            if chunk.choices[0].delta.content:
                collected_response += chunk.choices[0].delta.content
                response_holder.markdown(collected_response)

        st.session_state.messages.append({"role": "assistant", "content": collected_response})
