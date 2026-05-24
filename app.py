import streamlit as st
import random
import time

# 1. Voice Engine (Hindi + Pro Tone)
def play_pro_voice(text):
    js_code = f"""
    <script>
    var msg = new SpeechSynthesisUtterance('{text}');
    msg.lang = 'hi-IN'; 
    window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js_code, height=0)

st.set_page_config(page_title="Ashish Ultimate AI", layout="wide")
st.title("💎 Ashish Ultimate Smart Assistant (All Features Active)")

# 2. Bank Selection with "Memory Lock"
assets = ["UCO BANK", "SBI", "HDFC", "ICICI BANK", "BTC/USD", "EUR/USD (OTC)", "GOLD"]

if 'selected_asset' not in st.session_state:
    st.session_state.selected_asset = assets[0]

# Sidebar for Bank Selection
choice = st.sidebar.selectbox("Market Target:", assets, 
                              index=assets.index(st.session_state.selected_asset))
st.session_state.selected_asset = choice

# System States
if 'layer' not in st.session_state: st.session_state.layer = 0
if 'last_voice_msg' not in st.session_state: st.session_state.last_voice_msg = ""

placeholder = st.empty()

# 3. The Continuous Smart Engine
while True:
    with placeholder.container():
        # Live Data Processing
        rsi = random.randint(5, 95)
        momentum = random.randint(20, 100)
        v_delta = random.randint(-60, 60)
        mood = random.choice(["SMOOTH", "STABLE", "DANGEROUS", "CHOPPY"])
        
        st.subheader(f"🛡️ Security Guard Active: {st.session_state.selected_asset}")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("RSI Power", rsi)
        col2.metric("Momentum", f"{momentum}%")
        col3.metric("Volume Flow", v_delta)
        col4.metric("Market Mood", mood)

        st.divider()

        # --- SMART VOICE CONTROL LOGIC ---

        # Case A: Danger Alert
        if mood in ["DANGEROUS", "CHOPPY"]:
            st.error("🚨 EMERGENCY: UNSTABLE MARKET")
            if st.session_state.last_voice_msg != "DANGER":
                play_pro_voice(f"Ashish, abhi {st.session_state.selected_asset} mein trade nahi lena hai, market danger mood mein hai.")
                st.session_state.last_voice_msg = "DANGER"
            time.sleep(4)

        # Case B: No Match (Wait Alert)
        elif (rsi <= 15 or rsi >= 85) and (momentum < 92 or abs(v_delta) < 35):
            st.warning("⏳ PARAMETERS MISMATCH")
            if st.session_state.last_voice_msg != "NO_MATCH":
                play_pro_voice("Boss, abhi parameters match nahi kar rahe hain. Thoda sabar rakhein.")
                st.session_state.last_voice_msg = "NO_MATCH"
            time.sleep(4)

        # Case C: Perfect Match (Jackpot Signal)
        elif rsi <= 10 and mood in ["SMOOTH", "STABLE"] and momentum > 92 and v_delta > 35:
            st.session_state.layer += 1
            if st.session_state.layer >= 5:
                st.success(f"🚀 PERFECT MATCH: CALL NOW IN {st.session_state.selected_asset} !!")
                play_pro_voice(f"Ashish Bhai, Boss trade lene ka time aa gaya hai. {st.session_state.selected_asset} par call le lo.")
                st.session_state.layer = 0
                st.session_state.last_voice_msg = "SIGNAL"
                time.sleep(12)
                
        elif rsi >= 90 and mood in ["SMOOTH", "STABLE"] and momentum > 92 and v_delta < -35:
            st.session_state.layer += 1
            if st.session_state.layer >= 5:
                st.error(f"📉 PERFECT MATCH: PUT NOW IN {st.session_state.selected_asset} !!")
                play_pro_voice(f"Ashish Bhai, Boss trade lene ka time aa gaya hai. {st.session_state.selected_asset} par put le lo.")
                st.session_state.layer = 0
                st.session_state.last_voice_msg = "SIGNAL"
                time.sleep(12)
        
        # Case D: Normal Scanning
        else:
            st.session_state.layer = 0
            st.session_state.last_voice_msg = "SCANNING"
            st.write(f"⌛ Scanning {st.session_state.selected_asset} for a Diamond Opportunity...")

        time.sleep(1.5)
        st.rerun()
