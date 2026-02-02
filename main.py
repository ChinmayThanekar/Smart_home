import streamlit as st

# Page config
st.set_page_config(
    page_title="SmartNest Automation", 
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# PERFECTLY ALIGNED CSS
st.markdown("""
<style>
/* RESET & GLOBAL */
* { margin: 0; padding: 0; box-sizing: border-box; }
.main { padding: 1rem 2rem; }
h1, h2, h3 { margin-bottom: 1rem; }

/* HEADER */
.header-row { 
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); 
    padding: 1.5rem 2rem; 
    border-radius: 0 0 20px 20px;
    color: white;
    margin-bottom: 2rem;
}
.header-title { font-size: 2.5rem; font-weight: 800; text-align: center; }
.header-nav { display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; }

/* BUTTONS */
.btn-nav { 
    background: linear-gradient(45deg, #ff6b6b, #ff8e8e); 
    color: white; padding: 0.8rem 2rem; border-radius: 30px; 
    font-weight: 600; border: none; cursor: pointer; 
    box-shadow: 0 8px 25px rgba(255,107,107,0.3);
    transition: all 0.3s ease; font-size: 1rem;
}
.btn-nav:hover { transform: translateY(-2px); box-shadow: 0 12px 35px rgba(255,107,107,0.5); }
.btn-secondary { background: linear-gradient(45deg, #10b981, #34d399) !important; 
                 box-shadow: 0 8px 25px rgba(16,185,129,0.3) !important; }

/* CARDS */
.card { 
    background: white; padding: 2.5rem; border-radius: 20px; 
    box-shadow: 0 15px 35px rgba(0,0,0,0.08);
    border: 1px solid rgba(255,255,255,0.8); height: 100%;
    text-align: center; transition: all 0.3s ease;
}
.card:hover { transform: translateY(-8px); box-shadow: 0 25px 50px rgba(0,0,0,0.15); }
.gradient-card { color: white !important; }
.gradient-1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
.gradient-2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
.gradient-3 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
.gradient-4 { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }

/* HERO */
.hero-section { 
    background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c); 
    background-size: 400% 400%; animation: gradientShift 12s ease infinite;
    height: 70vh; display: flex; align-items: center; justify-content: center; 
    text-align: center; color: white; border-radius: 20px; margin: 2rem 0;
    position: relative; overflow: hidden;
}
@keyframes gradientShift { 0%{background-position:0%50%}50%{background-position:100%50%}100%{background-position:0%50%}}
.hero-content { max-width: 1000px; padding: 2rem; }

/* STATS */
.stats-row { display: flex; justify-content: space-around; margin: 3rem 0; }
.stat-item { text-align: center; }

/* FORM */
.form-row { display: flex; gap: 2rem; margin-bottom: 1.5rem; }
.form-section { flex: 1; }
.form-success { 
    background: linear-gradient(135deg, #10b981, #34d399); 
    color: white; padding: 3rem; border-radius: 20px; text-align: center; 
    box-shadow: 0 20px 40px rgba(16,185,129,0.3); margin: 2rem 0;
}

/* FOOTER */
.footer { 
    background: linear-gradient(135deg, #1e293b 0%, #334155 100%); 
    color: white; padding: 3rem 2rem; text-align: center; 
    border-radius: 20px 20px 0 0; margin-top: 4rem;
}
</style>
""", unsafe_allow_html=True)

# Session state
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# TOP NAVIGATION BAR
st.markdown("""
<div class="header-row">
    <div class="header-title">🏠 SmartNest Automation</div>
    <div class="header-nav">
        <button class="btn-nav" onclick="setPage('Home')">🏠 Home</button>
        <button class="btn-nav btn-secondary" onclick="setPage('About')">👨‍💼 About</button>
        <button class="btn-nav" onclick="setPage('Products')">📦 Products</button>
        <button class="btn-nav btn-secondary" onclick="setPage('Contact')">💬 Contact</button>
    </div>
</div>
""", unsafe_allow_html=True)

# SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("## 🚀 Quick Navigation")
    selected = st.selectbox("Go to page:", ["Home", "About", "Products", "Contact"], 
                          index=["Home", "About", "Products", "Contact"].index(st.session_state.page))
    if selected != st.session_state.page:
        st.session_state.page = selected
        st.rerun()

# MAIN CONTENT
if st.session_state.page == "Home":
    # HERO SECTION
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 1.5rem; text-shadow: 2px 2px 8px rgba(0,0,0,0.3);">
                Transform Your Home into Smart Haven
            </h1>
            <p style="font-size: 1.4rem; margin-bottom: 2.5rem; opacity: 0.95;">
                Seamless automation for modern Indian living
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # STATS ROW
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("🏠", "10K+", "Homes")
    with col2: st.metric("⭐", "4.9/5", "Rating")
    with col3: st.metric("⚡", "99.9%", "Uptime")
    with col4: st.metric("🏢", "50+", "Cities")
    
    # FEATURES
    st.markdown('<h2 style="text-align: center; color: #1e3a8a; margin: 3rem 0 2rem 0;">Why Choose SmartNest?</h2>')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card gradient-1 gradient-card">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🔒</div>
            <h3 style="font-size: 1.6rem;">Bank-Grade Security</h3>
            <p style="font-size: 1.1rem; opacity: 0.9;">End-to-end encryption</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Learn More", key="home_feat1", use_container_width=True):
            st.session_state.page = "About"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="card gradient-2 gradient-card">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🔗</div>
            <h3 style="font-size: 1.6rem;">Universal Integration</h3>
            <p style="font-size: 1.1rem; opacity: 0.9;">Alexa, Google Home, 500+ devices</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Packages", key="home_feat2", use_container_width=True):
            st.session_state.page = "Products"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="card gradient-3 gradient-card">
            <div style="font-size: 4rem; margin-bottom: 1rem;">⚡</div>
            <h3 style="font-size: 1.6rem;">24/7 Expert Support</h3>
            <p style="font-size: 1.1rem; opacity: 0.9;">Installation & troubleshooting</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Get Help", key="home_feat3", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()

elif st.session_state.page == "About":
    st.markdown('<h2 style="color: #1e3a8a; text-align: center; margin-bottom: 3rem;">About SmartNest Automation</h2>')
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="card gradient-1 gradient-card" style="height: 420px;">
            <div style="font-size: 4.5rem; margin-bottom: 1.5rem;">🏢</div>
            <h3 style="font-size: 1.8rem;">Pimpri-Chinchwad Experts</h3>
            <p style="font-size: 1.2rem; line-height: 1.6; opacity: 0.95;">
                5+ years serving Indian homes from Mumbai to Bangalore
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📦 View Our Packages", key="about_products", use_container_width=True):
            st.session_state.page = "Products"
            st.rerun()
    with col2:
        if st.button("💬 Free Consultation", key="about_contact", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()
    
    # Timeline
    st.markdown('<h3 style="color: #1e3a8a; text-align: center; margin: 3rem 0 2rem 0;">Our Journey</h3>')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card gradient-2 gradient-card" style="height: 200px;"><div style="font-size: 3rem;">📅</div><h4>2021</h4><p>Founded in Pune</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card gradient-3 gradient-card" style="height: 200px;"><div style="font-size: 3rem;">🚀</div><h4>2024</h4><p>10K homes automated</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card gradient-4 gradient-card" style="height: 200px;"><div style="font-size: 3rem;">🎯</div><h4>2026</h4><p>50K homes target</p></div>', unsafe_allow_html=True)

elif st.session_state.page == "Products":
    st.markdown('<h2 style="color: #1e3a8a; text-align: center; margin-bottom: 2rem;">Full Home Automation Packages</h2>')
    st.markdown('<p style="text-align: center; font-size: 1.3rem; color: #6b7280; margin-bottom: 3rem;">Tailored for every home size and lifestyle</p>')
    
    # Comparison Table
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card gradient-1 gradient-card" style="height: 380px;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">📦</div>
            <h3 style="font-size: 1.8rem;">Basic Package</h3>
            <p style="font-size: 1.3rem; opacity: 0.95;">1-2 BHK Apartments</p>
            <ul style="text-align: left; font-size: 1.1rem; margin: 1.5rem 0;">
                <li>✅ Smart lighting</li>
                <li>✅ Appliance control</li>
                <li>✅ Basic security</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("💬 Get Quote", key="prod_basic", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="card gradient-2 gradient-card" style="height: 380px;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">⭐</div>
            <h3 style="font-size: 1.8rem;">Standard Package</h3>
            <p style="font-size: 1.3rem; opacity: 0.95;">3 BHK & Villas</p>
            <ul style="text-align: left; font-size: 1.1rem; margin: 1.5rem 0;">
                <li>✅ Climate control</li>
                <li>✅ Curtain automation</li>
                <li>✅ Multi-room audio</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("💬 Get Quote", key="prod_standard", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="card gradient-3 gradient-card" style="height: 380px;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">👑</div>
            <h3 style="font-size: 1.8rem;">Premium Package</h3>
            <p style="font-size: 1.3rem; opacity: 0.95;">4+ BHK Luxury Homes</p>
            <ul style="text-align: left; font-size: 1.1rem; margin: 1.5rem 0;">
                <li>✅ AI personalization</li>
                <li>✅ Energy optimization</li>
                <li>✅ Full integration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("💬 Get Quote", key="prod_premium", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()

elif st.session_state.page == "Contact":
    # FIXED - Proper HTML rendering
    st.markdown("""
    <h2 style="color: #1e3a8a; text-align: center; margin-bottom: 1rem;">Share Your Interest</h2>
    <p style="text-align: center; font-size: 1.3rem; color: #6b7280; margin-bottom: 3rem;">Get personalized quote within 24 hours</p>
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
                name = st.text_input("👤 Full Name *", placeholder="Enter your name")
                email = st.text_input("📧 Email *", placeholder="your@email.com")
                phone = st.text_input("📱 Phone", placeholder="+91 98765 43210")
            with col2:
                package = st.selectbox("📦 Package Interest", ["Basic Package", "Standard Package", "Premium Package"])
                home_type = st.selectbox("🏠 Home Type", ["1-2 BHK", "3 BHK", "4+ BHK", "Villa/Independent"])
            
            message = st.text_area("💬 Project Details", 
                                 placeholder="Home size? Special requirements? Current setup?", height=100)
            
            col1, col2 = st.columns(2)
            submitted = col1.form_submit_button("🚀 Send Interest", use_container_width=True)
            
            if submitted:
                st.session_state.form_submitted = True
                st.rerun()
    
    if st.session_state.form_submitted:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #10b981, #34d399); color:white; padding:3rem; 
                    border-radius:20px; text-align:center; box-shadow:0 20px 40px rgba(16,185,129,0.3); margin:2rem 0;'>
            <div style='font-size:4rem; margin-bottom:1rem;'>🎉</div>
            <h2 style='font-size:2.2rem; margin-bottom:1rem;'>Thank You!</h2>
            <p style='font-size:1.3rem;'>We'll contact you within <strong>24 hours</strong> with your personalized quote.</p>
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
            "Message": message if 'message' in locals() else ""
        }
        st.json(details)


# PERFECT FOOTER
st.markdown("""
<div class="footer">
    <h3 style="margin-bottom: 1rem;">🏠 SmartNest Automation</h3>
    <p style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 1rem;">
        Pimpri-Chinchwad, Maharashtra, India | 
        <a href="mailto:info@smartnest.in" style="color: #60a5fa;">📧 info@smartnest.in</a> | 
        📱 +91 98765 43210
    </p>
    <p style="opacity: 0.8;">© 2026 All Rights Reserved | Making India Smarter, One Home at a Time</p>
</div>
""", unsafe_allow_html=True)
