from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def vectore_DB(chunks):
    embedding_model = HuggingFaceEmbeddings(
        model_name = "all-miniLM-L6-v2"
    )

    texts = [c.page_content for c in chunks]
    db = Chroma(
        collection_name="rag_store",
        embedding_model = embedding_model
    )
    db.add_texts(texts)

    return db.as_retriever(search_kwargs={"k" : 3})
