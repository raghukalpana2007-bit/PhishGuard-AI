import streamlit as st
import re

st.set_page_config(page_title="PhishGuard AI", page_icon="🛡️")

st.title("🛡️ PhishGuard AI")
st.subheader("Built by Kalpana | 3rd Year | Chennai")
st.write("AI tool to detect fake links!")

url = st.text_input("🔗 Enter URL:", placeholder="https://example.com")

def is_phishing(url):
    score = 0
    reasons = []
    if len(url) > 75:
        score += 2
        reasons.append("⚠️ URL unusually long")
    if "@" in url:
        score += 3
        reasons.append("🚨 Contains '@' symbol")
    if url.count('.') > 4:
        score += 2
        reasons.append("⚠️ Too many dots")
    if "https" not in url:
        score += 2
        reasons.append("🔓 No HTTPS")
    if re.search(r"(login|verify|free|bonus)", url.lower()):
        score += 2
        reasons.append("🎣 Suspicious words")
    return score, reasons

if st.button("Check Now"):
    if url:
        score, reasons = is_phishing(url)
        if score >= 4:
            st.error(f"🚨 PHISHING! Score: {score}/10")
        elif score >= 2:
            st.warning(f"⚠️ Suspicious! Score: {score}/10")
        else:
            st.success(f"✅ Safe! Score: {score}/10")
        for r in reasons:
            st.write(f"- {r}")
    else:
        st.warning("URL enter pannu da!")

st.markdown("---")
st.write("Tech: Python | Streamlit | Try: http://free-bonus-login.com@google.com")