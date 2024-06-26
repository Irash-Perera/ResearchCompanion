import os 
import streamlit as st

from create_vectordb import create_vectordb
from generate_output import generate_output 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import GoogleGenerativeAI

from env import API_KEY
os.environ['GOOGLE_API_KEY'] = API_KEY

def model_flexibility():
    return st.sidebar.slider("How creative should the AI be?", 0.1, 1.0, 0.7)
                
st. set_page_config(layout="wide") 


st.sidebar.title("Your Research Companion")
st.sidebar.image("assets/image.png", use_column_width=True)
temp = model_flexibility()
st.header("Your Research Companion 🕵🏻")

urls = []
with st.sidebar:
    url_count = st.number_input("Number of URLs", 1, 10, 1)
    st.caption("Make sure to hit enter after entering the URL")
    for i in range(url_count):
        urls.append(st.text_input(f"URL {i+1}"))
        
process_button = st.sidebar.button("Process")
st.sidebar.caption("Please make sure to turn on JavaScript and cookies in your browser settings to use this app.")

# llm = ChatGoogleGenerativeAI(model='aqa', temperature=0.7)
llm = GoogleGenerativeAI(model="gemini-pro", temperature= temp)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

if process_button:
    create_vectordb(urls, embeddings)
    
query = st.text_area("Enter your question here")
st.caption("Please provide a question based on the provided context. After entering your question, hit ctrl+enter and then click on Find Answer button.")

if query:
    find_answer = st.button("Find Answer")
    if find_answer:
        if os.path.exists("vectorstore"):
            generate_output(query, llm, embeddings)
        else:
            st.error("Data not loaded! Click on Process button to load data!")
    

