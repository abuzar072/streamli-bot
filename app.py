
import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load env variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="AIExambot",
    page_icon="🤖",
    layout="centered"
)

# Groq client
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))
client = Groq(api_key="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")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 AbuzarCustomGPT")

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    try:
        # Groq API call
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=300
        )

        assistant_reply = response.choices[0].message.content

        # Show assistant message
        with st.chat_message("assistant"):
            st.markdown(assistant_reply)

        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_reply}
        )

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
