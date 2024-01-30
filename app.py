import os
import streamlit as st 
from dotenv import load_dotenv
from langchain.llms import GooglePalm
from src.chat_with_pdf.utils.common import *
from langchain.prompts import SemanticSimilarityExampleSelector

def main():
    st.set_page_config(page_title="Chat with multiple PDFs",page_icon="🧊")

    st.header("Chat with multiple PDFs :books:")
    user_question = st.text_input("Ask a Question about the Documents")
    
    if user_question:
        respose = st.session_state.conversation({'question':user_question})
        st.write(respose['answer'])


    
    with st.sidebar:
        st.subheader("Your documents")
        pdf_files = st.file_uploader("Upload your PDF and Press 'Process'",accept_multiple_files=True)

        if st.button("Process"):
            st.spinner("Processing...")
            # get the pdf file
            pdf_text = get_pdf_file(pdf_files)
            # get the pdf chunks
            text_chunks = get_text_chunks(pdf_text)
            # create vector store
            vector = get_vectorstore(text_chunks=text_chunks)
            # conversation,
            st.session_state.conversation = conversation_chain(vectorstore=vector)
            #st.write(st.session_state.conversation)


if __name__ == "__main__":
    main()