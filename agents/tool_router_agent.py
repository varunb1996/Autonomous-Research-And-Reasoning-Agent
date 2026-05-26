from tools.llm_tool import run_llm


def tool_router_agent(task):

    prompt = f"""
    Decide which tools are required.

    Available tools:
    - web search
    - memory retrieval
    - pdf parser
    - browser tool
    - code execution

    Task:
    {task}
    """

    return run_llm(prompt)