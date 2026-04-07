import streamlit as st
import json
import os
from datetime import datetime

# Page config
st.set_page_config(
    page_title="SmartNest Automation", 
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------
# LEAD STORAGE FUNCTION
# ----------------------
def save_lead(data):
    file_path = "leads.json"
    leads = []

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                leads = json.load(f)
            except:
                leads = []

    leads.append(data)

    with open(file_path, "w") as f:
        json.dump(leads, f, indent=4)

# ----------------------
# SESSION STATE
# ----------------------
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# ----------------------
# FIXED HEADER NAVIGATION (NO JS)
# ----------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
        st.rerun()

with col2:
    if st.button("👨‍💼 About"):
        st.session_state.page = "About"
        st.rerun()

with col3:
    if st.button("📦 Products"):
        st.session_state.page = "Products"
        st.rerun()

with col4:
    if st.button("💬 Contact"):
        st.session_state.page = "Contact"
        st.rerun()

# ----------------------
# FLOATING WHATSAPP BUTTON
# ----------------------
st.markdown("""
<style>
.whatsapp-float {
    position: fixed;
    bottom: 20px;
    right: 20px;
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
    <a href="https://wa.me/919876543210" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" />
    </a>
</div>
""", unsafe_allow_html=True)

# ----------------------
# SIDEBAR
# ----------------------
with st.sidebar:
    selected = st.selectbox("Choose Page:", ["Home", "About", "Products", "Contact"],
                          index=["Home", "About", "Products", "Contact"].index(st.session_state.page))
    if selected != st.session_state.page:
        st.session_state.page = selected
        st.rerun()

# ----------------------
# CONTACT PAGE (UPDATED)
# ----------------------
if st.session_state.page == "Contact":
    if not st.session_state.form_submitted:
        with st.form("interest_form", clear_on_submit=True):
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            package = st.selectbox("Package", ["Basic Package", "Standard Package", "Premium Package"])
            home_type = st.selectbox("Home Type", ["1-2 BHK", "3 BHK", "4+ BHK", "Villa/Independent"])
            budget = st.selectbox("Budget", ["Economy", "Mid", "Premium"])
            message = st.text_area("Message")

            submitted = st.form_submit_button("Submit")

            if submitted:
                lead_data = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "package": package,
                    "home_type": home_type,
                    "budget": budget,
                    "message": message
                }

                save_lead(lead_data)
                st.session_state.form_submitted = True
                st.rerun()

    if st.session_state.form_submitted:
        st.success("Lead saved successfully!")

# ----------------------
# OTHER PAGES PLACEHOLDER
# ----------------------
if st.session_state.page == "Home":
    st.write("Home Page Content")

if st.session_state.page == "About":
    st.write("About Page Content")

if st.session_state.page == "Products":
    st.write("Products Page Content")
