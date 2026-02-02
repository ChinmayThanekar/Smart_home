import streamlit as st

# Page config
st.set_page_config(
    page_title="AICM Marketplace", 
    page_icon="🪙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# YOUR SAME PERFECT CSS - ENHANCED FOR MARKETPLACE
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }

body { background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 100%); color: #e2e8f0; }

@keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
@keyframes float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-15px); } }
@keyframes gradientShift { 0%{background-position:0%50%}50%{background-position:100%50%}100%{background-position:0%50%} }

.header-row { 
    background: linear-gradient(135deg, #8b5cf6 0%, #3b82f6 50%, #10b981 100%); 
    padding: 1.5rem 2rem; border-radius: 0 0 20px 20px; color: white; 
    box-shadow: 0 10px 30px rgba(139,92,246,0.4);
}
.header-title { font-size: 2.2rem; font-weight: 800; text-align: center; margin-bottom: 1rem; }
.header-nav { display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; }

.hero-section { 
    background: linear-gradient(-45deg, #8b5cf6, #ec4899, #10b981, #f59e0b); 
    background-size: 400% 400%; animation: gradientShift 12s ease infinite; 
    min-height: 500px; border-radius: 20px; margin: 2rem 0; display: flex; 
    align-items: center; justify-content: center; text-align: center; color: white;
    box-shadow: 0 20px 40px rgba(139,92,246,0.3);
}
.hero-content { max-width: 1000px; padding: 2rem; }

.card-container { display: flex; align-items: stretch; height: 480px; margin-bottom: 2rem; }
.card { 
    flex: 1; background: rgba(20,20,40,0.9); backdrop-filter: blur(20px); 
    padding: 3rem 2rem; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.3);
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
    background: rgba(20,20,40,0.9) !important; padding: 1.5rem !important; 
    border-radius: 15px !important; box-shadow: 0 10px 25px rgba(0,0,0,0.3) !important;
    border: 1px solid rgba(139,92,246,0.2) !important;
}

.form-success { background: linear-gradient(135deg, #10b981, #34d399); color: white; 
    padding: 3rem; border-radius: 20px; text-align: center; box-shadow: 0 20px 40px rgba(16,185,129,0.3); }

.footer { background: linear-gradient(135deg, #0f0f23 0%, #1e1b4b 100%); color: #e2e8f0; 
    padding: 3rem 2rem; text-align: center; border-radius: 20px 20px 0 0; margin-top: 4rem; 
    border-top: 1px solid rgba(139,92,246,0.2); }
</style>
""", unsafe_allow_html=True)

# Session state
if 'page' not in st.session_state:
    st.session_state.page = "Marketplace"
if 'wallet_connected' not in st.session_state:
    st.session_state.wallet_connected = False
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# HEADER - AICM STYLE
st.markdown("""
<div class="header-row">
    <div class="header-title">🪙 AICM Marketplace</div>
    <div style="text-align:center; font-size:1.1rem;">
        AI Crypto Services • Trading Bots • Signals • Token Tools
    </div>
</div>
""", unsafe_allow_html=True)

# SIDEBAR - MARKETPLACE NAV
with st.sidebar:
    st.markdown("## 🛒 Quick Navigation")
    selected = st.selectbox("Browse:", ["Marketplace", "Vendors", "Create Listing", "Wallet"], 
                          index=["Marketplace", "Vendors", "Create Listing", "Wallet"].index(st.session_state.page))
    if selected != st.session_state.page:
        st.session_state.page = selected
        st.rerun()
    
    st.markdown("---")
    if st.button("🔗 Connect Wallet", key="wallet_btn"):
        st.session_state.wallet_connected = True
        st.rerun()
    
    if st.session_state.wallet_connected:
        st.success("✅ Wallet Connected")
        st.caption("0x1234...abcd • 2.5 ETH")
    
    st.markdown("---")
    st.markdown("*Pimpri-Chinchwad, India*")

# MAIN CONTENT
if st.session_state.page == "Marketplace":
    # Hero - AICM Style
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 1.5rem; text-shadow: 2px 2px 8px rgba(0,0,0,0.5);">AI-Powered Crypto Services</h1>
            <p style="font-size: 1.4rem; margin-bottom: 2.5rem;">Trading bots • Signal services • Token analysis • Smart contracts</p>
            <div style="font-size: 1.8rem; background: rgba(255,255,255,0.2); padding: 1rem 2rem; border-radius: 50px; display: inline-block;">
                🔴 Live: 1,247 Services • $2.4M Volume
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Marketplace Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("🪙", "1,247", "+43")
    with col2: st.metric("⭐", "4.8/5", "+0.1")
    with col3: st.metric("💰", "$2.4M", "+12%")
    with col4: st.metric("👥", "89", "+5")
    
    # Featured Categories - AICM Style
    st.markdown('<h2 style="text-align:center; color:#8b5cf6; font-size:2.5rem; margin:3rem 0;">Hot Categories</h2>')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card gradient-1 gradient-card">
            <span class="icon-large">🤖</span>
            <h3 style="font-size:1.6rem;">Trading Bots</h3>
            <p>Automated strategies</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Browse Bots", key="market1")
    
    with col2:
        st.markdown("""
        <div class="card gradient-2 gradient-card">
            <span class="icon-large">📡</span>
            <h3 style="font-size:1.6rem;">Signals</h3>
            <p>Premium calls</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("View Signals", key="market2")
    
    with col3:
        st.markdown("""
        <div class="card gradient-3 gradient-card">
            <span class="icon-large">⚡</span>
            <h3 style="font-size:1.6rem;">Token Tools</h3>
            <p>Analysis & scanners</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Explore Tools", key="market3")

elif st.session_state.page == "Vendors":
    st.markdown('<h2 style="color:#8b5cf6; text-align:center; font-size:2.8rem; margin:3rem 0;">Top Vendors</h2>')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card-container">
            <div class="card gradient-1 gradient-card">
                <span class="icon-large">🦅</span>
                <h3>AlphaSignals</h3>
                <p>247 Sales • 4.9⭐</p>
                <div style="font-size:1.2rem; color:#10b981; margin-top:1rem;">$45.2K earned</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("View Store", key="vendor1")
    
    with col2:
        st.markdown("""
        <div class="card-container">
            <div class="card gradient-2 gradient-card">
                <span class="icon-large">⚡</span>
                <h3>BotMaster</h3>
                <p>189 Sales • 4.8⭐</p>
                <div style="font-size:1.2rem; color:#10b981; margin-top:1rem;">$32.1K earned</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("View Store", key="vendor2")
    
    with col3:
        st.markdown("""
        <div class="card-container">
            <div class="card gradient-3 gradient-card">
                <span class="icon-large">🔮</span>
                <h3>TokenOracle</h3>
                <p>156 Sales • 4.9⭐</p>
                <div style="font-size:1.2rem; color:#10b981; margin-top:1rem;">$28.7K earned</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("View Store", key="vendor3")

elif st.session_state.page == "Create Listing":
    st.markdown("""
    <h2 style="color:#8b5cf6; text-align:center; font-size:2.8rem; margin:3rem 0 1rem 0;">Create New Service</h2>
    <p style="text-align:center; font-size:1.2rem; color:#94a3b8; margin-bottom:3rem;">AI will auto-generate description & pricing</p>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠 Marketplace", key="create_home", use_container_width=True):
            st.session_state.page = "Marketplace"
            st.rerun()
    with col2:
        if st.button("👥 Vendors", key="create_vendors", use_container_width=True):
            st.session_state.page = "Vendors"
            st.rerun()
    
    with st.form("listing_form"):
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("🪙 Service Title", placeholder="AI Trading Bot - MCX Silver")
            category = st.selectbox("📁 Category", ["Trading Bots", "Signals", "Token Tools", "Smart Contracts"])
            price = st.number_input("💰 Price (USDC)", min_value=0.0, value=49.0, step=1.0)
        with col2:
            duration = st.selectbox("⏱️ Duration", ["1 Month", "3 Months", "Lifetime"])
            st.file_uploader("📁 Banner Image", type=["png", "jpg", "jpeg"])
        
        description = st.text_area("📝 Description", 
            placeholder="AI will generate optimized description based on your inputs...")
        ai_generate = st.checkbox("🤖 AI Generate Description & Tags")
        
        submitted = st.form_submit_button("🚀 Publish Listing")
        if submitted:
            st.session_state.form_submitted = True
            st.rerun()
    
    if st.session_state.form_submitted:
        st.markdown("""
        <div class="form-success">
            <div style="font-size:4rem;">✅</div>
            <h2>Listing Live!</h2>
            <p>Your service is now discoverable by 10K+ traders</p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

elif st.session_state.page == "Wallet":
    st.markdown('<h2 style="color:#8b5cf6; text-align:center; font-size:2.8rem; margin:3rem 0;">Wallet Dashboard</h2>')
    col1, col2 = st.columns(2)
    with col1:
        st.metric("💰 Balance", "2.47 ETH", "+0.12")
        st.metric("🪙 USDC", "1,247.32", "+23")
    with col2:
        st.metric("📈 P&L", "+12.4%", None)
        st.metric("🔥 Volume", "$4,892", "+56%")

# Footer - AICM Style
st.markdown("""
<div class="footer">
    <h3>🪙 AICM Marketplace</h3>
    <p>Pimpri-Chinchwad, Maharashtra | <a href="mailto:info@aicm.in" style="color:#8b5cf6;">info@aicm.in</a> | +91 98765 43210</p>
    <p>AI Crypto Services • Built for Traders • © 2026</p>
</div>
""", unsafe_allow_html=True)
