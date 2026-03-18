import streamlit as st
import requests

st.set_page_config(page_title="AI Assistant", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(145deg, #0a0a0a, #111111);
    color: white;
}

/* Title */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 20px;
    text-shadow: 0px 0px 20px rgba(255,255,255,0.2);
}

/* Chat bubble */
.user {
    background: #ffffff;
    color: black;
    padding: 12px;
    border-radius: 12px;
    margin: 10px 0;
    width: fit-content;
    margin-left: auto;
}

.bot {
    background: rgba(255,255,255,0.05);
    padding: 12px;
    border-radius: 12px;
    margin: 10px 0;
    backdrop-filter: blur(10px);
}

/* Button */
.stButton>button {
    background: linear-gradient(145deg, #ffffff, #cccccc);
    color: black;
    border-radius: 12px;
    height: 50px;
    font-weight: bold;
    box-shadow: 5px 5px 15px #000000, -5px -5px 15px #2a2a2a;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 15px;
    box-shadow: 8px 8px 20px #000000;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="title">🤖 Multi-Agent AI Business Assistant</div>', unsafe_allow_html=True)

# ---------- SESSION MEMORY ----------
if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------- INPUT ----------
query = st.text_input("Enter your task:")

# ---------- BUTTON ----------
if st.button("🚀 Run AI"):

    st.session_state.chat.append(("user", query))

    with st.spinner("Agents are collaborating... 🤖"):

        try:
            response = requests.get(f"http://127.0.0.1:8000/run?query={query}")

            if response.status_code == 200:
                output = response.json()["response"]

                # Fake split (you can later improve backend to split properly)
                planner = "Planning completed"
                executor = "Execution completed"
                analyst = output

                st.session_state.chat.append(("bot", output))

            else:
                st.error("API Error")

        except Exception as e:
            st.error(str(e))

# ---------- CHAT DISPLAY ----------
for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f'<div class="user">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot">{msg}</div>', unsafe_allow_html=True)

# ---------- SPLIT AGENT OUTPUT ----------
st.markdown("## 🧠 Agent Breakdown")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><h4>🧠 Planner</h4><p>Breaks problem into steps</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h4>⚙ Executor</h4><p>Executes tasks</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><h4>📊 Analyst</h4><p>Analyzes final result</p></div>', unsafe_allow_html=True)