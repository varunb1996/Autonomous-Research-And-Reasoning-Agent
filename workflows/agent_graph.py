from agents.supervisor_agent import (
    supervisor_agent
)

from agents.planner_agent import (
    planner_agent
)

from agents.research_agent import (
    research_agent
)

from agents.reasoning_agent import (
    reasoning_agent
)

from agents.critic_agent import (
    critic_agent
)

from agents.reflection_agent import (
    reflection_agent
)

from agents.response_agent import (
    response_agent
)

from tools.memory_tool import (
    save_memory,
    search_memory
)

from tools.logging_tool import (
    log_event
)

from workflows.autonomous_loop import (
    autonomous_retry_loop
)


def run_agentic_system(user_goal):

    log_event("System execution started")

    # Supervisor
    supervisor_output = supervisor_agent(
        user_goal
    )

    log_event("Supervisor completed")

    # Planning
    plan = planner_agent(user_goal)

    log_event("Planner completed")

    # Memory Retrieval
    memories = search_memory(user_goal)

    log_event("Memory retrieval completed")

    # Research
    research = research_agent(user_goal)

    log_event("Research completed")

    # Reasoning
    reasoning = reasoning_agent(
        research
    )

    log_event("Reasoning completed")

    # Critique
    critique = critic_agent(
        reasoning
    )

    log_event("Critique completed")

    # Reflection
    reflection = reflection_agent(
        critique
    )

    log_event("Reflection completed")

    # Final Response
    final_response = response_agent(
        user_goal,
        reasoning,
        reflection
    )

    log_event("Response generation completed")

    # Autonomous Retry Loop
    improved_response = autonomous_retry_loop(
        final_response
    )

    log_event("Autonomous retry loop completed")

    # Save memory
    save_memory(improved_response)

    log_event("Memory stored")

    return {

        "supervisor": supervisor_output,

        "plan": plan,

        "memories": memories,

        "research": research,

        "reasoning": reasoning,

        "critique": critique,

        "reflection": reflection,

        "final_response": improved_response
    }