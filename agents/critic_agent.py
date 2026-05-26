from tools.llm_tool import run_llm


def critic_agent(answer):

    prompt = f"""
    Critique the following answer.

    Identify:
    - Missing information
    - Weak reasoning
    - Areas for improvement

    Answer:
    {answer}
    """

    return run_llm(prompt)