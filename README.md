# Chatbot_AI
Personal Projects | Chatbot specialized in the topic of artificial intelligence


**ChatBot that specialized in the fields of artificial intelligence, machine learning, deep learning and algorithms.**

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
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
```


### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
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
- Meta Llama2
- Pinecone