from flask import Flask, render_template, request, jsonify
import os
import sys
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.vectorstores import Chroma
from langchain.document_loaders.csv_loader import CSVLoader

app = Flask(__name__)

# Set the API key
os.environ["OPENAI_API_KEY"] = "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"

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False

# Initialize the chain and index
chain = None
index = None

def initialize_chain_and_index():
    global chain, index
    if PERSIST and os.path.exists("persist"):
        print("Reusing index...\n")
        vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
        index = VectorStoreIndexWrapper(vectorstore=vectorstore)
    else:
        loader = TextLoader("data/data.txt")  # Use this line if you only need data.txt
        csv_loader = CSVLoader(file_path='data/projects.csv')
        if PERSIST:
            index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory": "persist"}).from_loaders([loader, csv_loader])
        else:
            index = VectorstoreIndexCreator().from_loaders([loader, csv_loader])

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

initialize_chain_and_index()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global chain, index
    query = request.form.get('prompt', '')
    if query.lower() in ['quit', 'q', 'exit']:
        sys.exit()
    else:
        result = chain({"question": query, "chat_history": []})
        response = result['answer']
        return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
