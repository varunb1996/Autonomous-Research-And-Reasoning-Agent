from tools.llm_tool import run_llm


def reasoning_agent(context):

    prompt = f"""
    Perform deep reasoning.

    Analyze:
    - hidden insights
    - inconsistencies
    - assumptions
    - opportunities

    Context:
    {context}
    """

    return run_llm(prompt)