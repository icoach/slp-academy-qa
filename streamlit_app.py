import streamlit as st
import os
import faiss
import pickle

from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI


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


# App title
st.set_page_config(page_title="Akademický chatbot")

# Sidebar for additional info and actions
with st.sidebar:
    st.title("Akademický chatbot")

    if 'OPENAI_API_KEY' in st.secrets:
        st.success('API klíč je v pořádku', icon='✅')
        openai_api = st.secrets['OPENAI_API_KEY']
    else:
        openai_api = st.text_input('Zadej OpenAI API klíč:', type='password')
        if not (openai_api.startswith('sk')):
            st.warning('Prosím zadej API klíč pro velký mozek', icon='👉')
        else:
            st.warning('Jdi do toho, ptej se', icon='👉')

    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=1.0, value=0.2, step=0.01)
    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.1, step=0.01)
    # max_length = st.sidebar.slider('max_length', min_value=64, max_value=4096, value=512, step=8)
    
    st.markdown('📖 TODO: more infor how to use this prototype')

os.environ['OPENAI_API_KEY'] = openai_api

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Jak ti můžu dneska pomoct?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Jak ti můžu dneska pomoct?"}]
st.sidebar.button('Vymazat historii chatu', on_click=clear_chat_history)

# Function for generating LLM response
def generate_response(prompt_input):
    string_dialogue = "Jsi nápomocný pracovník podpory pro webovou aplikaci. Neodpovídáš jako 'Uživatel' ani se nesnažíš předstírat, že jsi 'Uživatel'. Pouze odpovídáš jednou odpovědí jako 'Asistent'."
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "Uživatel: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Asistent: " + dict_message["content"] + "\n\n"
    
    # Load the LangChain.
    index = faiss.read_index("docs.index")

    with open("faiss_store.pkl", "rb") as f:
        store = pickle.load(f)

    store.index = index

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=temperature, top_p=top_p)
    chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever(), verbose=True)
    o = chain({"query": prompt_input})

    output = []
    output.append(o['result'])
    # output.append(o['sources'])
    
    return output

# User-provided prompt
if prompt := st.chat_input(disabled=not openai_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Pracuju na tom..."):
            response = generate_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)