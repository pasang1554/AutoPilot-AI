import streamlit as st
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.critic import CriticAgent
from memory.memory_store import MemoryStore

st.set_page_config(page_title="AutoPilot AI", layout="wide")

st.title("🚀 AutoPilot AI")
st.subheader("Task-Oriented LLM Agent for Autonomous Problem Solving")

goal = st.text_area("🎯 Enter your goal")

if st.button("Run AutoPilot"):
    memory = MemoryStore()

    planner = PlannerAgent()
    executor = ExecutorAgent(memory)
    critic = CriticAgent()

    with st.spinner("Planning..."):
        plan = planner.plan(goal)
        memory.add("planner", plan)

    with st.spinner("Executing..."):
        execution = executor.execute(plan)

    with st.spinner("Reviewing..."):
        review = critic.review(execution)

    st.success("Completed")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧠 Task Plan")
        st.code(plan)

        st.markdown("### ⚙️ Execution")
        st.code(execution)

    with col2:
        st.markdown("### 🔍 Critic Review")
        st.code(review)

        st.markdown("### ✅ Final Output")
        st.code(execution + "\n\nCritic Notes:\n" + review)
