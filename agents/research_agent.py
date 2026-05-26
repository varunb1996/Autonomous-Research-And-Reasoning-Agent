from tools.search_tool import search_web


def research_agent(query):

    results = search_web(query)

    formatted = ""

    for r in results:

        formatted += f"\nTitle: {r['title']}\n"
        formatted += f"Content: {r['content']}\n"

    return formatted