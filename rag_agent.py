from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# Setup
Settings.llm = Ollama(model="deepseek-r1:1.5b", num_gpu=50)
Settings.embed_model = OllamaEmbedding(model_name="deepseek-r1:1.5b")

# Load knowledge base
print("Loading PDFs...")
documents = SimpleDirectoryReader("data").load_data()
agent = VectorStoreIndex.from_documents(documents).as_query_engine()

# Your custom prompt system
def ask_agent(question, role="assistant"):
    prompt = f"""You are a helpful {role}. Answer based on the documents.
    Context: From the uploaded PDFs
    Question: {question}
    Answer concisely and accurately:"""
    return agent.query(prompt)

# Use it!
while True:
    user_input = input("\nYou: ")
    if user_input == "quit":
        break
    response = ask_agent(user_input, "expert assistant")
    print(f"Agent: {response}")