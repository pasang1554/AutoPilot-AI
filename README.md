# 🚀 AutoPilot AI

**Task-Oriented LLM Agent for Autonomous Problem Solving**

AutoPilot AI is a fully local, production-ready multi-agent AI system built using
LangChain and the FREE Groq API.

---

## 🧠 How It Works

1. **Planner Agent**
   - Breaks the user goal into numbered steps

2. **Executor Agent**
   - Executes tasks step-by-step
   - Uses local tools (calculator, file writer, logger)

3. **Critic Agent**
   - Reviews correctness, logic, and completeness
   - Suggests improvements

4. **Memory Module**
   - Stores intermediate reasoning and context

---

## 🖥️ How to Run

```bash
git clone <repo>
cd AutoPilot-AI
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
