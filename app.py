import streamlit as st
from backend import ask_ollama

st.set_page_config(page_title="AI Code Explainer + Bug Fixer (FAST)", layout="wide")

st.title("⚡ AI Code Explainer + Bug Fixer (FAST • Offline)")

# Sidebar
mode = st.radio("Mode:", ["Explain Code", "Fix Bugs"])
language = st.selectbox("Language:", ["Auto", "Python", "C++", "Java", "JavaScript", "C#"])

code = st.text_area("Paste your code here:", height=300)

# ---- OPTIMIZED PROMPTS ----
def build_prompt(mode, lang, code):
    if mode == "Explain Code":
        return (
            f"Explain this {lang} code clearly and briefly.\n"
            f"- Give a 2–3 line summary\n"
            f"- Explain logic step-by-step\n"
            f"- Mention important concepts\n\n"
            f"CODE:\n{code}"
        )
    else:
        return (
            f"Find bugs in this {lang} code and provide a corrected full version.\n"
            f"- List bugs\n"
            f"- Explain each bug (1–2 sentences)\n"
            f"- Provide FULL fixed code\n\n"
            f"CODE:\n{code}"
        )

# ---- RUN BUTTON ----
if st.button("⚡ Run"):
    if not code.strip():
        st.warning("Paste some code first!")
    else:
        st.subheader("🟦 Result (Streaming...)")
        placeholder = st.empty()

        final_text = ""
        prompt = build_prompt(mode, language, code)

        # STREAMING RESPONSE (no waiting!)
        for chunk in ask_ollama(prompt):
            final_text += chunk
            placeholder.markdown(final_text)
