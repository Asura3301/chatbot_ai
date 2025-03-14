"""
helper functions
"""

from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings


# Extract text from PDFs using langchain
def load_pdf_file(data):
    loader = DirectoryLoader(data,
                             glob="*.pdf",
                             loader_cls=PyPDFLoader)

    documents = loader.load()
    
    return documents

# Split the text into chunks 
chunk_size = 256
chunk_overlap = 64
def text_split(extracted_text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                   chunk_overlap=chunk_overlap)
    text_chunks = text_splitter.split_documents(extracted_text)
    return text_chunks

    
# Download the embeddings from Hugging Face
embed_model = "sentence-transformers/all-MiniLM-L6-v2"
# model_kwargs = {"device": "cuda"}  - need to fix this  
def download_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name=embed_model)
    return embeddings