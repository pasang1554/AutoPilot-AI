import streamlit as st
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.critic import CriticAgent
from memory.memory_store import MemoryStore

st.set_page_config(page_title="AutoPilot AI", layout="wide")
st.title("🚀 AutoPilot AI (Advanced)")

goal = st.text_area("🎯 Enter your goal")

MAX_RETRIES = 3

if st.button("Run AutoPilot"):
    memory = MemoryStore()
    planner = PlannerAgent()
    executor = ExecutorAgent(memory)
    critic = CriticAgent()

    plan = planner.plan(goal)
    st.subheader("🧠 Task Plan")
    st.code(plan)

    for attempt in range(1, MAX_RETRIES + 1):
        st.subheader(f"⚙️ Execution Attempt {attempt}")
        execution = executor.execute(plan)
        st.code(execution)

        review = critic.review(execution)
        st.subheader("🔍 Critic Review")
        st.code(review)

        if '"approved": true' in review.lower():
            st.success("✅ Approved by Critic")
            break
        else:
            st.warning("❌ Critic requested improvement")

    st.subheader("📌 Final Output")
    st.code(execution)
