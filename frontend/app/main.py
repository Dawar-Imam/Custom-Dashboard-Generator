"""
Streamlit application entry point.
Initializes and runs the Streamlit frontend application with page configuration.
"""
import streamlit as st
from services.api_client import ask_llm

# Page configuration
st.set_page_config(
    page_title="Runtime UI Generator",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Title and description
st.title("🚀 AI Runtime Dashboard Generator")
st.markdown("Generate custom homepage for your product!")

# Input section
question = st.text_input(
    "Describe the dashboard you want:",
    placeholder="e.g., Design a colorful homepage for a homemade food items...",
    help="Be descriptive about the design, functionality, and requirements",
)

# Generate button
if st.button("Generate", type="primary", use_container_width=True):
    if question.strip():
        with st.spinner("🔄 Generating your webpage..."):
            try:
                response = ask_llm(question)
                st.success(response.get("answer", "Webpage generated successfully!"))
                st.info("✅ Your generated webpage has been opened in your browser!")
            except Exception as e:
                st.error(f"❌ Error generating webpage: {str(e)}")
    else:
        st.warning("⚠️ Please enter a description for your webpage!")