# Chat with Multiple PDF files 

Building an end-to-end Language Model (LLM) project integrating Google Palm and Langchain for interaction with a PDf files,In today's digital age, managing multiple PDFs efficiently is a common necessity for professionals across various fields. Whether you're a student, researcher, or businessperson, effectively organizing, accessing, and manipulating PDF files can significantly enhance productivity and workflow. This short guide aims to provide essential tips and tools for managing multiple PDF documents seamlessly.

1. User Interaction:
Users can interact with the system using natural language queries about PDF file we upload . For example:

    - "Summarize the text"
    

2. Language Understanding:
Utilize the language model (Google Palm) to parse and understand the user's input. Extract key information such as the summarization, about specific topic in the pdf file.


## Installation

1.Clone this repository to your local machine using:

```bash
  git clone https://github.com/Vampaxx/chat_with_pdf.git
```
2.Navigate to the project directory:

```bash
  cd 'project directory'
```
3. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```
4.Acquire an api key through makersuite.google.com and put it in .env file

```bash
  GOOGLE_API_KEY="your_api_key_here"
```
## DEMO WORKING



https://github.com/Vampaxx/chat_with_pdf/assets/124393485/baa7c6bc-99de-447c-ac42-a77a80cf83a0





## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run app.py

```

2.The web app will open in your browser where you can ask questions. It in the localHost
