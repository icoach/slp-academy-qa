import faiss
import pickle
from langchain.chat_models import ChatOpenAI
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain.prompts.prompt import PromptTemplate

def setup():
    # Load vector database for similarity search
    index = faiss.read_index("docs.index")
    with open("faiss_store.pkl", "rb") as f:
        vectorstore = pickle.load(f)
    vectorstore.index = index

    # Create prompts for OpenAI chat completion API - use just openai package
    document_prompt = PromptTemplate(input_variables=['page_content', 'source'], output_parser=None, partial_variables={}, template='Content: {page_content}\nSource: {source}', template_format='f-string', validate_template=True)
    question_prompt = PromptTemplate(input_variables=['context', 'question'], output_parser=None, partial_variables={}, template='Use the following portion of a long document to see if any of the text is relevant to answer the question. \nReturn any relevant text verbatim.\n{context}\nQuestion: {question}\n\nRelevant text, if any:', template_format='f-string', validate_template=True)
    combine_prompt = PromptTemplate(input_variables=['summaries', 'question'], output_parser=None, partial_variables={}, template='You are senior support specialist for solidpixels (the name is always lowecase and spelled together). Your task is to answer user\'s questions about solidpixels SaaS application functionality. Given the following extracted parts of a long document and a question, create a final answer with references ("SOURCES"). \nYour primary source of information are given document, but you can use general knowledge to formulate answer. If you don\'t know the answer, just say that you don\'t know. Don\'t try to make up an answer. Formulate the answer in Czech. \nALWAYS return a "SOURCES" part in your answer.\n\nQUESTION: {question}\n=========\n{summaries}\n=========\nFINAL ANSWER:', template_format='f-string', validate_template=True)

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = RetrievalQAWithSourcesChain.from_llm(llm,document_prompt, question_prompt, combine_prompt, retriever=vectorstore.as_retriever(), verbose=True)

    return chain

def query(chain, question):
    return chain({"question": question})