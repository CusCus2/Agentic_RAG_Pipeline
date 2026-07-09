import os
import logging
import time
import get_data as gd
import chunking as ck
import Embedding_VectoreStore as ev
import model as md
import agent as ag

def build_rag_system():
    folder_path = "files/"

    docs = gd.load_docs(folder_path)
    print("PDF pages loaded: ", len(docs))

    chunk = ck.chunks(docs)
    print("chunks Created: ", len(chunk))

    retriever = ev.vectore_DB(chunk)
    
    llm = md.model()

    return {
        "retriever" : retriever,
        "llm" : llm
    }



def answer_query(query, retriever, llm):

    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename = "logs/raq_queries.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    start = time.perf_counter()
    
    decision = ag.agent_controller(query)

    action = decision["action"]
    sources = []

    if action == "search":
        print("Agent decided to SEARCH doc for : ", query)
        print("Reason : ", decision["reason"])
        results = retriever.invoke(query)
        context = "\n".join(
            [
                f"Source: {r.metadata.get('source', 'unknown')}, "
                f"Page: {r.metadata.get('page', 'None')}\n"
                f"{r.page_content}" 
                for r in results
            ]
        )

        sources = [
            {
               "source" : r.metadata.get('source', 'unknown'),
               "page" : r.metadata.get('page', 'None'),  
            }
            for r in results
        ]

        final_prompt = f"""
        You are a helpful assistant.
        Answer only using the context below.
        If the answer is not present in the context, say "I don't know.

        Context:
        {context}

        Question:
        {query}

        Answer:
        """
    else:
        print("Agent decided to answer DIRECTLY: ", query)
        final_prompt = query
    
    # response = llm(final_prompt)[0]["generated_text"] # this was for the google flan model
    response = llm.invoke(final_prompt).content
    latency = time.perf_counter() - start

    logging.info(
        f"query='{query}' | action='{action}' | chunks={len(results) if action == "search" else 0} | latency={latency:.2f}s"
    )

    return {
        "query" : query,
        "action" : action,
        "answer" : response,
        "sources" : sources
    }