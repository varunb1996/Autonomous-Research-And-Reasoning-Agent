import streamlit as st

from workflows.agent_graph import (
    run_agentic_system
)

st.set_page_config(
    page_title="Cognitive Autonomous Multi-Agent AI",
    layout="wide"
)

st.title(
    "🧠 Cognitive Autonomous Multi-Agent Intelligence System"
)

st.markdown("""
This platform includes:

- Supervisor agents
- Research agents
- Reflection loops
- Autonomous retries
- Vector memory
- Web search
- Multi-agent reasoning
""")

query = st.text_area(
    "Enter your goal"
)

if st.button("Run Autonomous Agents"):

    with st.spinner(
        "Agents are reasoning autonomously..."
    ):

        result = run_agentic_system(query)

    st.header("🧠 Supervisor")
    st.write(result["supervisor"])

    st.header("📋 Planning")
    st.write(result["plan"])

    st.header("🧠 Retrieved Memories")
    st.write(result["memories"])

    st.header("🌐 Research")
    st.write(result["research"])

    st.header("🧐 Reasoning")
    st.write(result["reasoning"])

    st.header("🔍 Critique")
    st.write(result["critique"])

    st.header("🪞 Reflection")
    st.write(result["reflection"])

    st.header("✅ Final Autonomous Response")
    st.write(result["final_response"])