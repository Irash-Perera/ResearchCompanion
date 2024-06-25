import streamlit as st
import time
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

def generate_output(query, llm, embeddings):
    with st.spinner("Analyzing data..."):
        # load the vectorstore
        vectorstore = Chroma(persist_directory="vectorstore", embedding_function=embeddings)
        time.sleep(2)
    with st.spinner("Generating answer..."): 
        template = """You are a helpful AI. Answer based on the provided context.Be friendly. Strictly search for the answer in the provided context. 
                        context: {context}
                        input: {input}
                        answer:
                        """ 
                        
        # define the chains 
        retriever = vectorstore.as_retriever()
        prompt = PromptTemplate.from_template(template)
        combined_docs_chain = create_stuff_documents_chain(llm, prompt)
        retrieval_chain = create_retrieval_chain (retriever, combined_docs_chain)
        
        result = retrieval_chain.invoke({"input": query})
        
        # chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=retriever)
        # result = chain({"question": query}, return_only_outputs=True)
        # print(result)

    if result["answer"]:
        st.header("Answer")
        st.write(result["answer"])
        st.subheader("Source")
        st.write(result["context"][0].metadata["source"])
        # st.subheader("Source")
        # st.write(result["source"])