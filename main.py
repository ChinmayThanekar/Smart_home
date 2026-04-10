import streamlit as st

logo_url = "https://github.com/ChinmayThanekar/Smart_home/blob/c3762dab5100a27dfa68cbe7450503a0dc2e51f3/Gemini_Generated_Image_uy80ituy80ituy80.png"

# Page config
st.set_page_config(
    page_title="Niva Novus", 
    page_icon=logo_url,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ULTIMATE ENHANCED CSS with SEAMLESS ANIMATIONS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

/* GLOBAL */
body { 
    background: #f5f1e8;
    color: #1f2933;
    font-family: 'Inter', sans-serif;
}

/* HEADINGS */
h1, h2, h3, .header-title {
    font-family: 'Playfair Display', serif !important;
    letter-spacing: 0.5px;
    color: #1b4332;
}

/* ANIMATIONS */
@keyframes luxuryFadeUp {
    from { opacity: 0; transform: translateY(25px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes luxuryFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-12px); }
}

@keyframes shimmer {
    0% { transform: translateX(-100%) rotate(25deg); }
    100% { transform: translateX(100%) rotate(25deg); }
}

/* HEADER */
.header-row { 
    background: #1b4332;
    padding: 2rem 3rem; 
    border-radius: 0 0 30px 30px; 
    color: #f5f1e8; 
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    animation: luxuryFadeUp 1s ease;
}
.header-title { 
    font-size: 3rem; 
    font-weight: 700; 
    text-align: center; 
    color: #e6d3a3;
}

/* NAV BUTTONS */
.header-nav button { 
    background: transparent; 
    border: 1px solid rgba(230,211,163,0.4);
    color: #e6d3a3;
    transition: 0.3s;
}
.header-nav button:hover { 
    background: rgba(230,211,163,0.15); 
    transform: translateY(-2px);
}

/* HERO */
.hero-section { 
    background: linear-gradient(135deg, #1b4332, #2d6a4f);
    height: 80vh; 
    border-radius: 30px; 
    margin: 4rem 0;
    color: #f5f1e8;
    box-shadow: 0 30px 80px rgba(0,0,0,0.2);
    
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding: 0 6rem;
    position: relative;
}

/* HERO CONTENT */
.hero-content {
    max-width: 700px;
    text-align: left;
    position: relative;
    z-index: 2;
    animation: luxuryFadeUp 1.2s ease;
}

/* MAIN TITLE */
.hero-title { 
    color: #f8f5ef !important;   /* clean white */
    font-weight: 700;
}

/* GRADIENT TEXT FIX (IMPORTANT) */
.hero-title span {
    background: none !important;
    -webkit-text-fill-color: #e6d3a3 !important;
    color: #e6d3a3 !important;
}

.hero-subtitle { 
    color: #d8d3c3 !important;
    margin-top: 1rem;
    font-size: 1.1rem;
}

/* ICONS (make them subtle, not distracting) */
.hero-section div[style*="font-size:4rem"] {
    position: absolute !important;
    opacity: 0.25;
    filter: grayscale(60%);
    animation: luxuryFloat 8s ease-in-out infinite !important;
    z-index: 0;
}

/* FLOATING ICONS */
.hero-section div[style*="font-size:4rem"] {
    animation: luxuryFloat 8s ease-in-out infinite !important;
}

/* CARDS */
.card { 
    background: #ffffff; 
    padding: 3.5rem 3rem; 
    border-radius: 30px; 
    box-shadow: 0 20px 50px rgba(0,0,0,0.08); 
    border: 1px solid rgba(0,0,0,0.05);
    color: #1f2933;
    animation: luxuryFadeUp 0.8s ease forwards;
}
.card:hover { 
    transform: translateY(-10px) scale(1.01);
    box-shadow: 0 30px 70px rgba(0,0,0,0.12);
}

/* REMOVE OLD BRIGHT GRADIENTS */
.gradient-1, .gradient-2, .gradient-3, .gradient-4 {
    background: #ffffff !important;
}
.gradient-card:hover {
    background: #f8f5ef !important;
}

/* BUTTONS */
.stButton > button {
    background: #e6d3a3 !important; 
    color: #1b4332 !important; 
    border-radius: 30px !important;
    font-weight: 600 !important;
    border: none !important;
    height: 50px !important;
    font-size: 1rem !important;
    max-width: 320px;
    margin: 0 auto;
    box-shadow: 0 10px 25px rgba(230,211,163,0.4) !important;
    transition: 0.3s !important;
}
.stButton > button:hover { 
    background: #d4c08f !important;
    transform: translateY(-3px) scale(1.02) !important;
}

/* METRICS */
[data-testid="metric-container"] { 
    background: #ffffff !important; 
    border-radius: 20px !important;
    border: 1px solid rgba(0,0,0,0.05) !important;
    color: #1f2933 !important;
    transition: 0.3s;
}
[data-testid="metric-container"]:hover {
    transform: translateY(-5px);
}

/* TEXT COLORS */
p, span, li {
    color: #4b5563 !important;
}

/* FORM SUCCESS */
.form-success { 
    background: #2d6a4f;
    color: #f5f1e8;
    padding: 4rem;
    border-radius: 30px;
    animation: luxuryFadeUp 1s ease;
}

/* FOOTER */
.footer { 
    background: #1b4332; 
    color: #e6d3a3; 
    padding: 5rem 3rem; 
    text-align: center; 
    border-radius: 30px 30px 0 0;
}

/* LINKS */
a {
    color: #e6d3a3 !important;
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
<style>
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 20px;
    background-color: #0e1117;
}

.title {
    font-size: 22px;
    font-weight: bold;
    color: white;
}

.nav button {
    background: none;
    border: none;
    color: white;
    font-size: 16px;
    margin-left: 20px;
    cursor: pointer;
    transition: 0.3s;
}

.nav button:hover {
    color: #00c8ff;
    transform: scale(1.1);
}
</style>
<div class="header-row">
    <div class="header-row">
    <div style="display:flex; align-items:center; justify-content:center; gap:15px;">
        <img src="{logo_url}" style="height:60px;">
        <div class="header-title">Niva Novus</div>
    </div>
    <div class="header-nav">
    </div>
</div>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"
# Layout
st.markdown('<div class="banner">', unsafe_allow_html=True)


b1, b2, b3, b4 = st.columns(4)

with b1:
    if st.button("🏠 Back to Home", key="contact_home", use_container_width=True):
        st.session_state.page = "Home"
        st.session_state.form_submitted = False
        st.rerun()

with b2:
    if st.button("👨‍💼 About",  key="nav_about", use_container_width=True):
        st.session_state.page = "About"
        st.session_state.form_submitted = False
        st.rerun()

with b3:
    if st.button("📦 View Packages", key="products_main", use_container_width=True):
        st.session_state.page = "Products"
        st.session_state.form_submitted = False
        st.rerun()
with b4:
    if st.button("💬 Contact", key="about_main", use_container_width=True):
        st.session_state.page = "Contact"
        st.session_state.form_submitted = False
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
    


# ----------------------
# FLOATING WHATSAPP BUTTON
# ----------------------
st.markdown("""
<style>
.whatsapp-float {
    position: fixed;
    bottom: 20px;
    left: 20px;
    z-index: 999;
}
.whatsapp-float a {
    text-decoration: none;
}
.whatsapp-float img {
    width: 60px;
    height: 60px;
}
</style>
<div class="whatsapp-float">
    <a href="https://wa.me/919359156648" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" />
    </a>
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
    st.markdown(
    '<h2 style="text-align:center; color:#1e3a8a; font-size:3rem; margin:5rem 0 4rem 0; font-weight:800;">Why Choose SmartNest?</h2>',
    unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card gradient-1 gradient-card">
            <span class="icon-large">🔒</span>
            <h3 style="font-size:2rem; margin-bottom:1.5rem;">Bank-Grade Security</h3>
            <p style="font-size:1.2rem; opacity:0.95; line-height:1.7;">End-to-end encryption<br><strong>Zero data leaks</strong> guaranteed</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔒 Learn More", key="home_learn_more", use_container_width=True):
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
    <h2 style="color:#1e3a8a; text-align:center; font-size:3.5rem; margin:4rem 0 2rem 0; font-weight:800;">About Niva Novus</h2>
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
    st.markdown("""
<h3 style="color:#1e3a8a; text-align:center; font-size:2.5rem; margin:5rem 0 3.5rem 0; font-weight:700;">Our Journey</h3>
""", unsafe_allow_html=True)

    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card gradient-2 gradient-card" style="height:300px; padding:3rem; display:flex; flex-direction:column; justify-content:space-between;">
            <span class="icon-large" style="font-size:4.5rem;">📅</span>
            <div style="margin-top:auto;">
                <h4 style="font-size:2rem; margin-bottom:0.5rem; font-weight:800;">2021</h4>
                <p style="font-size:1.25rem; opacity:0.95;">Founded in Nagpur</p>
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
<style>

/* GLASS CONTAINER */
.glass-container {
    max-width: 1100px;
    margin: 3rem auto;
    padding: 2rem;
    border-radius: 30px;

    background: color-mix(in srgb, var(--background-color) 85%, transparent);
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);

    border: 1px solid color-mix(in srgb, var(--text-color) 20%, transparent);

    box-shadow: 
        0 25px 60px rgba(0,0,0,0.3),
        inset 0 1px 0 color-mix(in srgb, white 20%, transparent);

    position: relative;
    overflow: hidden;
}

/* GLOW EFFECT */
.glass-container::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;

    background: linear-gradient(
        45deg,
        transparent,
        color-mix(in srgb, var(--text-color) 15%, transparent),
        transparent
    );

    transform: rotate(25deg);
    animation: shimmer 6s linear infinite;
}

/* TITLE */
.glass-title {
    text-align: center;
    font-size: 2.8rem;
    font-weight: 800;
    color: var(--text-color);
    margin-bottom: 1rem;
}

/* SUBTITLE */
.glass-subtitle {
    text-align: center;
    color: color-mix(in srgb, var(--text-color) 70%, transparent);
    font-size: 1.2rem;
    margin-bottom: 2rem;
}

/* IFRAME */
.glass-iframe {
    width: 100%;
    height: 750px;
    border: none;
    border-radius: 20px;

    background: color-mix(in srgb, var(--background-color) 95%, white 5%);

    box-shadow: 
        0 20px 40px rgba(0,0,0,0.25),
        inset 0 1px 0 color-mix(in srgb, white 20%, transparent);
}

/* ANIMATION */
@keyframes shimmer {
    0% { transform: translateX(-100%) rotate(25deg); }
    100% { transform: translateX(100%) rotate(25deg); }
}

</style>

<div class="glass-container">
    <div class="glass-title">🚀 Get Your Smart Home Quote</div>
    <div class="glass-subtitle">
        Fill the form below • Our experts will contact you within 24 hours
    </div>

   <iframe 
        src="https://docs.google.com/forms/d/e/1FAIpQLSdSpSEFMgm4sjIL6MaaLpb1Rf_b7TXuk_Pmu0gg4TErVFyirw/viewform?embedded=true" 
        width="100%" 
        height="2000" 
        frameborder="0" 
        marginheight="0" 
        marginwidth="0"
        style="border-radius:20px; box-shadow:0 20px 40px rgba(0,0,0,0.1);">
        Loading…
    </iframe>
</div>

""", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🏠 Back to Home", key="home_back", use_container_width=True):
            st.session_state.page = "Home"
            st.session_state.form_submitted = False
            st.rerun()
    with col2:
        if st.button("📦 View Packages", key="contact_products", use_container_width=True):
            st.session_state.page = "Products"
            st.session_state.form_submitted = False
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
    <h3 style="font-size:2.5rem; margin-bottom:1.5rem; font-weight:800;">🏠 Niva Novus</h3>
    <p style="font-size:1.3rem; opacity:0.95; margin-bottom:1.5rem;">
        Nagpur, Maharashtra, India | 
        <a href="mailto:info@smartnest.in" style="color:#60a5fa; text-decoration:none; font-weight:600;">📧 info@smartnest.in</a> | 
        📱 +91 98765 43210
    </p>
    <p style="font-size:1.1rem; opacity:0.8;">© 2026 All Rights Reserved | Making India Smarter, One Home at a Time</p>
</div>
""", unsafe_allow_html=True)
