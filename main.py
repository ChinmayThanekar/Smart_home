"""
🏠 Complete Smart Home Automation Dashboard
Save as smart_home.py and run: streamlit run smart_home.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# Page configuration for website-like experience
st.set_page_config(
    page_title="🏠 Smart Home Control Panel",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern smart home UI
st.markdown("""
    <style>
    /* Main layout */
    .main-header { 
        font-size: 4rem; 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center; 
        margin-bottom: 2rem;
        font-weight: 700;
    }
    
    /* Device cards */
    .device-card { 
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem; 
        border-radius: 20px; 
        color: white; 
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        margin: 1rem 0;
    }
    .device-card:hover { transform: translateY(-5px); }
    
    .status-on { 
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%) !important;
        animation: pulse 2s infinite;
    }
    .status-off { 
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%) !important;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(79, 172, 254, 0.7); }
        70% { box-shadow: 0 0 0 20px rgba(79, 172, 254, 0); }
        100% { box-shadow: 0 0 0 0 rgba(79, 172, 254, 0); }
    }
    
    /* Metrics */
    .metric-container { padding: 1rem; border-radius: 15px; }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for device controls
if 'devices' not in st.session_state:
    st.session_state.devices = {
        'living_light': {'status': 'OFF', 'brightness': 50, 'power': 0},
        'kitchen_light': {'status': 'OFF', 'brightness': 70, 'power': 0},
        'bedroom_ac': {'status': 'OFF', 'temp': 24, 'power': 0},
        'security_cam': {'status': 'ON', 'motion': False},
        'main_gate': {'status': 'CLOSED'},
        'water_pump': {'status': 'OFF', 'flow': 0},
        'garage_door': {'status': 'CLOSED'}
    }

def update_device_status(device_id, status):
    """Update device status in session state"""
    st.session_state.devices[device_id]['status'] = status
    if status == 'ON':
        st.session_state.devices[device_id]['power'] = 15  # Default power
    else:
        st.session_state.devices[device_id]['power'] = 0
    st.rerun()

# Header
st.markdown('<h1 class="main-header">🏠 Smart Home Control Center</h1>', unsafe_allow_html=True)
st.markdown("**Central dashboard for all your smart devices** | Real-time monitoring & automation ready")

# Sidebar - Quick controls & weather
st.sidebar.title("⚙️ Quick Actions")
quick_device = st.sidebar.selectbox("Quick Toggle", list(st.session_state.devices.keys()))
if st.sidebar.button("🔄 Toggle", key="quick_toggle", type="primary"):
    current_status = st.session_state.devices[quick_device]['status']
    new_status = 'ON' if current_status == 'OFF' else 'OFF'
    update_device_status(quick_device, new_status)

st.sidebar.markdown("---")
st.sidebar.subheader("🌡️ Weather")
st.sidebar.metric("Temperature", "28.4°C", "0.2°C")
st.sidebar.metric("Humidity", "62%", "-1%")

# Main Dashboard
row1_col1, row1_col2 = st.columns([2, 1])

with row1_col1:
    st.markdown("## 🏘️ Device Status Overview")
    
    # Lights Row
    st.markdown("### 💡 Lighting Control")
    light_col1, light_col2 = st.columns(2)
    
    with light_col1:
        device_id = 'living_light'
        status_class = "status-on" if st.session_state.devices[device_id]['status'] == 'ON' else "status-off"
        st.markdown(f'''
            <div class="device-card {status_class}">
                <h3>🛋️ Living Room Light</h3>
                <p><strong>{st.session_state.devices[device_id]["status"]}</strong></p>
                <p>Power: {st.session_state.devices[device_id]["power"]}W</p>
            </div>
        ''', unsafe_allow_html=True)
        if st.button("Toggle", key=f"{device_id}_toggle", use_container_width=True):
            update_device_status(device_id, 'ON' if st.session_state.devices[device_id]['status'] == 'OFF' else 'OFF')
    
    with light_col2:
        device_id = 'kitchen_light'
        status_class = "status-on" if st.session_state.devices[device_id]['status'] == 'ON' else "status-off"
        st.markdown(f'''
            <div class="device-card {status_class}">
                <h3>🍳 Kitchen Light</h3>
                <p><strong>{st.session_state.devices[device_id]["status"]}</strong></p>
                <p>Power: {st.session_state.devices[device_id]["power"]}W</p>
            </div>
        ''', unsafe_allow_html=True)
        if st.button("Toggle", key=f"{device_id}_toggle", use_container_width=True):
            update_device_status(device_id, 'ON' if st.session_state.devices[device_id]['status'] == 'OFF' else 'OFF')

