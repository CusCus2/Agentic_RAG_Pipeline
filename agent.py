def agent_controller(query):
    q = query.lower()
    search_keywords = [
        "pdf", "document", "data", "summarize", "information",
        "find", "according to", "based on", "what does the file say"
    ]
    if any(word in q for word in search_keywords):
        return {
            "action" : "search",
            "reason" : "The query appears to require information from the uploaded documents."
        }
    return {
        "action" : "direct",
        "reason" : "The query can likely be answered without document retrieval."
    }

