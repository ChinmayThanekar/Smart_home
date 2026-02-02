import streamlit as st

# Page config
st.set_page_config(
    page_title="SmartNest Automation", 
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ULTIMATE ENHANCED CSS with SEAMLESS ANIMATIONS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }

body { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }

/* SMOOTH ANIMATIONS */
@keyframes fadeInUp { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }
@keyframes fadeInLeft { from { opacity: 0; transform: translateX(-40px); } to { opacity: 1; transform: translateX(0); } }
@keyframes fadeInRight { from { opacity: 0; transform: translateX(40px); } to { opacity: 1; transform: translateX(0); } }
@keyframes float { 0%, 100% { transform: translateY(0px) rotate(0deg); } 50% { transform: translateY(-25px) rotate(5deg); } }
@keyframes pulseGlow { 0% { box-shadow: 0 0 0 0 rgba(255,107,107,0.7); } 70% { box-shadow: 0 0 0 25px rgba(255,107,107,0); } 100% { box-shadow: 0 0 0 0 rgba(255,107,107,0); } }
@keyframes gradientShift { 0%{background-position:0%50%}50%{background-position:100%50%}100%{background-position:0%50%} }
@keyframes shimmer { 0% { background-position: -468px 0; } 100% { background-position: 468px 0; } }

/* HEADER */
.header-row { 
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 50%, #1e40af 100%); 
    padding: 2rem 3rem; border-radius: 0 0 30px 30px; color: white; 
    box-shadow: 0 25px 50px rgba(30,58,138,0.4); position: sticky; top: 0; z-index: 100;
    animation: fadeInDown 1s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
@keyframes fadeInDown { from { opacity: 0; transform: translateY(-30px); } to { opacity: 1; transform: translateY(0); } }
.header-title { font-size: 3rem; font-weight: 800; text-align: center; letter-spacing: -1px; }
.header-nav { display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap; animation: fadeInUp 1s ease 0.3s both; }
.header-nav button { 
    background: rgba(255,255,255,0.15); backdrop-filter: blur(15px); border: 2px solid rgba(255,255,255,0.3);
    color: white; padding: 1rem 2.5rem; border-radius: 40px; font-weight: 600; font-size: 1.1rem;
    cursor: pointer; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); position: relative; overflow: hidden;
}
.header-nav button::before { content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; 
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent); transition: left 0.5s; }
.header-nav button:hover::before { left: 100%; }
.header-nav button:hover { background: rgba(255,255,255,0.25); transform: translateY(-4px); box-shadow: 0 20px 40px rgba(0,0,0,0.3); }

/* HERO */
.hero-section { 
    background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c); background-size: 400% 400%; 
    animation: gradientShift 15s ease infinite; height: 80vh; border-radius: 30px; margin: 4rem 0;
    display: flex; align-items: center; justify-content: center; text-align: center; color: white;
    position: relative; overflow: hidden; box-shadow: 0 40px 80px rgba(102,126,234,0.4);
}
.hero-content { max-width: 1200px; padding: 3rem; animation: fadeInUp 1.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.hero-title { font-size: 4.5rem; font-weight: 800; margin-bottom: 1.5rem; text-shadow: 0 6px 20px rgba(0,0,0,0.4); letter-spacing: -1px; }
.hero-subtitle { font-size: 1.6rem; margin-bottom: 3.5rem; opacity: 0.95; font-weight: 300; line-height: 1.6; }

/* CARDS */
.card { 
    background: rgba(255,255,255,0.95); backdrop-filter: blur(25px); padding: 3.5rem 3rem; border-radius: 30px; 
    box-shadow: 0 30px 60px rgba(0,0,0,0.12); border: 1px solid rgba(255,255,255,0.3); height: 100%;
    text-align: center; transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); position: relative;
    animation: fadeInUp 1s ease forwards; opacity: 0;
}
.card:nth-child(1) { animation-delay: 0.2s; }
.card:nth-child(2) { animation-delay: 0.4s; }
.card:nth-child(3) { animation-delay: 0.6s; }
.card:hover { 
    transform: translateY(-15px) scale(1.03); box-shadow: 0 50px 100px rgba(0,0,0,0.25); 
    background: rgba(255,255,255,1);
}
.gradient-card { color: white !important; border: none; }
.gradient-1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
.gradient-2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
.gradient-3 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
.gradient-4 { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }
.icon-large { font-size: 5rem; margin-bottom: 2rem; display: block; animation: float 4s ease-in-out infinite; }

