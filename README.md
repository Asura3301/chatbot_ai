# Chatbot_AI
Personal Projects | Chatbot specialized in the topic of artificial intelligence


**ChatBot that specialized in the fields of artificial intelligence, machine learning, deep learning and algorithms.**
This project is an advanced conversational agent that leverages state-of-the-art technologies in AI, machine learning, deep learning, and data engineering. It integrates LangChain with Pinecone for efficient vector data management, utilizes HuggingFace embedding models for robust semantic representation, and employs the Groq Cloud API with the Llama-3-8B-Instruct model for high-performance language processing. The result is a chatbot enhanced by retrieval augmented generation (RAG), ideal for autonomous agents and intelligent systems.

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/Asura3301/chatbot_ai
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n chatbotai python=3.12 -y
```

```bash
conda activate chatbotai
```
or if you have ```CondaError: Run 'conda init' before 'conda activate'```

```bash
source activate chatbotai
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GROQ_API_KEY     = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 3 Model:

meta-llama/Meta-Llama-3-8B-Instruct


## From the following link:
https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
```

```bash
# run the following command
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```

### Techstack Used:

- Python
- LangChain
- Flask
- Meta Llama3
- Pinecone
- Groq