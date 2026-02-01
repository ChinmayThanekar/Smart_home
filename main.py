import streamlit as st

# Page config
st.set_page_config(
    page_title="SmartNest Automation",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header { font-size: 3.5rem; color: #1e3a8a; text-align: center; margin-bottom: 1rem; }
    .sub-header { font-size: 1.8rem; color: #1e40af; text-align: center; margin-bottom: 2rem; }
    .hero-section { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; padding: 4rem 2rem; border-radius: 20px; text-align: center; }
    .feature-card { background: white; padding: 2rem; border-radius: 15px; 
                    box-shadow: 0 10px 30px rgba(0,0,0,0.1); text-align: center; height: 100%; }
    .product-card { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    color: white; padding: 2.5rem; border-radius: 15px; 
                    box-shadow: 0 15px 35px rgba(0,0,0,0.1); text-align: center; height: 100%; }
    .btn-primary { background: linear-gradient(45deg, #ff6b6b, #ff8e8e); 
                   border: none; padding: 12px 30px; border-radius: 25px; 
                   font-weight: bold; font-size: 1.1rem; color: white; }
    .btn-primary:hover { background: linear-gradient(45deg, #ff5252, #ff6b6b); }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for form
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

def main():
    # Header
    st.markdown('<h1 class="main-header">🏠 SmartNest Automation</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Transform Your Home into a Smart Haven</p>', unsafe_allow_html=True)
    
    # Navigation
    page = st.sidebar.selectbox("Navigate", ["Home", "About Us", "Products", "Share Interest"])
    
    if page == "Home":
        hero_section()
        
    elif page == "About Us":
        about_section()
        
    elif page == "Products":
        products_section()
        
    elif page == "Share Interest":
        contact_section()

def hero_section():
    # Full-width animated hero background
    st.markdown("""
    <style>
    .hero-bg {
        background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        height: 70vh;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: white;
        position: relative;
        overflow: hidden;
        border-radius: 0;
    }
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .hero-content {
        max-width: 1200px;
        padding: 2rem;
        z-index: 2;
    }
    .hero-title {
        font-size: 4.5rem;
        font-weight: 800;
        margin-bottom: 1.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        animation: fadeInUp 1s ease;
    }
    .hero-subtitle {
        font-size: 1.6rem;
        margin-bottom: 2.5rem;
        opacity: 0.95;
        animation: fadeInUp 1s ease 0.2s both;
    }
    .cta-button {
        background: linear-gradient(45deg, #ff6b6b, #ff8e8e);
        border: none;
        padding: 18px 40px;
        border-radius: 50px;
        font-size: 1.3rem;
        font-weight: 700;
        color: white;
        box-shadow: 0 10px 30px rgba(255,107,107,0.4);
        transition: all 0.3s ease;
        animation: fadeInUp 1s ease 0.4s both;
    }
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(255,107,107,0.6);
    }
    .floating-icons {
        position: absolute;
        width: 100%;
        height: 100%;
        overflow: hidden;
    }
    .icon {
        position: absolute;
        font-size: 2rem;
        animation: float 6s ease-in-out infinite;
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Hero section
    st.markdown("""
    <div class="hero-bg">
        <div class="floating-icons">
            <div class="icon" style="top:20%; left:10%; animation-delay: 0s;">💡</div>
            <div class="icon" style="top:60%; right:15%; animation-delay: 2s;">🔒</div>
            <div class="icon" style="bottom:20%; left:20%; animation-delay: 4s;">🎵</div>
            <div class="icon" style="top:30%; right:25%; animation-delay: 1s;">🌡️</div>
        </div>
        <div class="hero-content">
            <h1 class="hero-title">🏠 Transform Your Home</h1>
            <p class="hero-subtitle">Seamless Smart Home Automation • One Tap Control • Future-Proof Technology</p>
            <button class="cta-button" onclick="document.getElementById('products').scrollIntoView({behavior: 'smooth'})">
                🚀 Explore Smart Packages
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats row
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🏠", "10K+", "Homes Automated")
    with col2:
        st.metric("⭐", "4.9/5", "Customer Rating")
    with col3:
        st.metric("⚡", "99.9%", "Uptime")
    with col4:
        st.metric("🏢", "India", "Wide Coverage")
    
    # Feature showcase carousel effect
    st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #1e3a8a; font-size: 2.5rem; margin-bottom: 3rem;">Why SmartNest?</h2>', unsafe_allow_html=True)
    
    # Three main features with hover effects
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; 
            padding: 3rem 2rem; 
            border-radius: 20px; 
            text-align: center;
            height: 100%;
            transition: transform 0.3s ease;
            box-shadow: 0 20px 40px rgba(102,126,234,0.3);
        " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🔒</div>
            <h3 style="font-size: 1.8rem; margin-bottom: 1rem;">Bank-Grade Security</h3>
            <p>End-to-end encryption • Zero data leaks • Privacy-first design</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white; 
            padding: 3rem 2rem; 
            border-radius: 20px; 
            text-align: center;
            height: 100%;
            transition: transform 0.3s ease;
            box-shadow: 0 20px 40px rgba(240,147,251,0.3);
        " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🔗</div>
            <h3 style="font-size: 1.8rem; margin-bottom: 1rem;">Universal Integration</h3>
            <p>Alexa • Google Home • Apple HomeKit • 500+ devices</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white; 
            padding: 3rem 2rem; 
            border-radius: 20px; 
            text-align: center;
            height: 100%;
            transition: transform 0.3s ease;
            box-shadow: 0 20px 40px rgba(79,172,254,0.3);
        " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
            <div style="font-size: 4rem; margin-bottom: 1rem;">⚡</div>
            <h3 style="font-size: 1.8rem; margin-bottom: 1rem;">24/7 Expert Support</h3>
            <p>Installation • Troubleshooting • Lifetime assistance</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick action buttons
    st.markdown('<div style="height: 4rem;"></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; border-radius: 15px;">
            <h3 style="margin-bottom: 1rem;">Ready to Start?</h3>
            <button class="cta-button" onclick="document.getElementById('contact').scrollIntoView({behavior: 'smooth'})">
                💬 Share Your Interest Now
            </button>
        </div>
        """, unsafe_allow_html=True)


def about_section():
    st.markdown('<h2 style="color: #1e3a8a;">About SmartNest Automation</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("""
        We're a leading smart home automation company based in **Pimpri-Chinchwad, Maharashtra, India**, 
        dedicated to bringing cutting-edge technology to your doorstep.
        
        Our solutions integrate effortlessly with everyday devices, offering:
        - **Reliability**: Built to last with enterprise-grade components
        - **Security**: End-to-end encryption and privacy-first design  
        - **Convenience**: Voice control, app management, and automation rules
        """)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80")
    
    st.markdown("---")
    
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; border-radius: 15px;'>
        <h3>Ready to make your home smarter?</h3>
        <p>Transform your living space with our comprehensive automation solutions.</p>
    </div>
    """, unsafe_allow_html=True)

def products_section():
    st.markdown('<h2 style="color: #1e3a8a; text-align: center;">Our Full Home Automation Packages</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem;">Choose from our range of packages tailored for every need</p>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("""
        <div class="product-card">
            <h3>📦 Basic Package</h3>
            <p><strong>Essential controls for starters</strong></p>
            <ul style='text-align: left; padding-left: 1.5rem;'>
                <li>Smart lighting control</li>
                <li>Fan & appliance control</li>
                <li>Basic security sensors</li>
                <li>Mobile app access</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div class="product-card">
            <h3>⭐ Standard Package</h3>
            <p><strong>Advanced features for modern homes</strong></p>
            <ul style='text-align: left; padding-left: 1.5rem;'>
                <li>Climate control (AC)</li>
                <li>Multi-room audio</li>
                <li>Advanced security</li>
                <li>Voice assistant integration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("""
        <div class="product-card">
            <h3>👑 Premium Package</h3>
            <p><strong>Complete smart home ecosystem</strong></p>
            <ul style='text-align: left; padding-left: 1.5rem;'>
                <li>AI personalization</li>
                <li>Energy optimization</li>
                <li>Total home integration</li>
                <li>Custom automation rules</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<p style="text-align: center; margin-top: 3rem; font-size: 1.3rem;">Contact us to find the right fit for your home!</p>', unsafe_allow_html=True)

def contact_section():
    st.markdown('<h2 style="color: #1e3a8a;">Share Your Interest</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem;">Tell us about your project - we\'ll get back within 24 hours!</p>', unsafe_allow_html=True)
    
    with st.form("interest_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name", placeholder="Enter your name")
            email = st.text_input("Email", placeholder="your@email.com")
            phone = st.text_input("Phone Number", placeholder="+91 98765 43210")
        
        with col2:
            package = st.selectbox("Package Interest", 
                                 ["Select Package", "Basic Package", "Standard Package", "Premium Package"])
            home_size = st.selectbox("Home Size", ["1-2 BHK", "3 BHK", "4+ BHK", "Villa/Independent House"])
        
        message = st.text_area("Tell us about your home/project", 
                              placeholder="Any specific requirements or features you're looking for?")
        
        submitted = st.form_submit_button("🚀 Send Interest", use_container_width=True)
    
    if submitted and st.session_state.form_submitted == False:
        st.session_state.form_submitted = True
        st.success("🎉 Thank you for your interest! We'll contact you within 24 hours.")
        st.balloons()
        
        # Here you would typically save to database/email
        st.info("**Demo**: In production, this would send to your email/database.")
        st.markdown("**Submitted Details:**")
        details = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Package": package,
            "Home Size": home_size,
            "Message": message
        }
        st.json(details)
        
        if st.button("Submit Another Interest"):
            st.session_state.form_submitted = False
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem; color: #666;'>
    <p>© 2026 SmartNest Automation | Pimpri-Chinchwad, Maharashtra, India</p>
    <p>All rights reserved | <a href='mailto:info@smartnest.in' style='color: #1e3a8a;'>info@smartnest.in</a></p>
</div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
