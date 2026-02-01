"""
🏠 Smart Home Automation Dashboard - NO PLOTLY REQUIRED
Save as smart_home.py and run: streamlit run smart_home.py
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

# Page configuration
st.set_page_config(
    page_title="🏠 Smart Home Control Panel",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern smart home UI
st.markdown("""
    <style>
    .main-header { 
        font-size: 4rem; 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center; 
        margin-bottom: 2rem;
        font-weight: 700;
    }
    .device-card { 
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem; 
        border-radius: 20px; 
        color: white; 
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        margin: 1rem 0;
        border: none;
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
    .metric-container { padding: 1rem; border-radius: 15px; }
    .stButton > button { border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for devices
if 'devices' not in st.session_state:
    st.session_state.devices = {
        'living_light': {'status': 'OFF', 'brightness': 50, 'power': 0},
        'kitchen_light': {'status': 'OFF', 'brightness': 70, 'power': 0},
        'bedroom_ac': {'status': 'OFF', 'temp': 24, 'power': 0, 'mode': 'Cool'},
        'security_cam': {'status': 'ON', 'motion': False},
        'main_gate': {'status': 'CLOSED'},
        'water_pump': {'status': 'OFF', 'flow': 0},
        'garage_door': {'status': 'CLOSED'}
    }

def update_device_status(device_id, status):
    """Update device status"""
    st.session_state.devices[device_id]['status'] = status
    if 'power' in st.session_state.devices[device_id]:
        st.session_state.devices[device_id]['power'] = 15 if status == 'ON' else 0
    st.rerun()

# Header
st.markdown('<h1 class="main-header">🏠 Smart Home Control Center</h1>', unsafe_allow_html=True)
st.markdown("**Complete device control | Real-time monitoring | Automation ready**")

# Sidebar
st.sidebar.title("⚙️ Quick Controls")
quick_device = st.sidebar.selectbox("Quick Toggle", list(st.session_state.devices.keys()))
if st.sidebar.button("🔄 Toggle Device", key="quick_toggle"):
    current = st.session_state.devices[quick_device]['status']
    new_status = 'ON' if current in ['OFF', 'CLOSED'] else 'OFF'
    update_device_status(quick_device, new_status)

st.sidebar.markdown("---")
st.sidebar.subheader("🌡️ Weather")
st.sidebar.metric("Temperature", "28.4°C", "0.2°C")
st.sidebar.metric("Humidity", "62%", "-1%")

# Main Dashboard - Row 1
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("## 🏘️ Device Status")
    
    # Lights
    st.markdown("### 💡 Lighting")
    light_cols = st.columns(2)
    
    with light_cols[0]:
        device = 'living_light'
        status_class = "status-on" if st.session_state.devices[device]['status'] == 'ON' else "status-off"
        st.markdown(f'''
            <div class="device-card {status_class}">
                <h3>🛋️ Living Room</h3>
                <p><strong>{st.session_state.devices[device]["status"]}</strong></p>
                <p>Brightness: {st.session_state.devices[device]["brightness"]}%</p>
            </div>
        ''', unsafe_allow_html=True)
        if st.button("Toggle", key=f"{device}_btn"):
            update_device_status(device, 'ON' if st.session_state.devices[device]['status'] == 'OFF' else 'OFF')
    
    with light_cols[1]:
        device = 'kitchen_light'
        status_class = "status-on" if st.session_state.devices[device]['status'] == 'ON' else "status-off"
        st.markdown(f'''
            <div class="device-card {status_class}">
                <h3>🍳 Kitchen</h3>
                <p><strong>{st.session_state.devices[device]["status"]}</strong></p>
                <p>Power: {st.session_state.devices[device]["power"]}W</p>
            </div>
        ''', unsafe_allow_html=True)
        if st.button("Toggle", key=f"{device}_btn"):
            update_device_status(device, 'ON' if st.session_state.devices[device]['status'] == 'OFF' else 'OFF')

with col2:
    # Energy metrics
    st.markdown("### ⚡ Energy")
    total_power = sum(d.get('power', 0) for d in st.session_state.devices.values())
    st.metric("Total Power", f"{total_power}W", "↑12W")
    st.metric("Daily Cost", "₹48", "₹4")

# Climate Control
st.markdown("### ❄️ Climate Control")
ac_cols = st.columns(2)

device = 'bedroom_ac'
status_class = "status-on" if st.session_state.devices[device]['status'] == 'ON' else "status-off"

with ac_cols[0]:
    st.markdown(f'''
        <div class="device-card {status_class}">
            <h3>🛏️ Bedroom AC</h3>
            <p><strong>{st.session_state.devices[device]["status"]}</strong></p>
            <p>Temp: {st.session_state.devices[device]["temp"]}°C</p>
            <p>Mode: {st.session_state.devices[device]["mode"]}</p>
        </div>
    ''', unsafe_allow_html=True)

with ac_cols[1]:
    ac_btn_col1, ac_btn_col2 = st.columns(2)
    with ac_btn_col1:
        if st.button("Power", key="ac_power"):
            update_device_status(device, 'ON' if st.session_state.devices[device]['status'] == 'OFF' else 'OFF')
    with ac_btn_col2:
        new_temp = st.slider("Temp", 18, 28, st.session_state.devices[device]['temp'], key="ac_temp")
        if 'temp' in st.session_state and new_temp != st.session_state.devices[device]['temp']:
            st.session_state.devices[device]['temp'] = new_temp

# Security Row
st.markdown("### 🔒 Security & Access")
sec_cols = st.columns(3)

# Camera
device = 'security_cam'
status_class = "status-on" if st.session_state.devices[device]['status'] == 'ON' else "status-off"
st.markdown(f'''
    <div class="device-card {status_class}">
        <h3>📹 Security Cam</h3>
        <p><strong>{st.session_state.devices[device]["status"]}</strong></p>
        <p>{'🚨 MOTION!' if st.session_state.devices[device].get('motion', False) else 'All clear'}</p>
    </div>
''', unsafe_allow_html=True)

# Gate
device = 'main_gate'
status_class = "status-on" if st.session_state.devices[device]['status'] == 'OPEN' else "status-off"
with sec_cols[1]:
    st.markdown(f'''
        <div class="device-card {status_class}">
            <h3>🚪 Main Gate</h3>
            <p><strong>{st.session_state.devices[device]["status"]}</strong></p>
        </div>
    ''', unsafe_allow_html=True)
    if st.button("Toggle Gate", key="gate_btn"):
        status = st.session_state.devices[device]['status']
        update_device_status(device, 'OPEN' if status == 'CLOSED' else 'CLOSED')

# Simple Energy Chart (Streamlit native)
st.markdown("### 📊 Energy Usage (Last 24h)")
energy_data = pd.DataFrame({
    'Hour': range(24),
    'Usage': np.random.uniform(0.5, 2.5, 24)
})
st.bar_chart(energy_data.set_index('Hour'))

# Automation Rules
with st.expander("🤖 Automation Rules", expanded=False):
    st.markdown("""
    **Active Rules:**
    • 💡 Lights OFF after 30min inactivity  
    • ❄️ AC Eco-mode 10PM-6AM (22-26°C)
    • 🔒 Night security at sunset
    • 🚿 Water pump: 6AM, 7PM daily
    • ⚡ Alert: >5kWh/hour usage
    
    **Quick Actions:**
    """)
    mode_cols = st.columns(3)
    with mode_cols[0]:
        if st.button("🌙 Night Mode", use_container_width=True):
            st.success("✅ Night mode ON")
    with mode_cols[1]:
        if st.button("☀️ Day Mode", use_container_width=True):
            st.success("✅ Day mode ON")
    with mode_cols[2]:
        if st.button("🚨 EMERGENCY STOP", use_container_width=True):
            st.error("🛑 ALL DEVICES OFF")
            for dev_id in st.session_state.devices:
                if st.session_state.devices[dev_id]['status'] not in ['CLOSED']:
                    st.session_state.devices[dev_id]['status'] = 'OFF'

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>🏠 Smart Home Dashboard | Ready for MQTT/Home Assistant | Mobile Responsive</p>
    <p>🔧 <strong>Works with: streamlit pandas numpy</strong> | No plotly needed!</p>
</div>
""", unsafe_allow_html=True)
