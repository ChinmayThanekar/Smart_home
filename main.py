import streamlit as st
import pandas as pd
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="SmartNest Automation",
    page_icon="🏠",
    layout="wide"
)

# =========================
# SESSION STATE
# =========================
if 'page' not in st.session_state:
    st.session_state.page = "Home"

if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

# =========================
# NAVBAR
# =========================
st.markdown("## 🏠 SmartNest Automation")

col1, col2, col3, col4 = st.columns(4)

if col1.button("🏠 Home"):
    st.session_state.page = "Home"

if col2.button("👨‍💼 About"):
    st.session_state.page = "About"

if col3.button("📦 Products"):
    st.session_state.page = "Products"

if col4.button("💬 Contact"):
    st.session_state.page = "Contact"

st.divider()

# =========================
# HOME PAGE
# =========================
if st.session_state.page == "Home":
    st.title("Transform Your Home into a Smart Haven")
    st.write("Control lights, security & climate with one tap.")

    col1, col2 = st.columns(2)

    if col1.button("🚀 Explore Packages"):
        st.session_state.page = "Products"
        st.rerun()

    if col2.button("💬 Free Consultation"):
        st.session_state.page = "Contact"
        st.rerun()

    st.divider()

    col1, col2, col3 = st.columns(3)
    col1.metric("🏠 Homes Automated", "10K+")
    col2.metric("⭐ Rating", "4.9/5")
    col3.metric("🏙 Cities Covered", "50+")

# =========================
# ABOUT PAGE
# =========================
elif st.session_state.page == "About":
    st.title("About SmartNest")

    st.write("""
    SmartNest Automation provides modern smart home solutions across India.

    ✅ Smart Lighting  
    ✅ Security Systems  
    ✅ Voice Control (Alexa / Google)  
    ✅ Full Home Automation  

    We help you transform your home into a smart, secure, and energy-efficient space.
    """)

# =========================
# PRODUCTS PAGE
# =========================
elif st.session_state.page == "Products":
    st.title("Our Packages")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📦 Basic Package")
        st.write("For 1-2 BHK")
        st.write("💰 ₹49,999")
        if st.button("Get Quote - Basic"):
            st.session_state.page = "Contact"
            st.rerun()

    with col2:
        st.subheader("⭐ Standard Package")
        st.write("For 3 BHK")
        st.write("💰 ₹99,999")
        if st.button("Get Quote - Standard"):
            st.session_state.page = "Contact"
            st.rerun()

    with col3:
        st.subheader("👑 Premium Package")
        st.write("For Villas / Luxury Homes")
        st.write("💰 ₹1,99,999")
        if st.button("Get Quote - Premium"):
            st.session_state.page = "Contact"
            st.rerun()

# =========================
# CONTACT PAGE (CRM)
# =========================
elif st.session_state.page == "Contact":
    st.title("Get Your Smart Home Quote")

    if not st.session_state.form_submitted:
        with st.form("lead_form"):
            name = st.text_input("👤 Full Name")
            email = st.text_input("📧 Email")
            phone = st.text_input("📱 Phone")
            package = st.selectbox("📦 Package", ["Basic", "Standard", "Premium"])
            message = st.text_area("💬 Requirements")

            submitted = st.form_submit_button("🚀 Submit")

            if submitted:
                data = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "package": package,
                    "message": message,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                # Save to CSV (CRM)
                try:
                    df = pd.read_csv("leads.csv")
                    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
                except:
                    df = pd.DataFrame([data])

                df.to_csv("leads.csv", index=False)

                st.session_state.form_data = data
                st.session_state.form_submitted = True
                st.rerun()

    else:
        st.success("✅ Lead submitted successfully!")
        st.json(st.session_state.form_data)

        st.markdown("### 📞 Instant Contact")
        st.markdown("[💬 Chat on WhatsApp](https://wa.me/919876543210)")
        st.markdown("📞 Call Now: +91 98765 43210")

        if st.button("Submit Another Response"):
            st.session_state.form_submitted = False
            st.rerun()

# =========================
# FOOTER
# =========================
st.divider()
st.markdown("© 2026 SmartNest Automation | India")
