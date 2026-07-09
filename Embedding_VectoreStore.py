from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def vectore_DB(chunks):
    embedding_model = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-miniLM-L6-v2"
    )

    texts = [c.page_content for c in chunks]
    db = Chroma.from_documents(
        documents = chunks,
        collection_name="rag_store",
        embedding = embedding_model
    )
    db.add_texts(texts)

    return db.as_retriever(search_kwargs={"k" : 3})
