# Personal-Document-Q-A-Assistant
Working on a Personal Document Q&amp;A Assistant that uses LangChain and RAG pipelines and then feeds to LLM, thereby reducing hallucinations

PDF → split into chunks → embed chunks → store in ChromaDB
User question → embed question → similarity search → top-k chunks → LLM → answer + sources
