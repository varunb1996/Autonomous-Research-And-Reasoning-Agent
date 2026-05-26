from agents.reflection_agent import reflection_agent
from agents.reasoning_agent import reasoning_agent



def autonomous_retry_loop(initial_response):

    current_response = initial_response

    for _ in range(1):

        reflection = reflection_agent(
            current_response
        )

        improved = reasoning_agent(
            reflection
        )

        current_response = improved

    return current_response