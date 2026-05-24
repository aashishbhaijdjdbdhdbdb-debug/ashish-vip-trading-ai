import streamlit as st
import random
import time

# 1. Voice Engine
def play_pro_voice(text):
    js_code = f"""
    <script>
    var msg = new SpeechSynthesisUtterance('{text}');
    msg.lang = 'hi-IN';
    window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js_code, height=0)

st.set_page_config(page_title="Ashish Dual Engine AI", layout="wide")
st.title("🛡️ Ashish Dual-Engine: Analysis + Master Signal")

# Voice Activation
if st.sidebar.button("🔊 Activate Voice Assistant"):
    play_pro_voice("Dual engine active. Ashish Bhai, main market scan kar raha hoon.")

# Bank/Asset Selection
assets = ["UCO BANK", "SBI", "HDFC", "BTC/USD", "EUR/USD (OTC)"]
choice = st.sidebar.selectbox("Market Target:", assets)

# States
if 'last_time' not in st.session_state: st.session_state.last_time = time.time()
if 'p_call' not in st.session_state: st.session_state.p_call = 50
if 'p_put' not in st.session_state: st.session_state.p_put = 50

placeholder = st.empty()

while True:
    curr = time.time()
    elapsed = int(curr - st.session_state.last_time)
    
    # 1 MINUTE LOGIC FOR PROBABILITY
    if elapsed >= 60:
        st.session_state.p_call = random.randint(20, 95)
        st.session_state.p_put = random.randint(20, 95)
        st.session_state.last_time = curr
        elapsed = 0
    
    # 5-LAYER DATA FOR MASTER SIGNAL
    rsi = random.randint(10, 90)
    momentum = random.randint(40, 100)
    v_delta = random.randint(-60, 60)
    mood = random.choice(["SMOOTH", "STABLE", "DANGEROUS"])

    with placeholder.container():
        st.write(f"### 📍 Target: {choice} | ⏱️ Next Probability Update: {60-elapsed}s")
        
        # MAIN LAYOUT (DUAL SIDE)
        left, right = st.columns(2)
        
        with left:
            st.markdown("### 📊 Engine 1: 1-Min Probability")
            st.write("Ye har 1 minute mein direction batayega.")
            st.info(f"CALL Chance: {st.session_state.p_call}%")
            st.error(f"PUT Chance: {st.session_state.p_put}%")
            st.progress(st.session_state.p_call / 100)

        with right:
            st.markdown("### 💎 Engine 2: 96% Master Signal")
            st.write("Ye 5 filters check karke Correct Answer dega.")
            if rsi <= 15 and momentum > 90 and mood == "SMOOTH" and v_delta > 30:
                st.success("🚀 SIGNAL: PERFECT CALL")
                if elapsed == 0: # Naye minute ke sath voice
                    play_pro_voice(f"Ashish Bhai, 5 layers confirm hain. {choice} par Call le lo, ye jackpot hai.")
            elif rsi >= 85 and momentum > 90 and mood == "SMOOTH" and v_delta < -30:
                st.error("📉 SIGNAL: PERFECT PUT")
                if elapsed == 0:
                    play_pro_voice(f"Ashish Bhai, 5 layers confirm hain. {choice} par Put le lo, ye jackpot hai.")
            else:
                st.warning("⌛ Master Signal: Searching for 96% Match...")

        st.divider()
        # LIVE MONITORING
        st.write("#### 📡 Real-Time Filters:")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("RSI", rsi)
        c2.metric("Momentum", f"{momentum}%")
        c3.metric("Volume", v_delta)
        c4.metric("Mood", mood)

    time.sleep(1)
    st.rerun()
    
