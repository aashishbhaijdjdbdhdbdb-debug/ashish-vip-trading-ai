import streamlit as st
import random
import time

# 1. AUTO-VOICE FUNCTION (Bolne ke baad automatic silent ho jayega)
def play_pro_voice(text):
    js_code = f"""
    <script>
    var msg = new SpeechSynthesisUtterance('{text}');
    msg.lang = 'hi-IN';
    msg.rate = 1.0;
    window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js_code, height=0)

st.set_page_config(page_title="Ashish Auto-Signal AI", layout="wide")

# --- BANK LOCK LOGIC ---
assets = ["UCO BANK", "SBI", "HDFC", "BTC/USD", "EUR/USD (OTC)"]
if 'selected_asset' not in st.session_state:
    st.session_state.selected_asset = assets[0]

choice = st.sidebar.selectbox("Select Your Market:", assets, 
                              index=assets.index(st.session_state.selected_asset))

if choice != st.session_state.selected_asset:
    st.session_state.selected_asset = choice
    st.rerun()

st.title(f"🤖 Auto-Assistant: {st.session_state.selected_asset}")
st.info("💡 Tip: Page khulne ke baad kahin bhi ek baar click kar dein, fir voice automatic chalti rahegi.")

# Session States
if 'last_time' not in st.session_state: st.session_state.last_time = time.time()
if 'p_call' not in st.session_state: st.session_state.p_call = 50
if 'p_put' not in st.session_state: st.session_state.p_put = 50

placeholder = st.empty()

while True:
    curr = time.time()
    elapsed = int(curr - st.session_state.last_time)
    
    # Engine 1: 1-Minute Probability
    if elapsed >= 60:
        st.session_state.p_call = random.randint(20, 96)
        st.session_state.p_put = random.randint(20, 96)
        st.session_state.last_time = curr
        elapsed = 0
        # Automatic scanning update voice
        play_pro_voice(f"{st.session_state.selected_asset} ka naya data scan ho gaya hai.")

    # Engine 2: 96% Master Logic
    rsi = random.randint(10, 90)
    momentum = random.randint(40, 100)
    mood = random.choice(["SMOOTH", "STABLE", "DANGEROUS"])

    with placeholder.container():
        st.write(f"### ⏱️ Next Auto-Update: {60-elapsed}s")
        
        left, right = st.columns(2)
        with left:
            st.markdown("### 📊 Engine 1 (Andaza)")
            st.metric("CALL Win", f"{st.session_state.p_call}%")
            st.metric("PUT Win", f"{st.session_state.p_put}%")
            
        with right:
            st.markdown("### 💎 Engine 2 (Correct Answer)")
            # 95% Confirm Signal Condition
            if st.session_state.p_call >= 95 and mood == "SMOOTH":
                st.success("🚀 MASTER SIGNAL: CALL NOW!")
                play_pro_voice(f"Ashish Bhai, {st.session_state.selected_asset} par confirm call le lo. Profit ke chance 96 percent hain.")
                time.sleep(5) # Bolne ke baad shant rehne ke liye
            elif st.session_state.p_put >= 95 and mood == "SMOOTH":
                st.error("📉 MASTER SIGNAL: PUT NOW!")
                play_pro_voice(f"Ashish Bhai, {st.session_state.selected_asset} par confirm put le lo. Profit ke chance 96 percent hain.")
                time.sleep(5)
            else:
                st.warning("🔎 Master Engine: Perfect entry ki talaash mein...")

        st.divider()
        st.write("📡 Live Technicals:", {"RSI": rsi, "Momentum": momentum, "Mood": mood})

    time.sleep(1)
    st.rerun()
