import streamlit as st
import os
import faiss
import pickle

from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.prompt import PromptTemplate

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

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
    presence_penalty = st.sidebar.slider('presence_penalty', min_value=0.0, max_value=1.0, value=0.0, step=0.1)

    strategy = st.radio("Jakou použít strategii pro vyhledání obsahu", ('RetrievalQAWithSourcesChain', 'RetrievalQA', 'ConversationalRetrievalChain'))
    indexMethod = st.radio("Advanced: Metoda pro volání LLM", ('Stuffing', 'Map-Rerank', 'Map-Reduce', 'Refine'))

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
    # Load the LangChain.
    index = faiss.read_index("docs.index")

    with open("faiss_store.pkl", "rb") as f:
        store = pickle.load(f)

    store.index = index

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=temperature, model_kwargs={"presence_penalty": presence_penalty})
    
    output = []

    if indexMethod == "Stuffing":
        chain_type="stuff"
    elif indexMethod == "Map-Reduce":
        chain_type="map_reduce"
    elif indexMethod == "Map-Rerank":
        chain_type="map_rerank"
    elif indexMethod == "Refine":
        chain_type="refine"

    # context = "Jsi zkušený zdvořilý a velmi nápomocný pracovník podpory pro webovou aplikaci. Tvým úkolem je odpovídat na dotazy uživatelů aplikace."
    
    if strategy == "RetrievalQA":
        chain = RetrievalQA.from_llm(llm,retriever=store.as_retriever(), verbose=True)
        o = chain({"query": prompt_input})
        output.append(o['result'])

    elif strategy == "ConversationalRetrievalChain":
        chain = ConversationalRetrievalChain.from_llm(llm,retriever=store.as_retriever(), chain_type=chain_type, memory=memory, verbose=True)
        o = chain({"question": prompt_input + " Odpovídej pouze v češtině."})
        output.append(o['answer'])

    else:
        chain = RetrievalQAWithSourcesChain.from_llm(llm,retriever=store.as_retriever(), verbose=True)
        document_prompt = PromptTemplate(input_variables=['page_content', 'source'], output_parser=None, partial_variables={}, template='Content: {page_content}\nSource: {source}', template_format='f-string', validate_template=True)
        question_prompt = PromptTemplate(input_variables=['context', 'question'], output_parser=None, partial_variables={}, template='Use the following portion of a long document to see if any of the text is relevant to answer the question. \nReturn any relevant text verbatim. Use only provided document parts to formulate the answer.\n{context}\nQuestion: {question}\nRelevant text, if any:', template_format='f-string', validate_template=True)
        combine_prompt = PromptTemplate(input_variables=['summaries', 'question'], output_parser=None, partial_variables={}, template='You are senior support specialist for solidpixels (the name is always lowecase and spelled together). Your task is to answer user\'s questions about solidpixels SaaS application functionality. Given the following extracted parts of a long document and a question, create a final answer with references ("SOURCES"). \nIf you don\'t know the answer, just say that you don\'t know. Don\'t try to make up an answer. Formulate the answer in Czech. \nALWAYS return a "SOURCES" part in your answer.\n\nQUESTION: {question}\n=========\n{summaries}\n=========\nFINAL ANSWER:', template_format='f-string', validate_template=True)

        chain = RetrievalQAWithSourcesChain.from_llm(llm,document_prompt, question_prompt, combine_prompt, retriever=store.as_retriever())        # chain = RetrievalQAWithSourcesChain.from_chain_type(llm,retriever=store.as_retriever(), chain_type=chain_type, verbose=True)
        o = chain({"question": prompt_input})
        output.append(o['answer'] + "\n\n" + o['sources'])
    
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
            placeholder = st.empty()
            full_response = ''
            response = generate_response(prompt)

            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)