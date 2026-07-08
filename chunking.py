from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunks(docs):
    text_splitter =RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 80,
    )
    return text_splitter.split_documents(docs)