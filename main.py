import streamlit as st
import pandas as pd
from streamlit_faker import faker  # Optional: for demo form submissions

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
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="hero-section">
            <h2 style='font-size: 2.5rem; margin-bottom: 1rem;'>Seamless Smart Home Automation</h2>
            <p style='font-size: 1.3rem; margin-bottom: 2rem;'>Control lights, security, climate, and more with one tap. 
            Experience modern living with cutting-edge technology.</p>
            <button class='btn-primary'>Explore Packages</button>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("![Smart Home](https://images.unsplash.com/photo-1558618047-3c8c76ca6e71?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80)")
    
    st.markdown("---")
    
    # Features
    st.markdown('<h2 style="text-align: center; color: #1e3a8a;">Why Choose SmartNest?</h2>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div class="feature-card">
            <h3>🔒 Secure & Reliable</h3>
            <p>Bank-grade encryption protects your home data and devices 24/7.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div class="feature-card">
            <h3>🔗 Easy Integration</h3>
            <p>Works seamlessly with Alexa, Google Home, and all major smart devices.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("""
        <div class="feature-card">
            <h3>🛠️ 24/7 Support</h3>
            <p>Expert team available anytime to assist with installation and troubleshooting.</p>
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
