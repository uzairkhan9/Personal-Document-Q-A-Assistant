import streamlit as st
from ingest import ingest_pdf
from qa import get_qa_chain

st.title("📄 Chat with your PDF")

uploaded = st.file_uploader("Upload a PDF", type="pdf")
if uploaded:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded.read())
    ingest_pdf("temp.pdf")
    st.success("PDF ingested!")

query = st.text_input("Ask a question:")
if query:
    chain = get_qa_chain()
    result = chain.invoke(query)
    st.write(result["result"])
    with st.expander("Sources"):
        for doc in result["source_documents"]:
            st.write(f"Page {doc.metadata['page']}: {doc.page_content[:200]}...")
