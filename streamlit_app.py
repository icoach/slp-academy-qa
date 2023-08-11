import streamlit as st
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chains import VectorDBQAWithSourcesChain

import faiss-cpu
import pickle



def generate_response(openai_api_key, query_text):
    # Load the LangChain.
    index = faiss.read_index("docs.index")

    with open("faiss_store.pkl", "rb") as f:
        store = pickle.load(f)

    store.index = index
    chain = VectorDBQAWithSourcesChain.from_llm(llm=OpenAI(temperature=0.2), vectorstore=store)
    result = chain({"question": query_text})
    # print(f"{result['answer']}")
    # print()
    # print(f"Zdroje: {result['sources']}")

    return result['answer']
    # # Split documents into chunks
    # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    # texts = text_splitter.create_documents(documents)
    # # Select embeddings
    # embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    # # Create a vectorstore from documents
    # db = Chroma.from_documents(texts, embeddings)
    # # Create retriever interface
    # retriever = db.as_retriever()
    # # Create QA chain
    # qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=openai_api_key), chain_type='stuff', retriever=retriever)
    # return qa.run(query_text)


# Page title
st.set_page_config(page_title='Solidpixels Academie')
st.title('Solidpixels Academie')

# Query text
query_text = st.text_input('Zeptejte se akademie solidpixels:', placeholder = 'Zadejte váš dotaz')

# Form input and query
result = []
with st.form('myform', clear_on_submit=True):
    openai_api_key = st.text_input('OpenAI API Key', type='password', disabled=not query_text)
    submitted = st.form_submit_button('Submit', disabled=not query_text)
    if submitted and openai_api_key.startswith('sk-'):
        with st.spinner('Thinking...'):
            response = generate_response(openai_api_key, query_text)
            result.append(response)
            del openai_api_key

if len(result):
    st.info(response)