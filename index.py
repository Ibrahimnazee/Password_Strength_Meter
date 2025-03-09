import streamlit as st
import re

# 🌨️ Custom CSS for a Sleek Dark Blue Theme
st.markdown("""
    <style>
        .stApp {
            background-color: #27687a;
            color: #E6EDF3;
            font-family: 'Arial', sans-serif;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.4);
        }
        .title {
            text-align: center;
            color: #58A6FF;
            font-size: 2.5em;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #FFD700;
        }
        .footer {
            text-align: center;
            font-size: 1em;
            color: #FFD700;
            margin-top: 30px;
        }
        .stTextInput label {
            color: #E6EDF3 !important;
        }
        .stButton>button {
            color: #ffffff !important;
            background-color: #238636 !important;
            border-radius: 10px;
            padding: 12px 22px;
            font-size: 18px;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #2EA043 !important;
        }
        .stSuccess {
            color: #00FF7F !important;
        }
        .stWarning {
            color: #FFA500 !important;
        }
        .stError {
            color: #FF6347 !important;
        }
        .stInfo {
            color: #00BFFF !important;
        }
    </style>
""", unsafe_allow_html=True)

# 🎉 Title with Styled Header
st.markdown("""
    <h1 class='title'>🔐 Password Strength Meter</h1>
    <p class='subtitle'>Secure your online presence with a powerful password!</p>
""", unsafe_allow_html=True)

# 📝 Description
st.markdown("""
    Ensure your password is strong and secure by checking:
    - ✅ **At least 8 characters**
    - ✅ **Upper & Lowercase letters**
    - ✅ **Numbers (0-9)**
    - ✅ **Special Characters (!@#$%^&*)**

    > 🔒 *Enhance your security by creating a stronger password!*
""")

# 🏡 Stylish Input Field
password = st.text_input("🔑 Enter your password:", type="password", key="password_input")

# 🔍 Password Strength Check Function
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include **both uppercase and lowercase** letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least **one number (0-9)**.")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least **one special character (!@#$%^&*)**.")

    return score, feedback

# ✅ Button to Check Password
if st.button("🔍 Check Password Strength", key="check_button"):
    if password:
        score, feedback = check_password_strength(password)

        st.subheader("🔒 Password Strength Result:")

        if score == 4:
            st.markdown("<p class='stSuccess'>🎉 Strong Password! Your password is well-secured.</p>", unsafe_allow_html=True)
        elif score == 3:
            st.markdown("<p class='stWarning'>⚠️ Moderate Password - Consider enhancing security.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='stError'>❌ Weak Password - Follow the suggestions below to strengthen it.</p>", unsafe_allow_html=True)

        if feedback:
            st.markdown("<p class='stInfo'>💡 Suggestions to improve your password:</p>", unsafe_allow_html=True)
            for tip in feedback:
                st.markdown(f"- {tip}")
    else:
        st.error("🚨 Please enter a password to analyze.")

# 🌟 Footer with a Stylish Signature
st.markdown("""
    <hr>
    <p class='footer'>🚀 Made by <strong>Ibrahim Nazeer 🚀</strong></p>
""", unsafe_allow_html=True)
