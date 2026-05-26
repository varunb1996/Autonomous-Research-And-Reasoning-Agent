from tools.llm_tool import run_llm


def supervisor_agent(goal):

    prompt = f"""
    You are a supervisor AI agent.

    Decide:
    - which agents should execute
    - execution order
    - retry logic
    - required tools

    Goal:
    {goal}
    """

    return run_llm(prompt)