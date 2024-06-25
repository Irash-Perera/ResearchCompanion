import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
import time

def create_vectordb(urls, embeddings):
    with st.status("Searching data...", expanded=True) as status:
        #load data
        status.update(label="Loading data...",state="running", expanded=False)
        loader = WebBaseLoader(urls)
        data = loader.load()
        
        # print(data)
        #split data
        status.update(label="Crunching data into chunks...",state="running", expanded=False)
        r_splitter = RecursiveCharacterTextSplitter(
            separators= [ ".", "," ],
            chunk_size= 2000)
        docs = r_splitter.split_documents(data)
        # print(docs)

        #create embeddings
        status.update(label="Creating embeddings...",state="running", expanded=False)
        vectordb = Chroma.from_documents(docs, embeddings, persist_directory="vectorstore")
        
        # print(embeddings)
    
        time.sleep(2)
        vectordb.persist()
        vectordb = None
        status.update(label="Data saved successfully! Ready to answer!",state="complete", expanded=False)
        time.sleep(2)