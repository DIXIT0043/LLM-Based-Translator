
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser # responsible for displaying the output
load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

model = ChatGroq(model='Gemma2-9b-It',groq_api_key = groq_api_key)
from langchain_core.messages import HumanMessage,SystemMessage

parser = StrOutputParser()

genric_template = "Translate the following into {language}:"

prompt = ChatPromptTemplate.from_messages(

    [('system',genric_template),('user','{text}')]

)
chain = prompt|model|parser


# App Definition

st.title('LLM Based Translator')

text = st.text_area('Enter The Text you want to Translate')
language = st.text_input('Enter the Language')

if st.button('Translate'):
    if text and language:
        with st.spinner('Translating...'):
            try:
                translation = chain.invoke({'text':text,'language': language})
                st.subheader('Translation')
                st.write(translation)
            except Exception as obj:
                st.write('Error {obj}')
    else:
        st.write('⚠️ Please provide both text and language')
else:
    st.write('⚠️ Please Write both text and language')
