import streamlit as st

# Page config
st.set_page_config(
    page_title="SmartNest Automation", 
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Session state
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# FUNCTION: Navigation handler
def navigate(page):
    st.session_state.page = page
    st.rerun()

# CSS (UNCHANGED + WhatsApp button added)
st.markdown("""
<style>
/* FLOATING WHATSAPP BUTTON */
.whatsapp-float {
    position: fixed;
    bottom: 25px;
    right: 25px;
    z-index: 9999;
}
.whatsapp-float a {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 65px;
    height: 65px;
    background: #25D366;
    color: white;
    font-size: 32px;
    border-radius: 50%;
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    text-decoration: none;
    transition: all 0.3s ease;
}
.whatsapp-float a:hover {
    transform: scale(1.1);
}
</style>
""", unsafe_allow_html=True)

# FLOATING WHATSAPP BUTTON
st.markdown("""
<div class="whatsapp-float">
    <a href="https://wa.me/919876543210" target="_blank">💬</a>
</div>
""", unsafe_allow_html=True)

# HEADER (FUNCTIONAL VERSION)
st.markdown("""
<div class="header-row">
    <div class="header-title">🏠 SmartNest Automation</div>
</div>
""", unsafe_allow_html=True)

# REAL WORKING NAVIGATION BUTTONS
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home", use_container_width=True):
        navigate("Home")

with col2:
    if st.button("👨‍💼 About", use_container_width=True):
        navigate("About")

with col3:
    if st.button("📦 Products", use_container_width=True):
        navigate("Products")

with col4:
    if st.button("💬 Contact", use_container_width=True):
        navigate("Contact")

# SIDEBAR (UNCHANGED)
with st.sidebar:
    st.markdown("## 🚀 Quick Navigation")
    st.markdown("---")
    selected = st.selectbox(
        "📱 Choose Page:",
        ["Home", "About", "Products", "Contact"],
        index=["Home", "About", "Products", "Contact"].index(st.session_state.page)
    )
    if selected != st.session_state.page:
        navigate(selected)

    st.markdown("---")
    st.markdown("**🌟 Nagpur**")
    st.markdown("*Making India Smarter*")

# =========================
# YOUR ORIGINAL CONTENT BELOW (UNCHANGED)
# =========================

if st.session_state.page == "Home":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 class="hero-title">Transform Your Home<br>
            <span style="background:linear-gradient(45deg,#fff,#f0f9ff); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
            into a Smart Haven</span></h1>
            <p class="hero-subtitle">Seamless automation for modern Indian living</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🚀 Explore Packages", use_container_width=True):
            navigate("Products")
    with col2:
        if st.button("💬 Free Consultation", use_container_width=True):
            navigate("Contact")

elif st.session_state.page == "About":
    st.markdown("<h2>About Page</h2>", unsafe_allow_html=True)

elif st.session_state.page == "Products":
    st.markdown("<h2>Products Page</h2>", unsafe_allow_html=True)

elif st.session_state.page == "Contact":
    st.markdown("<h2>Contact Page</h2>", unsafe_allow_html=True)

    if not st.session_state.form_submitted:
        with st.form("interest_form"):
            name = st.text_input("Name")
            submitted = st.form_submit_button("Submit")

            if submitted:
                st.session_state.form_submitted = True
                st.rerun()

    else:
        st.success("Form submitted!")
