import streamlit as st

# Page config
st.set_page_config(
    page_title="SmartNest Automation", 
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# AICM-STYLE CSS ON YOUR SMARTNEST
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }

body { background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2a 100%); color: #e2e8f0; }

@keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
@keyframes float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-15px); } }
@keyframes gradientShift { 0%{background-position:0%50%}50%{background-position:100%50%}100%{background-position:0%50%} }

.header-row { 
    background: linear-gradient(135deg, #8b5cf6 0%, #3b82f6 50%, #06b6d4 100%); 
    padding: 1.5rem 2rem; border-radius: 0 0 20px 20px; color: white; 
    box-shadow: 0 10px 30px rgba(139,92,246,0.4);
}
.header-title { font-size: 2.2rem; font-weight: 800; text-align: center; margin-bottom: 1rem; }

.hero-section { 
    background: linear-gradient(-45deg, #8b5cf6, #ec4899, #10b981, #f59e0b); 
    background-size: 400% 400%; animation: gradientShift 12s ease infinite; 
    min-height: 500px; border-radius: 20px; margin: 2rem 0; display: flex; 
    align-items: center; justify-content: center; text-align: center; color: white;
    box-shadow: 0 20px 40px rgba(139,92,246,0.3);
}

.card-container { display: flex; align-items: stretch; height: 480px; margin-bottom: 2rem; }
.card { 
    flex: 1; background: rgba(15,15,35,0.9); backdrop-filter: blur(20px); 
    padding: 3rem 2rem; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    text-align: center; transition: all 0.3s ease; border: 1px solid rgba(139,92,246,0.3);
    display: flex; flex-direction: column; justify-content: space-between;
}
.card.gradient-card { color: white; border: 1px solid rgba(255,255,255,0.1); }
.gradient-1 { background: linear-gradient(135deg, #8b5cf6 0%, #a855f7 100%); }
.gradient-2 { background: linear-gradient(135deg, #ec4899 0%, #f472b6 100%); }
.gradient-3 { background: linear-gradient(135deg, #10b981 0%, #34d399 100%); }
.icon-large { font-size: 4rem; margin-bottom: 1.5rem; display: block; animation: float 4s ease-in-out infinite; }

.stButton > button {
    background: linear-gradient(45deg, #8b5cf6, #a855f7) !important; color: white !important; 
    padding: 1rem 2rem !important; border-radius: 25px !important; font-weight: 600 !important;
    font-size: 1.1rem !important; border: none !important; box-shadow: 0 10px 30px rgba(139,92,246,0.4) !important;
    transition: all 0.3s ease !important; width: 100%; margin-top: auto;
}
.stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 15px 35px rgba(139,92,246,0.5) !important; }

[data-testid="metric-container"] { 
    background: rgba(15,15,35,0.9) !important; padding: 1.5rem !important; 
    border-radius: 15px !important; box-shadow: 0 10px 25px rgba(0,0,0,0.4) !important;
    border: 1px solid rgba(139,92,246,0.2) !important; color: #e2e8f0 !important;
}

.form-success { background: linear-gradient(135deg, #10b981, #34d399); color: white; 
    padding: 3rem; border-radius: 20px; text-align: center; box-shadow: 0 20px 40px rgba(16,185,129,0.3); }

.footer { background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2a 100%); color: #e2e8f0; 
    padding: 3rem 2rem; text-align: center; border-radius: 20px 20px 0 0; margin-top: 4rem; 
    border-top: 1px solid rgba(139,92,246,0.2); }
</style>
""", unsafe_allow_html=True)

# Session state - YOUR ORIGINAL
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# YOUR HEADER (AICM STYLE COLORS)
st.markdown("""
<div class="header-row">
    <div class="header-title">🏠 SmartNest Automation</div>
</div>
""", unsafe_allow_html=True)

# YOUR SIDEBAR (AICM STYLE)
with st.sidebar:
    st.markdown("## 🚀 Quick Navigation")
    selected = st.selectbox("Go to:", ["Home", "About", "Products", "Contact"], 
                          index=["Home", "About", "Products", "Contact"].index(st.session_state.page))
    if selected != st.session_state.page:
        st.session_state.page = selected
        st.rerun()
    st.markdown("---")
    st.markdown("*Pimpri-Chinchwad, Maharashtra*")

# YOUR ORIGINAL CONTENT with AICM VISUALS
if st.session_state.page == "Home":
    # Hero - AICM Style
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 1.5rem; text-shadow: 2px 2px 8px rgba(0,0,0,0.5);">Transform Your Home</h1>
            <p style="font-size: 1.4rem; margin-bottom: 2.5rem;">Seamless smart automation for modern Indian living</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # YOUR Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("🏠", "10K+", "Homes")
    with col2: st.metric("⭐", "4.9/5", "Rating")
    with col3: st.metric("⚡", "99.9%", "Uptime")
    with col4: st.metric("🏢", "50+", "Cities")
    
    # YOUR Features - AICM Cards
    st.markdown('<h2 style="text-align:center; color:#8b5cf6; font-size:2.5rem; margin:3rem 0;">Why SmartNest?</h2>')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card gradient-1 gradient-card">
            <span class="icon-large">🔒</span>
            <h3 style="font-size:1.6rem;">Bank-Grade Security</h3>
            <p>End-to-end encryption</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Learn More", key="home1")
    
    with col2:
        st.markdown("""
        <div class="card gradient-2 gradient-card">
            <span class="icon-large">🔗</span>
            <h3 style="font-size:1.6rem;">Universal Integration</h3>
            <p>Alexa, Google Home</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("View Packages", key="home2")
    
    with col3:
        st.markdown("""
        <div class="card gradient-3 gradient-card">
            <span class="icon-large">⚡</span>
            <h3 style="font-size:1.6rem;">24/7 Support</h3>
            <p>Installation help</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Get Support", key="home3")

# [REST OF YOUR ORIGINAL PAGES - just with AICM CSS applied]
# About, Products, Contact remain exactly the same as your code
# Just paste your original About/Products/Contact sections here

# YOUR Footer (AICM Style)
st.markdown("""
<div class="footer">
    <h3>🏠 SmartNest Automation</h3>
    <p>Pimpri-Chinchwad, Maharashtra | <a href="mailto:info@smartnest.in" style="color:#8b5cf6;">info@smartnest.in</a> | +91 98765 43210</p>
    <p>© 2026 All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
