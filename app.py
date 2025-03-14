from flask import Flask, render_template, jsonify, request
from src.helper import download_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
# from store_index import index_name
from src.prompt import *
import os

# init Flask 
app = Flask(__name__)

#------------------------------------
# setup Groq and Pinecone env

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

#------------------------------------
# configuration for vectorestore 

# init embed object 
embeddings = download_embeddings()
index_name = "asura"
search_type = "similarity"
search_kwargs={"k":3}

#------------------------------------

# load vector indexes from Pinecone database
vectorestore_from_docs = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = vectorestore_from_docs.as_retriever(
    search_type=search_type, 
    search_kwargs=search_kwargs,
    )

#------------------------------------
# configuration for llm

llm_model = "llama3-8b-8192"
max_tokens = 512
temperature = 0.4

#------------------------------------
llm = ChatGroq(
    temperature=temperature, 
    model_name=llm_model, 
    max_tokens=max_tokens
    )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# creating default route
@app.route("/")
def index():
    return render_template("index.html")

# creating route for chat operation 
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)