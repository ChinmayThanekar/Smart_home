import streamlit as st

# Page config
st.set_page_config(
    page_title="SmartNest Automation", 
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# FIXED CSS - PERFECT ALIGNMENT
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }

body { background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); }

/* ANIMATIONS */
@keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
@keyframes float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-15px); } }
@keyframes gradientShift { 0%{background-position:0%50%}50%{background-position:100%50%}100%{background-position:0%50%} }

/* HEADER - FIXED */
.header-row { 
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); 
    padding: 1.5rem 2rem; border-radius: 0 0 20px 20px; color: white; 
    box-shadow: 0 10px 30px rgba(30,58,138,0.3);
}
.header-title { font-size: 2.2rem; font-weight: 800; text-align: center; margin-bottom: 1rem; }
.header-nav { display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; }

/* HERO */
.hero-section { 
    background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c); 
    background-size: 400% 400%; animation: gradientShift 12s ease infinite; 
    min-height: 500px; border-radius: 20px; margin: 2rem 0; display: flex; 
    align-items: center; justify-content: center; text-align: center; color: white;
    box-shadow: 0 20px 40px rgba(102,126,234,0.3);
}
.hero-content { max-width: 1000px; padding: 2rem; }

/* PERFECT CARD ALIGNMENT - FIXED HEIGHTS */
.card-container { display: flex; align-items: stretch; height: 480px; margin-bottom: 2rem; }
.card { 
    flex: 1; background: rgba(255,255,255,0.95); backdrop-filter: blur(20px); 
    padding: 3rem 2rem; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    text-align: center; transition: all 0.3s ease; border: 1px solid rgba(255,255,255,0.2);
    display: flex; flex-direction: column; justify-content: space-between;
}
.card.gradient-card { color: white; border: none; }
.gradient-1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
.gradient-2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
.gradient-3 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
.icon-large { font-size: 4rem; margin-bottom: 1.5rem; display: block; animation: float 4s ease-in-out infinite; }

/* BUTTONS - PERFECT */
.stButton > button {
    background: linear-gradient(45deg, #ff6b6b, #ff8e8e) !important; color: white !important; 
    padding: 1rem 2rem !important; border-radius: 25px !important; font-weight: 600 !important;
    font-size: 1.1rem !important; border: none !important; box-shadow: 0 10px 30px rgba(255,107,107,0.4) !important;
    transition: all 0.3s ease !important; width: 100%; margin-top: auto;
}
.stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 15px 35px rgba(255,107,107,0.5) !important; }

/* METRICS */
[data-testid="metric-container"] { 
    background: rgba(255,255,255,0.9) !important; padding: 1.5rem !important; 
    border-radius: 15px !important; box-shadow: 0 10px 25px rgba(0,0,0,0.08) !important;
}