/* ENHANCED BUTTONS */
.stButton > button {
    background: linear-gradient(45deg, #ff6b6b, #ff8e8e) !important; color: white !important; 
    padding: 1.2rem 3rem !important; border-radius: 35px !important; font-weight: 700 !important;
    font-size: 1.15rem !important; border: none !important; box-shadow: 0 15px 40px rgba(255,107,107,0.4) !important;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; width: 100%; height: 60px;
    position: relative; overflow: hidden;
}
.stButton > button::before {
    content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%; 
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent); 
    transition: left 0.6s ease;
}
.stButton > button:hover::before { left: 100%; }
.stButton > button:hover { transform: translateY(-5px) !important; box-shadow: 0 25px 50px rgba(255,107,107,0.6) !important; }
.btn-success { background: linear-gradient(45deg, #10b981, #34d399) !important; box-shadow: 0 15px 40px rgba(16,185,129,0.4) !important; }

/* METRICS */
[data-testid="metric-container"] { 
    background: rgba(255,255,255,0.95) !important; padding: 2rem !important; 
    border-radius: 25px !important; box-shadow: 0 20px 40px rgba(0,0,0,0.1) !important; 
    text-align: center !important; border: 1px solid rgba(255,255,255,0.3) !important;
    transition: all 0.3s ease !important;
}
[data-testid="metric-container"]:hover { transform: translateY(-5px) !important; box-shadow: 0 30px 60px rgba(0,0,0,0.15) !important; }

/* FORM */
.form-success { 
    background: linear-gradient(135deg, #10b981, #34d399); color: white; padding: 4.5rem; 
    border-radius: 30px; text-align: center; box-shadow: 0 40px 80px rgba(16,185,129,0.4); 
    animation: fadeInUp 1s cubic-bezier(0.175, 0.885, 0.32, 1.275); margin: 4rem 0;
}

/* FOOTER */
.footer { 
    background: linear-gradient(135deg, #1e293b 0%, #334155 100%); color: white; 
    padding: 5rem 3rem; text-align: center; border-radius: 30px 30px 0 0; 
    box-shadow: 0 -30px 60px rgba(30,41,59,0.4); margin-top: 6rem;
}
</style>
""", unsafe_allow_html=True)

# Session state
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# SPECTACULAR ANIMATED HEADER
st.markdown("""
<div class="header-row">
    <div class="header-title">🏠 SmartNest Automation</div>
    <div class="header-nav">
        <button onclick="window.parent.document.querySelector('[data-testid=column] button[key*=home]').click()">🏠 Home</button>
        <button onclick="window.parent.document.querySelector('[data-testid=column] button[key*=about]').click()">👨‍💼 About</button>
        <button onclick="window.parent.document.querySelector('[data-testid=column] button[key*=product]').click()">📦 Products</button>
        <button onclick="window.parent.document.querySelector('[data-testid=column] button[key*=contact]').click()">💬 Contact</button>
    </div>
</div>
""", unsafe_allow_html=True)

# ENHANCED SIDEBAR
with st.sidebar:
    st.markdown("## 🚀 Quick Navigation")
    st.markdown("---")
    selected = st.selectbox("📱 Choose Page:", ["Home", "About", "Products", "Contact"], 
                          index=["Home", "About", "Products", "Contact"].index(st.session_state.page))
    if selected != st.session_state.page:
        st.session_state.page = selected
        st.rerun()
    st.markdown("---")
    st.markdown("**🌟 Nagpur**")
    st.markdown("*Making India Smarter*")

# MAIN CONTENT - FULLY ANIMATED
if st.session_state.page == "Home":
    # BREATHTAKING HERO
    st.markdown("""
    <div class="hero-section">
        <div style="position:absolute; width:100%; height:100%; overflow:hidden; pointer-events:none; z-index:1;">
            <div style="position:absolute; top:20%; left:10%; font-size:4rem; animation:float 6s ease-in-out infinite;">💡</div>
            <div style="position:absolute; top:60%; right:15%; font-size:4rem; animation:float 6s ease-in-out infinite 1.5s;">🔒</div>
            <div style="position:absolute; bottom:20%; left:20%; font-size:4rem; animation:float 6s ease-in-out infinite 3s;">🌡️</div>
            <div style="position:absolute; top:30%; right:25%; font-size:4rem; animation:float 6s ease-in-out infinite 2s;">🎵</div>
        </div>
        <div class="hero-content">
            <h1 class="hero-title">Transform Your Home<br><span style="background:linear-gradient(45deg,#fff,#f0f9ff); -webkit-background-clip:text; -webkit-text-fill-color:transparent; font-weight:900;">into a Smart Haven</span></h1>
            <p class="hero-subtitle">Seamless automation for modern Indian living • One tap control for lights, security & climate</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🚀 Explore Packages", key="home_explore", use_container_width=True):
            st.session_state.page = "Products"
            st.rerun()
    with col2:
        if st.button("💬 Free Consultation", key="home_consult", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()
    
    # ELEGANT STATS
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("🏠", "10K+", "Homes Automated")
    with col2: st.metric("⭐", "4.9/5", "Customer Rating")
    with col3: st.metric("⚡", "99.9%", "Uptime")
    with col4: st.metric("🏢", "50+", "Cities Covered")
    
    # ANIMATED FEATURE CARDS
    st.markdown('<h2 style="text-align:center; color:#1e3a8a; font-size:3rem; margin:5rem 0 4rem 0; font-weight:800;">Why Choose SmartNest?</h2>')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card gradient-1 gradient-card">
            <span class="icon-large">🔒</span>
            <h3 style="font-size:2rem; margin-bottom:1.5rem;">Bank-Grade Security</h3>
            <p style="font-size:1.2rem; opacity:0.95; line-height:1.7;">End-to-end encryption<br><strong>Zero data leaks</strong> guaranteed</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔒 Learn More", key="home_sec", use_container_width=True):
            st.session_state.page = "About"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="card gradient-2 gradient-card">
            <span class="icon-large">🔗</span>
            <h3 style="font-size:2rem; margin-bottom:1.5rem;">Universal Integration</h3>
            <p style="font-size:1.2rem; opacity:0.95; line-height:1.7;">Alexa • Google Home<br>Apple HomeKit • <strong>500+ devices</strong></p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📦 View Packages", key="home_pkg", use_container_width=True):
            st.session_state.page = "Products"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="card gradient-3 gradient-card">
            <span class="icon-large">⚡</span>
            <h3 style="font-size:2rem; margin-bottom:1.5rem;">24/7 Expert Support</h3>
            <p style="font-size:1.2rem; opacity:0.95; line-height:1.7;">Installation • Troubleshooting<br><strong>Lifetime assistance</strong></p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("💬 Get Support", key="home_support", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()

elif st.session_state.page == "About":
    # PERFECTLY ALIGNED HEADER
    st.markdown("""
    <h2 style="color:#1e3a8a; text-align:center; font-size:3.5rem; margin:4rem 0 2rem 0; font-weight:800;">About SmartNest Automation</h2>
    <p style="text-align:center; font-size:1.5rem; color:#6b7280; margin-bottom:4rem;">Nagpur's leading smart home automation experts</p>
    """, unsafe_allow_html=True)
    
    # MAIN CONTENT - PERFECTLY BALANCED
    col1, col2 = st.columns([1.1, 1])
    
    with col1:
        # FIXED HEIGHT & PERFECT SPACING
        st.markdown("""
        <div class="card gradient-1 gradient-card" style="height:520px; padding:3.5rem 3rem; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
                <span class="icon-large" style="font-size:5.5rem;">🏢</span>
                <h3 style="font-size:2.1rem; margin:1.5rem 0 1rem 0; font-weight:800;">Nagpur's<br>Smart Home Pioneers</h3>
                <p style="font-size:1.25rem; line-height:1.7; opacity:0.95; margin-bottom:1.5rem;">
                    5+ years transforming Indian homes from Mumbai apartments 
                    to Bangalore villas with <strong>enterprise-grade reliability</strong>.
                </p>
                <ul style="text-align:left; font-size:1.15rem; line-height:1.6;">
                    <li>✅ 10K+ homes automated</li>
                    <li>✅ 50+ cities covered</li>
                    <li>✅ 99.9% uptime guaranteed</li>
                </ul>
            </div>
            <div style="margin-top:auto;">
                <p style="font-size:1.4rem; font-weight:700; margin-bottom:1rem;">Since 2021</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # IMAGE CONTAINER - SAME HEIGHT
        st.markdown("""
        <div style="height:520px; border-radius:30px; overflow:hidden; box-shadow:0 30px 60px rgba(0,0,0,0.15); background:linear-gradient(135deg, rgba(255,255,255,0.9), rgba(248,250,252,0.8)); display:flex; align-items:center; justify-content:center;">
            <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=900&h=520&q=85" style="width:100%; height:100%; object-fit:cover; border-radius:30px;">
        </div>
        """, unsafe_allow_html=True)
    
    # PERFECTLY ALIGNED ACTION BUTTONS
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("📦 Explore Packages", key="about_pkg", use_container_width=True):
            st.session_state.page = "Products"
            st.rerun()
    with col2:
        if st.button("💬 Free Consultation", key="about_chat", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()
    
    # JOURNEY TIMELINE - PERFECT ALIGNMENT
    st.markdown('<h3 style="color:#1e3a8a; text-align:center; font-size:2.5rem; margin:5rem 0 3.5rem 0; font-weight:700;">Our Journey</h3>')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card gradient-2 gradient-card" style="height:300px; padding:3rem; display:flex; flex-direction:column; justify-content:space-between;">
            <span class="icon-large" style="font-size:4.5rem;">📅</span>
            <div style="margin-top:auto;">
                <h4 style="font-size:2rem; margin-bottom:0.5rem; font-weight:800;">2021</h4>
                <p style="font-size:1.25rem; opacity:0.95;">Founded in Pune</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card gradient-3 gradient-card" style="height:300px; padding:3rem; display:flex; flex-direction:column; justify-content:space-between;">
            <span class="icon-large" style="font-size:4.5rem;">🚀</span>
            <div style="margin-top:auto;">
                <h4 style="font-size:2rem; margin-bottom:0.5rem; font-weight:800;">2024</h4>
                <p style="font-size:1.25rem; opacity:0.95;">10K+ homes automated</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card gradient-4 gradient-card" style="height:300px; padding:3rem; display:flex; flex-direction:column; justify-content:space-between;">
            <span class="icon-large" style="font-size:4.5rem;">🎯</span>
            <div style="margin-top:auto;">
                <h4 style="font-size:2rem; margin-bottom:0.5rem; font-weight:800;">2026</h4>
                <p style="font-size:1.25rem; opacity:0.95;">50K homes target</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # SPACING
    st.markdown("<div style='height:3rem;'></div>", unsafe_allow_html=True)


elif st.session_state.page == "Products":
    # FIXED HEIGHTS & PERFECT ALIGNMENT
    st.markdown("""
    <h2 style="color:#1e3a8a; text-align:center; font-size:3.5rem; margin:4rem 0 1.5rem 0; font-weight:800;">Full Home Automation Packages</h2>
    <p style="text-align:center; font-size:1.5rem; color:#6b7280; margin-bottom:4rem;">Tailored solutions for every home size and lifestyle</p>
    """, unsafe_allow_html=True)
    
    # EQUAL HEIGHT CONTAINERS
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card gradient-1 gradient-card" style="height:480px; padding:3rem; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
                <span class="icon-large" style="font-size:5rem;">📦</span>
                <h3 style="font-size:2rem; margin:1.5rem 0 1rem 0;">Basic Package</h3>
                <p style="font-size:1.3rem; margin-bottom:2rem; opacity:0.95;">1-2 BHK Apartments</p>
                <ul style="text-align:left; font-size:1.15rem; line-height:1.7; margin-bottom:0; flex-grow:1;">
                    <li style="margin-bottom:0.5rem;">✅ Smart lighting</li>
                    <li style="margin-bottom:0.5rem;">✅ Appliance control</li>
                    <li style="margin-bottom:0.5rem;">✅ Basic security</li>
                </ul>
            </div>
            <div style="margin-top:auto;">
                <p style="font-size:1.4rem; font-weight:600; margin-bottom:1rem; color:#fff;">Starting ₹49,999</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("💬 Get Quote", key="prod_basic", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="card gradient-2 gradient-card" style="height:480px; padding:3rem; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
                <span class="icon-large" style="font-size:5rem;">⭐</span>
                <h3 style="font-size:2rem; margin:1.5rem 0 1rem 0;">Standard Package</h3>
                <p style="font-size:1.3rem; margin-bottom:2rem; opacity:0.95;">3 BHK & Villas</p>
                <ul style="text-align:left; font-size:1.15rem; line-height:1.7; margin-bottom:0; flex-grow:1;">
                    <li style="margin-bottom:0.5rem;">✅ Climate control</li>
                    <li style="margin-bottom:0.5rem;">✅ Curtain automation</li>
                    <li style="margin-bottom:0.5rem;">✅ Multi-room audio</li>
                </ul>
            </div>
            <div style="margin-top:auto;">
                <p style="font-size:1.4rem; font-weight:600; margin-bottom:1rem; color:#fff;">Starting ₹99,999</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("💬 Get Quote", key="prod_standard", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="card gradient-3 gradient-card" style="height:480px; padding:3rem; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
                <span class="icon-large" style="font-size:5rem;">👑</span>
                <h3 style="font-size:2rem; margin:1.5rem 0 1rem 0;">Premium Package</h3>
                <p style="font-size:1.3rem; margin-bottom:2rem; opacity:0.95;">4+ BHK Luxury Homes</p>
                <ul style="text-align:left; font-size:1.15rem; line-height:1.7; margin-bottom:0; flex-grow:1;">
                    <li style="margin-bottom:0.5rem;">✅ AI personalization</li>
                    <li style="margin-bottom:0.5rem;">✅ Energy optimization</li>
                    <li style="margin-bottom:0.5rem;">✅ Full integration</li>
                </ul>
            </div>
            <div style="margin-top:auto;">
                <p style="font-size:1.4rem; font-weight:600; margin-bottom:1rem; color:#fff;">Starting ₹1,99,999</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("💬 Get Quote", key="prod_premium", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()
    
    # PERFECT SPACING BELOW
    st.markdown("<div style='height:2rem;'></div>", unsafe_allow_html=True)


elif st.session_state.page == "Contact":
    st.markdown("""
    <h2 style="color:#1e3a8a; text-align:center; font-size:3.5rem; margin:4rem 0 1.5rem 0; font-weight:800;">Share Your Interest</h2>
    <p style="text-align:center; font-size:1.5rem; color:#6b7280; margin-bottom:4rem;">Get your personalized quote within 24 hours • 100% free consultation</p>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🏠 Back to Home", key="contact_home", use_container_width=True):
            st.session_state.page = "Home"
            st.session_state.form_submitted = False
            st.rerun()
    with col2:
        if st.button("📦 View Packages", key="contact_products", use_container_width=True):
            st.session_state.page = "Products"
            st.session_state.form_submitted = False
            st.rerun()
    
    if not st.session_state.form_submitted:
        with st.form("interest_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("👤 Full Name *", placeholder="Enter your full name")
                email = st.text_input("📧 Email *", placeholder="your@email.com")
                phone = st.text_input("📱 Phone", placeholder="+91 98765 43210")
            with col2:
                package = st.selectbox("📦 Package Interest", ["Basic Package", "Standard Package", "Premium Package"])
                home_type = st.selectbox("🏠 Home Type", ["1-2 BHK", "3 BHK", "4+ BHK", "Villa/Independent"])
                budget = st.selectbox("💰 Budget Range", ["Economy (₹50K-1L)", "Mid-Range (₹1-3L)", "Premium (₹3L+)"])
            
            message = st.text_area("💬 Project Details", 
                                 placeholder="Home size? Special requirements? Current setup?", height=120)
            
            col1, col2 = st.columns([2, 1])
            submitted = col1.form_submit_button("🚀 Send My Interest", use_container_width=True)
            
            if submitted:
                st.session_state.form_submitted = True
                st.rerun()
    
    if st.session_state.form_submitted:
        st.markdown("""
        <div class="form-success">
            <div style="font-size:5rem; margin-bottom:1.5rem; animation: pulseGlow 2s infinite;">🎉</div>
            <h2 style="font-size:2.5rem; margin-bottom:1.5rem; font-weight:800;">Thank You!</h2>
            <p style="font-size:1.4rem; line-height:1.6;">We'll contact you within <strong>24 hours</strong> with your personalized quote.</p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
        
        st.markdown("### 📋 Your Submitted Details:")
        details = {
            "Name": name if 'name' in locals() else "",
            "Email": email if 'email' in locals() else "",
            "Phone": phone if 'phone' in locals() else "",
            "Package": package if 'package' in locals() else "",
            "Home Type": home_type if 'home_type' in locals() else "",
            "Budget": budget if 'budget' in locals() else "",
            "Message": message if 'message' in locals() else ""
        }
        st.json(details)

# SPECTACULAR FOOTER
st.markdown("""
<div class="footer">
    <h3 style="font-size:2.5rem; margin-bottom:1.5rem; font-weight:800;">🏠 SmartNest Automation</h3>
    <p style="font-size:1.3rem; opacity:0.95; margin-bottom:1.5rem;">
        Nagpur, Maharashtra, India | 
        <a href="mailto:info@smartnest.in" style="color:#60a5fa; text-decoration:none; font-weight:600;">📧 info@smartnest.in</a> | 
        📱 +91 98765 43210
    </p>
    <p style="font-size:1.1rem; opacity:0.8;">© 2026 All Rights Reserved | Making India Smarter, One Home at a Time</p>
</div>
""", unsafe_allow_html=True)
