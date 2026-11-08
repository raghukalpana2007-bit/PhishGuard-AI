import streamlit as st
import re

st.set_page_config(page_title="PhishGuard AI", page_icon="🛡️")

st.title("🛡️ PhishGuard AI")
st.subheader("Built by Kalpana | 3rd Year | Chennai")
st.write("AI tool to detect fake links! | Tamil + WhatsApp + Email Support!")

# Create Tabs for 3 Features
tab1, tab2, tab3 = st.tabs(["🔗 Link Check", "💬 WhatsApp Link", "📧 Email Check"])

def is_phishing(url):
    score = 0
    reasons = []
    if len(url) > 75:
        score += 2
        reasons.append("⚠️ URL unusually long")
    if "@" in url:
        score += 3
        reasons.append("🚩 Contains '@' symbol")
    if url.count('.') > 4:
        score += 2
        reasons.append("🚩 Too many dots")
    if "login" in url.lower() or "verify" in url.lower():
        score += 1
        reasons.append("⚠️ Suspicious keywords")
    return score, reasons

def show_result(url):
    score, reasons = is_phishing(url)
    if score >= 3:
        st.error("🚨 AYYO! Idhu Fraud Link da! Click pannadha da!")
        st.error(f"Risk Score: {score}/10 - DANGER!")
        for r in reasons:
            st.write(r)
        st.warning("Idhu un data ah thirudum! Delete pannidu!")
    else:
        st.success("✅ Safe da! No tension, use pannalam!")
        st.balloons()
        st.write(f"Risk Score: {score}/10 - Safe")

with tab1:
    st.write("### Link ah check pannu da!")
    url = st.text_input("🔍 Enter URL:", placeholder="https://example.com", key="url1")
    if st.button("Check pannu!", key="b1"):
        if url:
            show_result(url)
        else:
            st.warning("Link enter pannu da!")

with tab2:
    st.write("### WhatsApp la vantha link ah check pannu!")
    wa_url = st.text_area("WhatsApp Message ah full ah paste pannu:", placeholder="Forwarded message paste pannu da...", key="wa")
    if st.button("WhatsApp Link Check!", key="b2"):
        # Extract URLs from text
        urls = re.findall(r'http[s]?://\S+', wa_url)
        if urls:
            for u in urls:
                st.write(f"Found: {u}")
                show_result(u)
        else:
            st.warning("Link eh illa da! Message la link irukka paaru!")

with tab3:
    st.write("### Email phishing ah check pannu!")
    email_text = st.text_area("Email content ah paste pannu:", placeholder="Dear user, your account blocked... click here...", key="email")
    if st.button("Email Check!", key="b3"):
        if email_text:
            urls = re.findall(r'http[s]?://\S+', email_text)
            suspicious_words = ["urgent", "blocked", "verify", "lottery", "prize", "click immediately"]
            count = sum(1 for w in suspicious_words if w in email_text.lower())
            if count >= 2 or urls:
                st.error("🚨 Dei! Idhu Fake Email da! Nambadha!")
                st.write(f"{count} suspicious words found!")
                for u in urls:
                    show_result(u)
            else:
                st.success("✅ Email ok maadhiri theriyuthu, but careful ah iru da!")
        else:
            st.warning("Email paste pannu da!")
