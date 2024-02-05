import os
from dotenv import load_dotenv
load_dotenv()
from langchain.llms import OpenAI
import streamlit as st

#streamlit framework
st.set_page_config(page_title="OpenAI Basic LLM")
st.title("Basic Search Demo!")
input_text = st.text_input("Search the topic we want!")

#OPENAI LLMS
llm = OpenAI(temperature=0.9, openai_api_key=os.getenv("OPENAI_API_KEY"))

if input_text:
    st.write(llm(input_text))