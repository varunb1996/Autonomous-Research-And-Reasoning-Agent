from tools.llm_tool import run_llm


def planner_agent(user_goal):

    prompt = f"""
    You are a planning agent.

    Break the following goal into smaller tasks.

    Goal:
    {user_goal}
    """

    return run_llm(prompt)