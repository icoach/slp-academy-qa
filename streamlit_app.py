import streamlit as st
import os
import faiss
import pickle

from langchain.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
# from langchain.chains import ConversationalRetrievalQAChain
from langchain.chat_models import ChatOpenAI
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
# from langchain.memory import ConversationBufferMemory
# from langchain.callbacks.base import BaseCallbackHandler
# from langchain.schema import HumanMessage

# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

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

# class StreamHandler(BaseCallbackHandler):
#     def __init__(self, container, initial_text="", display_method='markdown'):
#         self.container = container
#         self.text = initial_text
#         self.display_method = display_method

#     def on_llm_new_token(self, token: str, **kwargs) -> None:
#         self.text += token + "/"
#         display_function = getattr(self.container, self.display_method, None)
#         if display_function is not None:
#             display_function(self.text)
#         else:
#             raise ValueError(f"Invalid display_method: {self.display_method}")


# def get_chat_history(inputs) -> str:
#     res = []
#     for human, ai in inputs:
#         res.append(f"Human:{human}\nAI:{ai}")
#     return "\n".join(res)

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
    # top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.1, step=0.01)
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

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=temperature)
    chain = RetrievalQAWithSourcesChain.from_chain_type(llm,retriever=store.as_retriever(), chain_type="stuff", return_source_documents=True, verbose=True)
    o = chain({"question": prompt_input})

    output = []
    output.append(o['answer'] + o['sources'])
    
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
            # stream_handler = StreamHandler(placeholder, display_method='write')
            full_response = ''
            response = generate_response(prompt)

            # llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=temperature, streaming=True)
            # question_generator = LLMChain(llm=llm, prompt=prompt_input)
            # chain = ConversationalRetrievalChain.from_llm(llm,retriever=store.as_retriever(), callbacks=[stream_handler], question_generator=question_generator, memory=memory, verbose=True)
            
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)