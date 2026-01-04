import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY")
)

# UI
st.set_page_config(page_title="Vishnu LLM", page_icon="🤖")
st.write("Ask your queries")

# User input
user_prompt = st.text_area("Enter your prompt:", height=150)

# Button
if st.button("Generate Response"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Generating response..."):
            response = llm.invoke(user_prompt)
            st.success("Response:")
            st.write(response.content)


