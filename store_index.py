"""
-Script to configure, create and store indexes to our 
Pinecone Vector Database.
-Execute only one time, before actually staring app.py
"""

from src.helper import load_pdf_file, text_split, download_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os
import time

#------------------------------------------

# Set env variables
load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

#------------------------------------------

extracted_text = load_pdf_file(data="data/")
text_chunks = text_split(extracted_text=extracted_text)
embeddings = download_embeddings()

#------------------------------------------
# configure pinecone

pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = 'asura'
cloud = os.environ.get('PINECONE_CLOUD') or 'aws'
region = os.environ.get('PINECONE_REGION') or 'us-east-1'

embed_dim = 384 # dimensionality of all-MiniLM-L6-v2
metric = "cosine"

spec = ServerlessSpec(cloud=cloud, region=region)

#------------------------------------------
# check existing indexes
if index_name in pc.list_indexes().names():
    pc.delete_index(index_name)

# we create a new index
pc.create_index(
        index_name,
        dimension=embed_dim,  # dimensionality of all-MiniLM-L6-v2
        metric=metric,
        spec=spec
    )

# wait for index to be initialized
while not pc.describe_index(index_name).status['ready']:
    time.sleep(1)

# wait a moment for connection and check the status of vectorestore
time.sleep(1)
index = pc.Index(index_name)
index.describe_index_stats()

#------------------------------------------
# upload embeddings to pinecone
# Embed each chunk and upsert the embeddings into your Pinecone index
vectorestore_from_docs = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)

# Notification that you done correctly!
print("Creating and storing indexes done correctly!")