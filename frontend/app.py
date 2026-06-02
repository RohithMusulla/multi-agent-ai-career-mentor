import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Career Mentor",
    layout="wide"
)

st.title("🚀 Multi-Agent AI Career Mentor")

st.sidebar.title("Navigation")

option = st.sidebar.radio(
    "Choose Feature",
    [
        "Resume Analysis",
        "Career Chat",
        "Multi-Agent Analysis"
    ]
)

# ==========================================
# Resume Analysis
# ==========================================

if option == "Resume Analysis":

    st.header("📄 Resume Upload & Skill Analysis")

    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    target_role = st.text_input(
        "Target Role",
        "Data Scientist"
    )

    if st.button("Analyze Resume"):

        if uploaded_file is not None:

            files = {
                "file": uploaded_file
            }

            response = requests.post(
                f"{API_URL}/upload-resume",
                files=files,
                params={
                    "target_role": target_role
                }
            )

            result = response.json()

            st.success("Resume Analyzed Successfully")

            st.subheader("Detected Skills")
            st.write(result["detected_skills"])

            st.subheader("Skill Gap Analysis")
            st.json(result["skill_gap_analysis"])

            st.subheader("Resume Preview")
            st.write(result["resume_preview"][:2000])

# ==========================================
# Career Chat
# ==========================================

elif option == "Career Chat":

    st.header("💬 AI Career Chat")

    question = st.text_input(
        "Ask Career Question"
    )

    if st.button("Ask AI"):

        response = requests.get(
            f"{API_URL}/career-chat",
            params={
                "question": question
            }
        )

        result = response.json()

        st.success("Answer Generated")

        st.write(result)

# ==========================================
# Multi-Agent Analysis
# ==========================================

elif option == "Multi-Agent Analysis":

    st.header("🧠 Multi-Agent Career Analysis")

    if st.button("Run Multi-Agent System"):

        response = requests.post(
            f"{API_URL}/multi-agent-analysis"
        )

        result = response.json()

        st.success("Multi-Agent Analysis Completed")

        st.write(result["multi_agent_result"])