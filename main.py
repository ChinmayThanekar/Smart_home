import streamlit as st

# Page config
st.set_page_config(
    page_title="SmartNest Automation",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# COMPLETE Enhanced Custom CSS (ALL animations fixed)
st.markdown("""
<style>
/* Global Styles */
.main-header { font-size: 3.8rem; color: #1e3a8a; text-align: center; margin-bottom: 1rem; font-weight: 800; }
.sub-header { font-size: 2rem; color: #1e40af; text-align: center; margin-bottom: 2.5rem; }
.section-title { font-size: 2.8rem; color: #1e3a8a; text-align: center; margin-bottom: 3rem; font-weight: 700; }

/* Cards */
.card { 
    padding: 2.5rem; border-radius: 25px; text-align: center; height: 100%; 
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}
.card:hover { transform: translateY(-15px) scale(1.02); box-shadow: 0 30px 60px rgba(0,0,0,0.2); }

/* Gradients */
.gradient-1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
.gradient-2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; }
.gradient-3 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; }
.gradient-4 { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); color: white; }
.gradient-5 { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); color: white; }

/* Buttons */
.cta-btn, .cta-button { 
    background: linear-gradient(45deg, #ff6b6b, #ff8e8e); border: none; padding: 16px 40px; 
    border-radius: 50px; font-size: 1.2rem; font-weight: 700; color: white; 
    box-shadow: 0 10px 30px rgba(255,107,107,0.4); transition: all 0.3s ease;
    text-decoration: none; display: inline-block;
}
.cta-btn:hover, .cta-button:hover { transform: translateY(-3px); box-shadow: 0 15px 40px rgba(255,107,107,0.6); }

/* Stats */
.stat-card { background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); border-radius: 20px; padding: 2rem; text-align: center; border: 1px solid rgba(255,255,255,0.2); }

/* HERO ANIMATIONS - FIXED */
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
}
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.floating-icons { position: absolute; width: 100%; height: 100%; overflow: hidden; }
.icon { position: absolute; font-size: 2rem; animation: float 6s ease-in-out infinite; }
@keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(180deg); }
}
.hero-title { font-size: 4.5rem; font-weight: 800; margin-bottom: 1.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
.hero-subtitle { font-size: 1.6rem; margin-bottom: 2.5rem; opacity: 0.95; }
.hero-content { max-width: 1200px; padding: 2rem; z-index: 2; }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

def main():
    st.markdown('<h1 class="main-header">🏠 SmartNest Automation</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">India\'s Premier Smart Home Solutions</p>', unsafe_allow_html=True)
    
    page = st.sidebar.selectbox("Navigate", ["🏠 Home", "👨‍💼 About Us", "📦 Products", "💬 Share Interest"])
    
    if page == "🏠 Home":
        hero_section()
    elif page == "👨‍💼 About Us":
        about_section()
    elif page == "📦 Products":
        products_section()
    elif page == "💬 Share Interest":
        contact_section()

# 🔥 PERFECT HERO SECTION (All animations working)
def hero_section():
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
            <a href="#products" class="cta-button">🚀 Explore Smart Packages</a>
            <a href="#contact" class="cta-button" style="background: linear-gradient(45deg, #43e97b, #38f9d7); margin-left: 1rem;">💬 Get Free Quote</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats row
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("🏠", "10K+", "Homes Automated")
    with col2: st.metric("⭐", "4.9/5", "Customer Rating")
    with col3: st.metric("⚡", "99.9%", "Uptime")
    with col4: st.metric("🏢", "India", "Wide Coverage")
    
    # Feature showcase
    st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #1e3a8a; font-size: 2.5rem; margin-bottom: 3rem;">Why SmartNest?</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="card gradient-1" style="height: 100%;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🔒</div>
            <h3 style="font-size: 1.8rem; margin-bottom: 1rem;">Bank-Grade Security</h3>
            <p>End-to-end encryption • Zero data leaks • Privacy-first design</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card gradient-2" style="height: 100%;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🔗</div>
            <h3 style="font-size: 1.8rem; margin-bottom: 1rem;">Universal Integration</h3>
            <p>Alexa • Google Home • Apple HomeKit • 500+ devices</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card gradient-3" style="height: 100%;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">⚡</div>
            <h3 style="font-size: 1.8rem; margin-bottom: 1rem;">24/7 Expert Support</h3>
            <p>Installation • Troubleshooting • Lifetime assistance</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick action
    st.markdown('<div style="height: 4rem;"></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 2.5rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 20px;">
            <h3 style="margin-bottom: 1.5rem;">Ready to Start?</h3>
            <a href="#contact" class="cta-button" style="background: linear-gradient(45deg, #43e97b, #38f9d7);">💬 Share Your Interest Now</a>
        </div>
        """, unsafe_allow_html=True)

# 🔥 ABOUT SECTION
def about_section():
    st.markdown('<h2 class="section-title">About SmartNest Automation</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown("""
        <div class="card gradient-1" style="height: 500px;">
            <div style="font-size: 5rem; margin-bottom: 1.5rem;">🏢</div>
            <h3 style="font-size: 2.2rem; margin-bottom: 1.5rem;">Pimpri-Chinchwad's Smart Home Experts</h3>
            <p style="font-size: 1.2rem; line-height: 1.8;">
                5+ years bringing <strong>cutting-edge automation</strong> to Indian homes. 
                From Mumbai apartments to Bangalore villas, we make smart living accessible.
            </p>
            <ul style="text-align: left; font-size: 1.1rem; margin-top: 2rem;">
                <li>✅ 100% Indian engineering team</li>
                <li>✅ Local service across 50+ cities</li>
                <li>✅ Enterprise-grade reliability</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&fit=crop&w=800&q=80", 
                use_column_width=True, caption="Modern Indian Smart Homes")
    
    st.markdown("---")
    st.markdown('<h3 style="text-align:center; color:#1e3a8a; font-size:2.2rem;">Our Journey</h3>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div class="card gradient-2" style="height:280px;">
            <div style="font-size:3.5rem;">📅</div>
            <h4 style="margin:1rem 0;">2021</h4>
            <p><strong>Founded</strong> in Pune with mission to automate 1M homes</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div class="card gradient-3" style="height:280px;">
            <div style="font-size:3.5rem;">🚀</div>
            <h4 style="margin:1rem 0;">2024</h4>
            <p><strong>10K homes</strong> automated across India</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div class="card gradient-4" style="height:280px;">
            <div style="font-size:3.5rem;">🎯</div>
            <h4 style="margin:1rem 0;">2026</h4>
            <p><strong>50K homes</strong> target this year</p>
        </div>
        """, unsafe_allow_html=True)

# 🔥 PRODUCTS SECTION
def products_section():
    st.markdown('<h2 class="section-title" id="products">Full Home Automation Packages</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size:1.4rem; color:#6b7280; max-width:800px; margin:0 auto 3rem;">Tailored solutions for every home, apartment, and lifestyle</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="overflow-x:auto; margin:3rem 0;">
    <table style="width:100%; border-collapse:collapse; background:white; border-radius:20px; overflow:hidden; box-shadow:0 20px 40px rgba(0,0,0,0.1);">
        <thead>
            <tr style="background:linear-gradient(135deg,#667eea 0%,#764ba2 100%); color:white;">
                <th style="padding:2rem 1rem; text-align:center; font-size:1.3rem;"></th>
                <th style="padding:2rem 1rem; text-align:center; font-size:1.3rem;"><div style="font-size:3rem;">📦</div><br>Basic</th>
                <th style="padding:2rem 1rem; text-align:center; font-size:1.3rem;"><div style="font-size:3rem;">⭐</div><br>Standard</th>
                <th style="padding:2rem 1rem; text-align:center; font-size:1.3rem;"><div style="font-size:3rem;">👑</div><br>Premium</th>
            </tr>
        </thead>
        <tbody>
            <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:1.5rem; font-weight:600; background:#f8fafc;">Smart Lighting</td><td style="padding:1.5rem; text-align:center;">✅</td><td style="padding:1.5rem; text-align:center;">✅</td><td style="padding:1.5rem; text-align:center;">✅</td></tr>
            <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:1.5rem; font-weight:600; background:#f8fafc;">Appliance Control</td><td style="padding:1.5rem; text-align:center;">✅</td><td style="padding:1.5rem; text-align:center;">✅</td><td style="padding:1.5rem; text-align:center;">✅</td></tr>
            <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:1.5rem; font-weight:600; background:#f8fafc;">Security Sensors</td><td style="padding:1.5rem; text-align:center;">Basic</td><td style="padding:1.5rem; text-align:center;">✅</td><td style="padding:1.5rem; text-align:center;">✅ Pro</td></tr>
            <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:1.5rem; font-weight:600; background:#f8fafc;">Climate Control</td><td style="padding:1.5rem; text-align:center;">❌</td><td style="padding:1.5rem; text-align:center;">✅</td><td style="padding:1.5rem; text-align:center;">✅ Smart</td></tr>
            <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:1.5rem; font-weight:600; background:#f8fafc;">Voice Assistant</td><td style="padding:1.5rem; text-align:center;">✅</td><td style="padding:1.5rem; text-align:center;">✅ Multi</td><td style="padding:1.5rem; text-align:center;">✅ AI</td></tr>
            <tr style="border-bottom:1px solid #e5e7eb;"><td style="padding:1.5rem; font-weight:600; background:#f8fafc;">Energy Analytics</td><td style="padding:1.5rem; text-align:center;">❌</td><td style="padding:1.5rem; text-align:center;">Basic</td><td style="padding:1.5rem; text-align:center;">✅ Advanced</td></tr>
        </tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(3)
    with cols[0]:
        st.markdown("""
        <div class="card gradient-1" style="height:350px;">
            <div style="font-size:5rem;">📦</div>
            <h3 style="font-size:2rem;">Perfect for Starters</h3>
            <p style="font-size:1.2rem;">1-2 BHK apartments</p>
            <ul style="text-align:left; font-size:1.1rem;">
                <li>Essential lighting control</li>
                <li>Fan & geyser automation</li>
                <li>Basic door sensors</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div class="card gradient-2" style="height:350px;">
            <div style="font-size:5rem;">⭐</div>
            <h3 style="font-size:2rem;">Modern Family Homes</h3>
            <p style="font-size:1.2rem;">3 BHK & Villas</p>
            <ul style="text-align:left; font-size:1.1rem;">
                <li>AC climate control</li>
                <li>Curtain automation</li>
                <li>Multi-room audio</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("""
        <div class="card gradient-3" style="height:350px;">
            <div style="font-size:5rem;">👑</div>
            <h3 style="font-size:2rem;">Luxury Smart Ecosystem</h3>
            <p style="font-size:1.2rem;">4+ BHK Luxury Homes</p>
            <ul style="text-align:left; font-size:1.1rem;">
                <li>AI learning system</li>
                <li>Energy optimization</li>
                <li>Full home integration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# 🔥 CONTACT SECTION
def contact_section():
    st.markdown('<h2 class="section-title" id="contact">Share Your Interest</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size:1.4rem; color:#6b7280;">Get your personalized quote within 24 hours • 100% free consultation</p>', unsafe_allow_html=True)
    
    with st.form("interest_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("👤 Full Name", placeholder="Enter your name")
            email = st.text_input("📧 Email", placeholder="your@email.com")
            phone = st.text_input("📱 Phone", placeholder="+91 98765 43210")
        with col2:
            package = st.selectbox("📦 Package Interest", ["Basic Package", "Standard Package", "Premium Package"])
            home_type = st.selectbox("🏠 Home Type", ["1-2 BHK", "3 BHK", "4+ BHK", "Villa/Independent"])
            budget_range = st.selectbox("💰 Budget Range", ["Economy", "Mid-Range", "Premium", "Discuss"])
        
        col1, col2 = st.columns([2,1])
        with col1:
            message = st.text_area("💬 Project Details", 
                                 placeholder="Home size? Special requirements? Current setup?", height=120)
        with col2:
            st.markdown('<div style="height:100px;"></div>', unsafe_allow_html=True)
        
        st.markdown('<div style="text-align:center; margin-top:2rem;">', unsafe_allow_html=True)
        submitted = st.form_submit_button("🚀 Send My Interest", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    if 'submitted' in locals() and submitted and not st.session_state.form_submitted:
        st.session_state.form_submitted = True
        st.markdown("""
        <div style='background: linear-gradient(135deg, #10b981, #34d399); color:white; padding:3rem; 
                    border-radius:25px; text-align:center; box-shadow:0 20px 40px rgba(16,185,129,0.3);'>
            <div style='font-size:5rem;'>🎉</div>
            <h2 style='font-size:2.5rem; margin:1rem 0;'>Thank You!</h2>
            <p style='font-size:1.3rem;'>We'll contact you within <strong>24 hours</strong> with your personalized quote.</p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
        
        st.markdown("**📋 Your Details:**")
        details = {"Name": name, "Email": email, "Phone": phone, "Package": package, 
                  "Home": home_type, "Budget": budget_range, "Message": message}
        st.json(details)

# PERFECT FOOTER
st.markdown("""
<hr style='border: none; height: 2px; background: linear-gradient(90deg, transparent, #667eea, #764ba2, transparent); margin: 4rem 0;'>

<div style='text-align:center; padding:4rem 2rem; background:linear-gradient(135deg,#1e293b 0%,#334155 100%); color:white; border-radius:25px 25px 0 0;'>
    <h3 style='font-size:2.2rem; margin-bottom:1rem;'>🏠 SmartNest Automation</h3>
    <p style='font-size:1.2rem; opacity:0.9;'>Pimpri-Chinchwad, Maharashtra, India | 
    <a href="mailto:info@smartnest.in" style="color:#60a5fa; text-decoration:none;">📧 info@smartnest.in</a> | 
    📱 +91 98765 43210</p>
    <p style='margin-top:2rem; opacity:0.8;'>© 2026 All Rights Reserved | Making India Smarter, One Home at a Time</p>
</div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
