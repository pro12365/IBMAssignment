import os
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

# Set API key for OpenAI Service
os.environ['OPENAI_API_KEY'] = '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'
llm = OpenAI(temperature=0.1, verbose=True)
embeddings = OpenAIEmbeddings()

# Function to parse PDF file and extract negotiation data
def parse_pdf(filename):
    loader = PyPDFLoader(filename)
    pages = loader.load_and_split()
    return pages

# Function to preprocess negotiation data
def preprocess_negotiation_data(negotiation_data):
    # Preprocessing steps as needed
    return negotiation_data

# Parse PDF to extract negotiation data
negotiation_data = parse_pdf('Negotiationdata.pdf')
negotiation_data = preprocess_negotiation_data(negotiation_data)

# Create vector store from negotiation data
store = Chroma.from_documents(negotiation_data, embeddings, collection_name='negotiation_data')
vectorstore_info = VectorStoreInfo(
    name="negotiation_data",
    description="Negotiation conversation data from PDF",
    vectorstore=store
)
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

# Create agent executor
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

# Streamlit app
st.set_page_config(page_title="Negotiation Engine", page_icon="💬")

st.title("💬 Negotiation Engine")
st.write(
    "Welcome to the Negotiation Engine prototype. This tool can assist you in simulating negotiation scenarios. "
    "Enter your negotiation query in the text box below and click the 'Search' button to generate a response."
)

prompt = st.text_input('Enter your negotiation query here:')
prompt_history = st.session_state.get("prompt_history", [])
search_button = st.button("Search", key="search_button", help="Click to search")

if search_button:
    response = agent_executor.run(prompt)
    st.write("Response:", response)
    prompt_history.insert(0, prompt)
    st.session_state.prompt_history = prompt_history

st.sidebar.title("Prompt History")

for i, history_prompt in enumerate(prompt_history, 1):
    st.sidebar.write(f"{i}. {history_prompt}")
