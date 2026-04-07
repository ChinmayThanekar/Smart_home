import streamlit as st
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SmartNest Automation",
    page_icon="🏠",
    layout="wide"
)

# ---------------- NAVIGATION ----------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

def navigate(page):
    st.session_state.page = page
    st.rerun()

# ---------------- GOOGLE SHEETS ----------------
def save_lead(data):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        st.secrets["gcp_service_account"], scope
    )

    client = gspread.authorize(creds)
    sheet = client.open("SmartNest_Leads").sheet1

    row = [
        str(datetime.datetime.now()),
        data["name"],
        data["email"],
        data["phone"],
        data["package"],
        data["home_type"],
        data["budget"],
        data["message"]
    ]

    sheet.append_row(row)

# ---------------- WHATSAPP ----------------
def whatsapp_redirect(name):
    phone_number = "919876543210"
    message = f"Hi, I just submitted a request on SmartNest. My name is {name}"
    url = f"https://wa.me/{phone_number}?text={message.replace(' ', '%20')}"
    st.markdown(f"[👉 Continue on WhatsApp]({url})")

# ---------------- CSS ----------------
st.markdown("""
<style>
.hero-title { font-size: 3rem; font-weight: bold; text-align: center; }
.card { padding: 2rem; border-radius: 20px; background: #ffffff; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }

@media (max-width: 768px) {
    .hero-title { font-size: 2rem !important; }
    .card { padding: 1.5rem !important; }
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("Navigation")
    page = st.radio("", ["Home", "About", "Products", "Contact"])

    if page != st.session_state.page:
        navigate(page)

# ---------------- HOME ----------------
if st.session_state.page == "Home":
    st.markdown("<h1 class='hero-title'>🏠 SmartNest Automation</h1>", unsafe_allow_html=True)
    st.write("Transform your home into a smart home with automation.")

    col1, col2 = st.columns(2)
    with col1:
        st.button("Explore Packages", on_click=navigate, args=("Products",))
    with col2:
        st.button("Free Consultation", on_click=navigate, args=("Contact",))

# ---------------- ABOUT ----------------
elif st.session_state.page == "About":
    st.title("About SmartNest")
    st.write("We provide smart home automation solutions across India.")

# ---------------- PRODUCTS ----------------
elif st.session_state.page == "Products":
    st.title("Packages")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'>Basic Package<br>₹49,999</div>", unsafe_allow_html=True)
        st.button("Get Quote", on_click=navigate, args=("Contact",))

    with col2:
        st.markdown("<div class='card'>Standard Package<br>₹99,999</div>", unsafe_allow_html=True)
        st.button("Get Quote", on_click=navigate, args=("Contact",))

    with col3:
        st.markdown("<div class='card'>Premium Package<br>₹1,99,999</div>", unsafe_allow_html=True)
        st.button("Get Quote", on_click=navigate, args=("Contact",))

# ---------------- CONTACT ----------------
elif st.session_state.page == "Contact":

    st.title("Contact Us")

    if not st.session_state.form_submitted:
        with st.form("lead_form"):
            name = st.text_input("Name *")
            email = st.text_input("Email *")
            phone = st.text_input("Phone")

            package = st.selectbox("Package", ["Basic", "Standard", "Premium"])
            home_type = st.selectbox("Home Type", ["1-2 BHK", "3 BHK", "4+ BHK"])
            budget = st.selectbox("Budget", ["50K-1L", "1-3L", "3L+"])

            message = st.text_area("Message")

            submitted = st.form_submit_button("Submit")

            if submitted:
                if not name or not email:
                    st.error("Please fill required fields")
                else:
                    data = {
                        "name": name,
                        "email": email,
                        "phone": phone,
                        "package": package,
                        "home_type": home_type,
                        "budget": budget,
                        "message": message
                    }

                    save_lead(data)

                    st.session_state.form_submitted = True
                    st.session_state.lead_data = data
                    st.rerun()

    else:
        data = st.session_state.lead_data

        st.success("🎉 Request submitted successfully!")
        st.json(data)

        st.markdown("### ⚡ Instant Response")
        whatsapp_redirect(data["name"])

        st.balloons()

        if st.button("Submit Another Response"):
            st.session_state.form_submitted = False
            st.rerun()
