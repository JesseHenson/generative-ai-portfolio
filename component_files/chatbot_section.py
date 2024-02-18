import streamlit as st
from constant import *
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader


def create_chatbot_section():
    openai_api_key = st.text_input('Enter your OpenAI API Key and hit Enter to chat.')

    if openai_api_key.startswith('sk-'):
        st.session_state.openai_api_key = openai_api_key


    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def load_files():
        loader = TextLoader("./bio.txt")
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(openai_api_key=st.session_state.openai_api_key))
        return vectorstore

    def create_rag_chain(vectorstore):
        retriever = vectorstore.as_retriever()
        prompt = hub.pull("rlm/rag-prompt")
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=st.session_state.openai_api_key)
        st.session_state.rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

    def ask_bot(input_text):
        response = st.session_state.rag_chain.invoke(input_text)
        return response
        
    if 'openai_api_key' in st.session_state:
        input_text = st.text_input("After providing OpenAI API Key on the sidebar, you can send your questions and hit Enter to know more about me from my AI agent, Buddy!", key="input")
        if 'rag_chain' not in st.session_state:
            vectorstore = load_files()
            create_rag_chain(vectorstore)
        if input_text is not None and input_text is not "":
            st.info(ask_bot(input_text))