import os
import get_data as gd
import chunking as ck
import Embedding_VectoreStore as ev
import model as md
import agent as ag

def main():
    folder_path = "files/"


    docs = gd.load_docs(folder_path)
    print("PDF pages loaded: ", len(docs))

    chunk = ck.chunks(docs)
    print("chunks Created: ", len(chunk))

    retriever = ev.vector_DB(chunk)
    
    llm = md.model()

    query = input("enter a question or type 'exit' to close prompt : ")
    
    action = ag.agent_controller(query)

    if action == "search":
        print("Agent decided to SEARCH doc for : ", query)
        results = retriever.invoke(query)
        context = "\n".join([r.page_content for r in results])
        final_prompt = f"Use this context:\n{context}\n\nAnswer:\n{query}"
    else:
        print("Agent decided to answer DIRECTLY: ", query)
        final_prompt = query
    
    response = llm(final_prompt)[0]["generated_text"]
    print(response)
    print("-" * 20)

if __name__ == "__main__":
    main()