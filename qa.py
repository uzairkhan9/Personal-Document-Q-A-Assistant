from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

def get_qa_chain():
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
        return_source_documents=True
    )
    return chain
