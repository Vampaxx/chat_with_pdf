import os
from dotenv import load_dotenv
from langchain.llms import GooglePalm
from langchain.llms import OpenAI
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma



from src.chat_with_pdf.utils.common import get_pdf_file

import streamlit as st 


def main():
    st.set_page_config(page_title="Chat with multiple PDFs",page_icon="🧊")
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a Question about the Documents")




    with st.sidebar:
        st.subheader("Your documents")
        pdf_files = st.file_uploader("Upload your PDF and Press 'Process'",accept_multiple_files=True)

        if st.button("Process"):
            st.spinner("Processing...")
            pdf_text = get_pdf_file(pdf_files)
            st.write(pdf_text)
            # get the pdf file
            # get the pdf chunks
            # create vector store

        add_radio = st.radio(
            "Choose file format",
            ("PDF", "JPEG"))
        
        add_selectbox = st.sidebar.selectbox(
            "How would you like to be contacted?",
            ("Email", "Home phone", "Mobile phone"))
        

    



if __name__ == "__main__":
    main()

