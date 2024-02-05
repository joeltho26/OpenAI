import os
from dotenv import  load_dotenv
load_dotenv()
from langchain.llms import OpenAI

import streamlit as st

openai_api_key = os.getenv('OPENAI_API_KEY')
huggingface_api_key = os.getenv('HUGGINGFACE_API_KEY')

def get_openai_response(question):
    llm = OpenAI(temperature=0.9,openai_api_key=openai_api_key, model='davinci-002')
    response =  llm(question)
    return response

st.set_page_config(page_title="Q & A Demo")
st.header("Langchain Application")

input = st.text_input("Input: ", key="input")
response = get_openai_response(input)

submit = st.button("Ask Me!")

if submit:
    st.subheader("The response is:")
    st.write(response)