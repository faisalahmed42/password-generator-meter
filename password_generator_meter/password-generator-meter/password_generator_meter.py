
import streamlit as st
import re
import random

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", "green"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "orange"
    else:
        return "❌ Weak Password - Improve it using the suggestions below:\n" + "\n".join(feedback), "red"

# Password Generator Function
def generate_strong_password():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
    return "".join(random.sample(characters, 12))  # Generates a 12-character password

# Blacklist Feature (Common Weak Passwords)
blacklist = ["password", "123456", "password123", "admin",]

# Streamlit UI
st.title("🔐 Password Strength Meter")

# Password Input
password = st.text_input("Enter your password:", type="password")

if password:
    # Check if password is in blacklist
    if password.lower() in blacklist:
        st.error("❌ This is a common weak password! Try a stronger one.")
    else:
        message, color = check_password_strength(password)
        st.markdown(f"<span style='color:{color}; font-size:16px;'>{message}</span>", unsafe_allow_html=True)

# Generate Strong Password Button
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.success(f"🔹 Suggested Strong Password: `{strong_password}`")
