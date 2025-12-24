# 🚀 AutoPilot AI
## 🧠 Task-Oriented LLM Agent for Autonomous Problem Solving

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/LangChain-Agents-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge"/>
</p>

> ✨ **AutoPilot AI** is a self-improving, multi-agent AI system that can  
> **plan tasks**, **execute step-by-step**, **validate results**, and  
> **autonomously refine outputs** — just like a real engineer.

🚫 **Not a chatbot**  
✅ **A real autonomous AI system**  
🧠 **Inspired by real-world software engineering workflows**

---

## 📑 Table of Contents
- [Why AutoPilot AI](#-why-autopilot-ai)
- [How It Works](#-how-it-works)
- [System Architecture](#️-system-architecture)
- [Demo](#-demo)
- [Tool System](#️-tool-system)
- [How to Run](#️-how-to-run)
- [Tech Stack](#️-tech-stack)
- [Project Highlights](#-project-highlights)

---

## ✨ Why AutoPilot AI?

✔ Multi-Agent Architecture  
✔ Autonomous Retry & Self-Improvement  
✔ Strict Tool Hallucination Control  
✔ Scoring-Based Validation  
✔ Structured JSON Outputs  
✔ 100% Free & Local Execution  

🎯 **Designed for final-year projects, interviews, and AI portfolios**

---

## 🧠 How It Works

```text
User Goal
   ↓
Planner Agent
   ↓
Executor Agent
   ↓
Critic Agent
   ↓
Approved? ── No ──▶ Retry
      │
      Yes
      ↓
Final Output
🏗️ System Architecture
<p align="center"> <img src="docs/architecture.png" width="700"/> </p>
🎬 Demo
<p align="center"> <img src="docs/demo.gif" width="700"/> </p>
🛠️ Tool System
🧮 Calculator

📝 File Writer

📋 Task Logger

🔒 Only whitelisted tools allowed
🚫 Unknown tools rejected

🖥️ How to Run
Prerequisites
Python 3.9+

Git

Groq API Key (FREE)

Installation
bash
Copy code
git clone https://github.com/your-username/AutoPilot-AI.git
cd AutoPilot-AI

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Environment Setup
env
Copy code
GROQ_API_KEY=your_groq_api_key_here
Run the App
bash
Copy code
python -m streamlit run app.py
🛠️ Tech Stack
Layer	Technology
Language	Python
LLM	Groq (Free)
Framework	LangChain
UI	Streamlit
Architecture	Multi-Agent

🌟 Project Highlights
🔁 Self-improving retry loop

🧠 Multi-agent orchestration

🚫 Tool hallucination prevention

🎓 Interview-grade project

⭐ Star the repo if you find it useful!
