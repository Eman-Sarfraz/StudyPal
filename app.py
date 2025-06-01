import streamlit as st
from gemini_helper import ask_gemini
from prompts import get_summary_prompt, get_flashcard_prompt, get_tip_prompt
from file_utils import read_txt, read_pdf

# -------- Streamlit Page Config --------
st.set_page_config(
    page_title="StudyPal – AI Study Assistant",
    page_icon="📘",
    layout="wide"
)

# -------- Sidebar --------
with st.sidebar:
    st.image("https://img.icons8.com/color/96/open-book--v2.png", width=80)
    st.title("📚 StudyPal")
    st.markdown("""
Welcome to your AI-powered study buddy!

**Features:**
- Summarize notes
- Generate flashcards
- Get study tips

Built using **Gemini API** and **Streamlit**
""")
    st.markdown("---")
    st.caption("Createdby Eman Sarfraz")

# -------- Header --------
st.markdown("""
    <h1 style="text-align: center; color: #2E86C1;">📘 StudyPal – Your AI Study Assistant</h1>
    <p style="text-align: center; color: gray;">Upload your notes or paste content below</p>
""", unsafe_allow_html=True)

# -------- File Upload --------
uploaded_file = st.file_uploader("📎 Upload Notes (.txt or .pdf)", type=["txt", "pdf"])
text_input = ""

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1]
    try:
        if file_type == "txt":
            text_input = read_txt(uploaded_file)
        elif file_type == "pdf":
            text_input = read_pdf(uploaded_file)
        st.success(f"✅ Loaded `{uploaded_file.name}` successfully!")
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
else:
    text_input = st.text_area("✏️ Or paste your notes here:", height=250)

# -------- Main Action Area --------
if text_input.strip():
    st.markdown("### ✨ Choose an action:")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📌 Generate Summary", use_container_width=True):
            with st.spinner("Summarizing..."):
                summary = ask_gemini(get_summary_prompt(text_input))
                st.markdown("### 📌 Summary")
                st.markdown(f"<div style='background-color:#f0f8ff; padding:15px; border-radius:10px;'>{summary}</div>", unsafe_allow_html=True)

    with col2:
        if st.button("🧾 Generate Flashcards", use_container_width=True):
            with st.spinner("Generating flashcards..."):
                cards = ask_gemini(get_flashcard_prompt(text_input))
                st.markdown("### 🧾 Flashcards")
                st.markdown(f"<div style='background-color:#fffaf0; padding:15px; border-radius:10px;'>{cards}</div>", unsafe_allow_html=True)

    with col3:
        if st.button("💡 Get Study Tips", use_container_width=True):
            with st.spinner("Fetching study tips..."):
                tips = ask_gemini(get_tip_prompt(text_input))
                st.markdown("### 💡 Study Tips")
                st.markdown(f"<div style='background-color:#f5fffa; padding:15px; border-radius:10px;'>{tips}</div>", unsafe_allow_html=True)

# -------- Footer --------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size:14px;'>🔗 Powered by Gemini API | 💻 Built by Streamlit</p>",
    unsafe_allow_html=True
)
