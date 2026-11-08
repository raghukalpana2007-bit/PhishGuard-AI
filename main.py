import streamlit as st
import re

st.set_page_config(page_title="PhishGuard AI", page_icon="🛡️")
st.title("🛡️ PhishGuard AI")
st.write("Built by Kalpana | 3rd Year | Chennai")
st.write("AI tool to detect fake links! Tamil + WhatsApp + Email Support!")

tab1, tab2, tab3 = st.tabs(["🔗 Link Check", "💬 WhatsApp Link", "📧 Email Check"])

def check_phishing(url):
    url = url.lower()
    risk = 0
    reasons = []
    
    fake_words = ["free", "money", "offer", "login", "verify", "account", "update", "gift", "lottery", "prize", "bank", "secure"]
    for word in fake_words:
        if word in url:
            risk += 2
            reasons.append(f"'{word}' fake word irukku")

    sus_tld = [".tk", ".ml", ".ga", ".cf", ".gq", ".xyz", ".top", ".buzz"]
    for tld in sus_tld:
        if tld in url:
            risk += 3
            reasons.append(f"{tld} - suspicious domain!")

    if url.count("-") >= 3:
        risk += 2
        reasons.append("Romba hyphen irukku - fake sign!")
    
    if len(url) > 75:
        risk += 1
        reasons.append("Link romba perusu")
    
    if "http://" in url:
        risk += 1
        reasons.append("https illa, http than irukku")
    
    if "@" in url:
        risk += 2
        reasons.append("@ irukku - phishing trick!")
    
    return risk, reasons

with tab1:
    st.subheader("Link ah check pannu da!")
    url = st.text_input("🔍 Enter URL:", key="a")
    if st.button("Check pannu!", key="1"):
        if url:
            risk, reasons = check_phishing(url)
            if risk >= 4:
                st.error(f"🚨 DANGER DA! Fake link! Risk Score: {risk}/10 - DANGER")
                for r in reasons:
                    st.write(f"- {r}")
            elif risk >= 2:
                st.warning(f"⚠️ Doubt ah irukku! Risk Score: {risk}/10 - Suspect")
                for r in reasons:
                    st.write(f"- {r}")
            else:
                st.success(f"✅ Safe da! No tension! Risk Score: {risk}/10 - Safe")

with tab2:
    st.subheader("WhatsApp link check pannu da!")
    url2 = st.text_input("WhatsApp link:", key="b")
    if st.button("Check pannu!", key="2"):
        if url2:
            risk, reasons = check_phishing(url2)
            if risk >= 4:
                st.error(f"🚨 WhatsApp la fake da! Risk: {risk}/10")
                for r in reasons: st.write(f"- {r}")
            else:
                st.success(f"✅ Safe da! Risk: {risk}/10")

with tab3:
    st.subheader("Email link check pannu da!")
    url3 = st.text_input("Email link:", key="c")
    if st.button("Check pannu!", key="3"):
        if url3:
            risk, reasons = check_phishing(url3)
            if risk >= 4:
                st.error(f"🚨 Email fake da! Risk: {risk}/10")
                for r in reasons: st.write(f"- {r}")
            else:
                st.success(f"✅ Safe da! Risk: {risk}/10")
