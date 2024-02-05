import streamlit as st
import os
from langchain.schema import HumanMessage, SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

st.set_page_config(page_title="Conversational QA chatbot")
st.header("Lets Chat!")

chatllm = ChatOpenAI(temperature=0.9, openai_api_key=openai_api_key)

if 'flow_messages' not in st.session_state:
    st.session_state['flow_messages'] = [SystemMessage(content="Act as an comedian AI assistant")
    ]

def get_openai_response(question):
    st.session_state['flow_messages'].append(HumanMessage(content=question))
    answer = chatllm(st.session_state['flow_messages'])
    st.session_state['flow_messages'].append(AIMessage(content=answer.content))
    return answer.content


input = st.text_input("Input: ", key="input")
response = get_openai_response(input)

submit = st.button("Ask Me!")

if submit:
    st.subheader("The response is:")
    st.write(response)