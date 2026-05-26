from tools.llm_tool import run_llm


def reflection_agent(answer):

    prompt = f"""
    Reflect on the following output.

    Evaluate:
    - accuracy
    - completeness
    - weaknesses
    - improvements

    Output:
    {answer}
    """

    return run_llm(prompt)