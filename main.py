import streamlit as st
import pandas as pd
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="SmartNest Automation",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
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
# PREMIUM CSS (YOUR UI KEPT)
# =========================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.header {
    background: linear-gradient(135deg, #1e3a8a, #3b82f6);
    padding: 2rem;
    border-radius: 0 0 25px 25px;
    text-align: center;
    color: white;
    font-size: 2.5rem;
    font-weight: 800;
}

.card {
    background: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    text-align: center;
    transition: 0.3s;
}
.card:hover {
    transform: translateY(-10px);
}

.hero {
    background: linear-gradient(135deg,#667eea,#764ba2);
    padding: 5rem;
    border-radius: 25px;
    text-align: center;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (FIXED)
# =========================
st.markdown('<div class="header">🏠 SmartNest Automation</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

if col1.button("Home"):
    st.session_state.page = "Home"
if col2.button("About"):
    st.session_state.page = "About"
if col3.button("Products"):
    st.session_state.page = "Products"
if col4.button("Contact"):
    st.session_state.page = "Contact"

# =========================
# HOME
# =========================
if st.session_state.page == "Home":

    st.markdown("""
    <div class="hero">
        <h1>Transform Your Home into a Smart Haven</h1>
        <p>Control lights, security & climate with one tap</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    if col1.button("🚀 Explore Packages"):
        st.session_state.page = "Products"
        st.rerun()

    if col2.button("💬 Free Consultation"):
        st.session_state.page = "Contact"
        st.rerun()

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric("🏠 Homes", "10K+")
    col2.metric("⭐ Rating", "4.9")
    col3.metric("🏙 Cities", "50+")

# =========================
# ABOUT
# =========================
elif st.session_state.page == "About":
    st.markdown("## About SmartNest")

    st.markdown("""
    <div class="card">
    SmartNest delivers smart automation solutions across India.<br><br>
    ✅ Smart Lighting<br>
    ✅ Security Systems<br>
    ✅ Voice Control<br>
    </div>
    """, unsafe_allow_html=True)

# =========================
# PRODUCTS
# =========================
elif st.session_state.page == "Products":
    st.markdown("## Packages")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card"><h3>Basic</h3><p>₹49,999</p></div>', unsafe_allow_html=True)
        if st.button("Get Quote Basic"):
            st.session_state.page = "Contact"

    with col2:
        st.markdown('<div class="card"><h3>Standard</h3><p>₹99,999</p></div>', unsafe_allow_html=True)
        if st.button("Get Quote Standard"):
            st.session_state.page = "Contact"

    with col3:
        st.markdown('<div class="card"><h3>Premium</h3><p>₹1,99,999</p></div>', unsafe_allow_html=True)
        if st.button("Get Quote Premium"):
            st.session_state.page = "Contact"

# =========================
# CONTACT + CRM
# =========================
elif st.session_state.page == "Contact":
    st.markdown("## Get Your Quote")

    if not st.session_state.form_submitted:
        with st.form("form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            package = st.selectbox("Package", ["Basic", "Standard", "Premium"])
            message = st.text_area("Requirements")

            submit = st.form_submit_button("Submit")

            if submit:
                data = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "package": package,
                    "message": message,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

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
        st.success("✅ Submitted successfully!")
        st.json(st.session_state.form_data)

        st.markdown("[💬 WhatsApp](https://wa.me/919876543210)")
        st.markdown("📞 Call: +91 98765 43210")

        if st.button("Submit Again"):
            st.session_state.form_submitted = False
            st.rerun()

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("© SmartNest Automation")
