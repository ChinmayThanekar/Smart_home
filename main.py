import streamlit as st

# Page config
st.set_page_config(
    page_title="SmartNest Automation",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# PERFECT CSS - Streamlit Native Navigation
st.markdown("""
<style>
.main-header { font-size: 3.8rem; color: #1e3a8a; text-align: center; margin-bottom: 1rem; font-weight: 800; }
.sub-header { font-size: 2rem; color: #1e40af; text-align: center; margin-bottom: 2.5rem; }
.section-title { font-size: 2.8rem; color: #1e3a8a; text-align: center; margin-bottom: 3rem; font-weight: 700; }
.card { padding: 2.5rem; border-radius: 25px; text-align: center; height: 100%; 
        transition: all 0.4s ease; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
.card:hover { transform: translateY(-10px); box-shadow: 0 30px 60px rgba(0,0,0,0.2); }
.gradient-1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
.gradient-2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; }
.gradient-3 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; }
.gradient-4 { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); color: white; }
.btn-nav { background: linear-gradient(45deg, #ff6b6b, #ff8e8e); color: white; padding: 12px 24px; 
           border-radius: 25px; text-decoration: none; font-weight: 600; display: inline-block; 
           margin: 0.5rem; box-shadow: 0 5px 15px rgba(255,107,107,0.4); }
.btn-nav:hover { transform: translateY(-2px); box-shadow: 0 10px 25px rgba(255,107,107,0.6); }
.btn-secondary { background: linear-gradient(45deg, #43e97b, #38f9d7) !important; 
                 box-shadow: 0 5px 15px rgba(67,233,123,0.4) !important; }
.hero-bg { background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c); 
           background-size: 400% 400%; animation: gradientShift 15s ease infinite; 
           height: 70vh; display: flex; align-items: center; justify-content: center; 
           text-align: center; color: white; position: relative; }
@keyframes gradientShift { 0%{background-position:0%50%}50%{background-position:100%50%}100%{background-position:0%50%} }
</style>
""", unsafe_allow_html=True)

# Session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# TOP NAVIGATION BAR (Always visible)
def render_top_nav():
    col1, col2, col3, col4, col5 = st.columns([1,1,2,1,1])
    with col2:
        st.markdown('<h1 style="margin:0; color:#1e3a8a;">🏠 SmartNest Automation</h1>', unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div style="display:flex; gap:1rem; justify-content:center;">
            <a href="#" onclick="setPage('Home')" class="btn-nav">🏠 Home</a>
            <a href="#" onclick="setPage('About')" class="btn-nav btn-secondary">👨‍💼 About</a>
            <a href="#" onclick="setPage('Products')" class="btn-nav">📦 Products</a>
            <a href="#" onclick="setPage('Contact')" class="btn-nav btn-secondary">💬 Contact</a>
        </div>
        """, unsafe_allow_html=True)

# MAIN NAVIGATION
def main():
    # Top navigation
    render_top_nav()
    
    # Sidebar + Main content
    col1, col2 = st.columns([0.25, 1])
    with col1:
        st.sidebar.markdown("## 🚀 Navigate")
        selected = st.sidebar.selectbox("Go to", ["Home", "About", "Products", "Contact"], 
                                      index=["Home", "About", "Products", "Contact"].index(st.session_state.page))
        if selected != st.session_state.page:
            st.session_state.page = selected
            st.rerun()
    
    with col2:
        if st.session_state.page == "Home":
            home_page()
        elif st.session_state.page == "About":
            about_page()
        elif st.session_state.page == "Products":
            products_page()
        elif st.session_state.page == "Contact":
            contact_page()

# HOME PAGE
def home_page():
    # Hero
    st.markdown("""
    <div class="hero-bg">
        <div style="max-width:1200px; padding:2rem;">
            <h1 style="font-size:4.5rem; font-weight:800; margin-bottom:1.5rem; text-shadow:2px 2px 4px rgba(0,0,0,0.3);">
                Transform Your Home into Smart Haven
            </h1>
            <p style="font-size:1.6rem; margin-bottom:2.5rem; opacity:0.95;">
                Control lights, security, climate with one tap
            </p>
            <div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
                """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Explore Packages", key="home_products", use_container_width=True):
            st.session_state.page = "Products"
            st.rerun()
    with col2:
        if st.button("💬 Get Free Quote", key="home_contact", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()
    
    st.markdown("""
            </div>
            <p style="margin-top:2rem; font-size:1.1rem;">
                Trusted by <strong>10K+ Indian homes</strong> | 
                <a href="#" onclick="setPage('About')" style="color:#fff;">Learn our story →</a>
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("🏠", "10K+", "Homes")
    with col2: st.metric("⭐", "4.9/5", "Rating")
    with col3: st.metric("⚡", "99.9%", "Uptime")
    with col4: st.metric("🏢", "50+", "Cities")
    
    # Features
    st.markdown('<h2 style="text-align:center; color:#1e3a8a;">Why SmartNest?</h2>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card gradient-1">
            <div style="font-size:4rem;">🔒</div>
            <h3>Bank-Grade Security</h3>
            <p>End-to-end encryption</p>
            """, unsafe_allow_html=True)
        if st.button("Learn More", key="feat1"):
            st.session_state.page = "About"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="card gradient-2">
            <div style="font-size:4rem;">🔗</div>
            <h3>Universal Integration</h3>
            <p>Alexa, Google Home, 500+ devices</p>
            """, unsafe_allow_html=True)
        if st.button("See Packages", key="feat2"):
            st.session_state.page = "Products"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="card gradient-3">
            <div style="font-size:4rem;">⚡</div>
            <h3>24/7 Support</h3>
            <p>Installation & troubleshooting</p>
            """, unsafe_allow_html=True)
        if st.button("Contact Us", key="feat3"):
            st.session_state.page = "Contact"
            st.rerun()

# ABOUT PAGE
def about_page():
    st.markdown('<h2 style="color:#1e3a8a;">About SmartNest Automation</h2>')
    
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown("""
        <div class="card gradient-1" style="height:450px;">
            <div style="font-size:5rem;">🏢</div>
            <h3>Pimpri-Chinchwad Experts</h3>
            <p>5+ years serving Indian homes from Mumbai to Bangalore</p>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📦 Our Packages", key="about_products"):
                st.session_state.page = "Products"
                st.rerun()
        with col2:
            if st.button("💬 Talk to Us", key="about_contact"):
                st.session_state.page = "Contact"
                st.rerun()
    
    with col2:
        st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?fit=crop&w=800&q=80")
    
    st.markdown("---")
    st.subheader("Our Journey")
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown('<div class="card gradient-2"><h4>2021</h4><p>Founded in Pune</p></div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="card gradient-3"><h4>2024</h4><p>10K homes automated</p></div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="card gradient-4"><h4>2026</h4><p>50K homes target</p></div>', unsafe_allow_html=True)

# PRODUCTS PAGE  
def products_page():
    st.markdown('<h2 style="color:#1e3a8a;">Full Home Automation Packages</h2>')
    
    # Comparison table
    st.markdown("""
    <table style="width:100%; border-collapse:collapse; background:white; border-radius:20px; box-shadow:0 20px 40px rgba(0,0,0,0.1);">
    <tr style="background:linear-gradient(135deg,#667eea 0%,#764ba2 100%); color:white;">
        <th>Feature</th><th>📦 Basic</th><th>⭐ Standard</th><th>👑 Premium</th>
    </tr>
    <tr><td>Smart Lighting</td><td>✅</td><td>✅</td><td>✅</td></tr>
    <tr><td>Appliance Control</td><td>✅</td><td>✅</td><td>✅</td></tr>
    <tr><td>Security Sensors</td><td>Basic</td><td>✅</td><td>✅ Pro</td></tr>
    <tr><td>Climate Control</td><td>❌</td><td>✅</td><td>✅ Smart</td></tr>
    </table>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card gradient-1">
            <div style="font-size:5rem;">📦</div>
            <h3>Basic Package</h3>
            <p>1-2 BHK apartments</p>
            """, unsafe_allow_html=True)
        if st.button("💬 Get Quote", key="prod1"):
            st.session_state.page = "Contact"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="card gradient-2">
            <div style="font-size:5rem;">⭐</div>
            <h3>Standard Package</h3>
            <p>3 BHK & Villas</p>
            """, unsafe_allow_html=True)
        if st.button("💬 Get Quote", key="prod2"):
            st.session_state.page = "Contact"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="card gradient-3">
            <div style="font-size:5rem;">👑</div>
            <h3>Premium Package</h3>
            <p>4+ BHK Luxury</p>
            """, unsafe_allow_html=True)
        if st.button("💬 Get Quote", key="prod3"):
            st.session_state.page = "Contact"
            st.rerun()

# CONTACT PAGE
def contact_page():
    st.markdown('<h2 style="color:#1e3a8a;">Share Your Interest</h2>')
    st.info("📧 We'll respond within 24 hours!")
    
    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False
    
    if not st.session_state.form_submitted:
        with st.form("interest_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("👤 Full Name")
                email = st.text_input("📧 Email")
                phone = st.text_input("📱 Phone")
            with col2:
                package = st.selectbox("📦 Package", ["Basic", "Standard", "Premium"])
                home_type = st.selectbox("🏠 Home Type", ["1-2 BHK", "3 BHK", "Villa"])
            
            message = st.text_area("💬 Project Details")
            col1, col2 = st.columns(2)
            with col1:
                submitted = st.form_submit_button("🚀 Send Interest")
            
            if submitted:
                st.session_state.form_submitted = True
                st.rerun()
    
    if st.session_state.form_submitted:
        st.success("🎉 Thank you! We'll contact you within 24 hours!")
        st.balloons()
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🏠 Back to Home"):
                st.session_state.page = "Home"
                st.session_state.form_submitted = False
                st.rerun()
        with col2:
            if st.button("📦 View Packages"):
                st.session_state.page = "Products"
                st.session_state.form_submitted = False
                st.rerun()

# Footer
st.markdown("""
<div style='text-align:center; padding:3rem; background:linear-gradient(135deg,#1e293b 0%,#334155 100%); color:white; margin-top:4rem;'>
    <h3>🏠 SmartNest Automation</h3>
    <p>Pimpri-Chinchwad, Maharashtra | 📧 info@smartnest.in | 📱 +91 98765 43210</p>
    <p>© 2026 All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
