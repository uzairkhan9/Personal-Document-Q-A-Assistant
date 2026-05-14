# Personal-Document-Q-A-Assistant
Working on a Personal Document Q&amp;A Assistant that uses LangChain and RAG pipelines and then feeds to LLM, thereby reducing hallucinations.
Basically, I built a RAG pipeline using LangChain that chunks and embeds PDF documents into a ChromaDB vector store, then uses semantic similarity search to retrieve relevant context before passing it to an LLM — so answers are grounded in the actual document rather than hallucinated

PDF → split into chunks → embed chunks → store in ChromaDB
User question → embed question → similarity search → top-k chunks → LLM → answer + sources

How to run:

pip install langchain langchain-openai langchain-community chromadb pypdf streamlit

export OPENAI_API_KEY="your-key"

streamlit run app.py