/* FORM */
.form-success { background: linear-gradient(135deg, #10b981, #34d399); color: white; 
    padding: 3rem; border-radius: 20px; text-align: center; box-shadow: 0 20px 40px rgba(16,185,129,0.3); }

/* FOOTER */
.footer { background: linear-gradient(135deg, #1e293b 0%, #334155 100%); color: white; 
    padding: 3rem 2rem; text-align: center; border-radius: 20px 20px 0 0; margin-top: 4rem; }
</style>
""", unsafe_allow_html=True)

# Session state
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# FIXED HEADER
st.markdown("""
<div class="header-row">
    <div class="header-title">🏠 SmartNest Automation</div>
</div>
""", unsafe_allow_html=True)

# SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("## 🚀 Quick Navigation")
    selected = st.selectbox("Go to:", ["Home", "About", "Products", "Contact"], 
                          index=["Home", "About", "Products", "Contact"].index(st.session_state.page))
    if selected != st.session_state.page:
        st.session_state.page = selected
        st.rerun()
    st.markdown("---")
    st.markdown("*Pimpri-Chinchwad, Maharashtra*")

# MAIN CONTENT - PERFECT ALIGNMENT
if st.session_state.page == "Home":
    # Hero
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 1.5rem; text-shadow: 2px 2px 8px rgba(0,0,0,0.3);">Transform Your Home</h1>
            <p style="font-size: 1.4rem; margin-bottom: 2.5rem;">Seamless smart automation for modern Indian living</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats - Perfect alignment
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("🏠", "10K+", "Homes")
    with col2: st.metric("⭐", "4.9/5", "Rating")
    with col3: st.metric("⚡", "99.9%", "Uptime")
    with col4: st.metric("🏢", "50+", "Cities")
    
    # Features
    st.markdown('<h2 style="text-align:center; color:#1e3a8a; font-size:2.5rem; margin:3rem 0;">Why SmartNest?</h2>')
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

elif st.session_state.page == "About":
    st.markdown('<h2 style="color:#1e3a8a; text-align:center; font-size:2.8rem; margin:3rem 0;">About SmartNest</h2>')
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown("""
        <div class="card gradient-1 gradient-card" style="height:400px;">
            <span class="icon-large" style="font-size:5rem;">🏢</span>
            <h3>Pimpri-Chinchwad Experts</h3>
            <p>5+ years serving Indian homes</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_column_width=True)

elif st.session_state.page == "Products":
    st.markdown('<h2 style="color:#1e3a8a; text-align:center; font-size:2.8rem; margin:3rem 0 2rem 0;">Automation Packages</h2>')
    st.markdown('<p style="text-align:center; font-size:1.2rem; color:#6b7280; margin-bottom:3rem;">Perfect for every home</p>')
    
    # FIXED PERFECT ALIGNMENT - SAME HEIGHT CONTAINERS
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card-container">
            <div class="card gradient-1 gradient-card">
                <span class="icon-large">📦</span>
                <h3 style="font-size:1.8rem; margin-bottom:1rem;">Basic Package</h3>
                <p style="font-size:1.3rem; margin-bottom:1rem;">1-2 BHK Apartments</p>
                <ul style="text-align:left; font-size:1.1rem; margin-bottom:auto;">
                    <li>✅ Smart lighting</li>
                    <li>✅ Appliance control</li>
                    <li>✅ Basic security</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("💬 Get Quote", key="prod1", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="card-container">
            <div class="card gradient-2 gradient-card">
                <span class="icon-large">⭐</span>
                <h3 style="font-size:1.8rem; margin-bottom:1rem;">Standard Package</h3>
                <p style="font-size:1.3rem; margin-bottom:1rem;">3 BHK & Villas</p>
                <ul style="text-align:left; font-size:1.1rem; margin-bottom:auto;">
                    <li>✅ Climate control</li>
                    <li>✅ Curtain automation</li>
                    <li>✅ Multi-room audio</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("💬 Get Quote", key="prod2", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="card-container">
            <div class="card gradient-3 gradient-card">
                <span class="icon-large">👑</span>
                <h3 style="font-size:1.8rem; margin-bottom:1rem;">Premium Package</h3>
                <p style="font-size:1.3rem; margin-bottom:1rem;">4+ BHK Luxury</p>
                <ul style="text-align:left; font-size:1.1rem; margin-bottom:auto;">
                    <li>✅ AI personalization</li>
                    <li>✅ Energy optimization</li>
                    <li>✅ Full integration</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("💬 Get Quote", key="prod3", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()

elif st.session_state.page == "Contact":
    st.markdown("""
    <h2 style="color:#1e3a8a; text-align:center; font-size:2.8rem; margin:3rem 0 1rem 0;">Share Your Interest</h2>
    <p style="text-align:center; font-size:1.2rem; color:#6b7280; margin-bottom:3rem;">Free quote within 24 hours</p>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Home", key="contact_home", use_container_width=True):
            st.session_state.page = "Home"
            st.rerun()
    with col2:
        if st.button("📦 Packages", key="contact_prod", use_container_width=True):
            st.session_state.page = "Products"
            st.rerun()
    
    if not st.session_state.form_submitted:
        with st.form("interest_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("👤 Name")
                email = st.text_input("📧 Email")
            with col2:
                package = st.selectbox("📦 Package", ["Basic", "Standard", "Premium"])
            
            submitted = st.form_submit_button("🚀 Send")
            if submitted:
                st.session_state.form_submitted = True
                st.rerun()
    
    if st.session_state.form_submitted:
        st.markdown("""
        <div class="form-success">
            <div style="font-size:4rem;">🎉</div>
            <h2>Thank You!</h2>
            <p>We'll contact you within 24 hours</p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

# Footer
st.markdown("""
<div class="footer">
    <h3>🏠 SmartNest Automation</h3>
    <p>Pimpri-Chinchwad, Maharashtra | info@smartnest.in | +91 98765 43210</p>
    <p>© 2026 All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