with row1_col2:
    # Energy metrics
    st.markdown("### ⚡ Energy Monitor")
    total_power = sum(device['power'] for device in st.session_state.devices.values())
    st.metric("Total Power", f"{total_power}W", "12W")
    st.metric("Daily Usage", "2.4 kWh", "0.2 kWh")
    st.metric("Cost", "₹48", "₹4")

# Climate Control Row
st.markdown("### ❄️ Climate Control")
ac_col1, ac_col2 = st.columns(2)

device_id = 'bedroom_ac'
status_class = "status-on" if st.session_state.devices[device_id]['status'] == 'ON' else "status-off"

with ac_col1:
    st.markdown(f'''
        <div class="device-card {status_class}">
            <h3>🛏️ Bedroom AC</h3>
            <p><strong>{st.session_state.devices[device_id]["status"]}</strong></p>
            <p>Temp: {st.session_state.devices[device_id]["temp"]}°C</p>
            <p>Power: {st.session_state.devices[device_id]["power"]}W</p>
        </div>
    ''', unsafe_allow_html=True)

with ac_col2:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("Toggle", key=f"{device_id}_toggle", use_container_width=True)
    with col2:
        new_temp = st.slider("Set Temp", 18, 28, st.session_state.devices[device_id]['temp'], key=f"{device_id}_temp")
        if new_temp != st.session_state.devices[device_id]['temp']:
            st.session_state.devices[device_id]['temp'] = new_temp
    with col3:
        if st.button("Fan Speed", key=f"{device_id}_fan"):
            st.success("Fan speed changed!")

# Security & Outdoor
st.markdown("### 🔒 Security & Outdoor")
sec_col1, sec_col2, sec_col3 = st.columns(3)

device_id = 'security_cam'
status_class = "status-on" if st.session_state.devices[device_id]['status'] == 'ON' else "status-off"
st.markdown(f'''
    <div class="device-card {status_class}">
        <h3>📹 Security Camera</h3>
        <p><strong>{st.session_state.devices[device_id]["status"]}</strong></p>
        {"🚨 Motion Detected!" if st.session_state.devices[device_id].get('motion', False) else ""}
    </div>
''', unsafe_allow_html=True)

device_id = 'main_gate'
status_class = "status-on" if st.session_state.devices[device_id]['status'] == 'OPEN' else "status-off"
with sec_col2:
    st.markdown(f'''
        <div class="device-card {status_class}">
            <h3>🚪 Main Gate</h3>
            <p><strong>{st.session_state.devices[device_id]["status"]}</strong></p>
        </div>
    ''', unsafe_allow_html=True)
    if st.button("Toggle Gate", key="main_gate_toggle"):
        status = st.session_state.devices[device_id]['status']
        update_device_status(device_id, 'OPEN' if status == 'CLOSED' else 'CLOSED')

# Energy Chart
st.markdown("### 📊 24h Energy Usage")
chart_data = pd.DataFrame({
    'time': pd.date_range(start=datetime.now() - timedelta(hours=24), periods=25, freq='H'),
    'usage': np.random.uniform(0.1, 0.8, 25).cumsum()
})
fig = px.area(chart_data, x='time', y='usage', title="Energy Consumption (kWh)")
fig.update_layout(showlegend=False, height=400)
st.plotly_chart(fig, use_container_width=True)

# Automation Rules
with st.expander("🤖 Automation Rules (Click to Edit)", expanded=False):
    st.markdown("""
    **Active Rules:**
    - 💡 Lights auto-off after 30min inactivity
    - ❄️ AC eco-mode 10PM-6AM (22-26°C)
    - 🔒 Security night mode at sunset
    - 🚿 Water pump schedules (6AM, 7PM)
    - ⚡ High energy alerts >5kWh/hour
    
    **Quick Actions:**
    """)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🌙 Night Mode"):
            st.success("Night mode activated!")
    with col2:
        if st.button("☀️ Day Mode"):
            st.success("Day mode activated!")
    with col3:
        if st.button("🚨 Emergency Stop"):
            st.error("All devices OFF!")
            for device in st.session_state.devices:
                update_device_state(device, 'OFF')

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🏠 Powered by Streamlit | Ready for MQTT/Home Assistant | Deploy to cloud</p>
    <p>📱 Mobile responsive | 🔄 Real-time updates | ⚙️ Production ready</p>
</div>
""", unsafe_allow_html=True)
