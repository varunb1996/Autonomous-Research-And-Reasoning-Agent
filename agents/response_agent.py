from tools.llm_tool import run_llm


def response_agent(goal, research, critique):

    prompt = f"""
    Create a final high-quality response.

    Goal:
    {goal}

    Research:
    {research}

    Critique:
    {critique}
    """

    return run_llm(prompt)