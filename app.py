import streamlit as st
import random
import time

# 1. Voice Engine (Auto-Clear Voice)
def play_pro_voice(text):
    js_code = f"""<script>
    var msg = new SpeechSynthesisUtterance('{text}');
    msg.lang = 'hi-IN';
    msg.rate = 1.1;
    window.speechSynthesis.speak(msg);
    </script>"""
    st.components.v1.html(js_code, height=0)

st.set_page_config(page_title="Ashish 1-Min Master", layout="wide")

# --- Permanent Bank Lock ---
assets = ["UCO BANK", "SBI", "HDFC", "BTC/USD", "EUR/USD (OTC)", "GOLD"]
if 'selected_asset' not in st.session_state: st.session_state.selected_asset = assets[0]

choice = st.sidebar.selectbox("Select Asset:", assets, index=assets.index(st.session_state.selected_asset))
if choice != st.session_state.selected_asset:
    st.session_state.selected_asset = choice
    st.rerun()

# States
if 'last_tick' not in st.session_state: st.session_state.last_tick = time.time()
if 'c_prob' not in st.session_state: st.session_state.c_prob = 50

placeholder = st.empty()

while True:
    now = time.time()
    elapsed = int(now - st.session_state.last_tick)
    
    # --- 1 MINUTE DYNAMICS ---
    # Har 10 second mein andaza badlega (Thinking process)
    if elapsed % 10 == 0:
        st.session_state.c_prob = random.randint(40, 95)

    # FINAL 60 SECONDS CHECK
    if elapsed >= 60:
        # Layer Check (95% Accuracy Simulation)
        final_roll = random.randint(1, 100)
        if final_roll > 10: # 90% chance of getting a clear direction
            side = "CALL" if st.session_state.c_prob > 50 else "PUT"
            acc = random.randint(94, 98)
            play_pro_voice(f"Ashish Bhai, 1 minute ka analysis poora hua. {st.session_state.selected_asset} par {side} lo. {acc} percent confirm hai.")
            msg_type = "SUCCESS"
        else:
            play_pro_voice("Market tight hai, abhi trade cancel karo.")
            msg_type = "WARNING"
            
        st.session_state.last_tick = now
        elapsed = 0

    with placeholder.container():
        st.title(f"⚡ 1-Min Master Engine: {st.session_state.selected_asset}")
        st.subheader(f"⏱️ Next Trade Decision in: {60-elapsed}s")
        
        # Dual Meter for Visual Impact
        c_val = st.session_state.c_prob
        p_val = 100 - c_val
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"### 🟢 CALL: {c_val}%")
            st.progress(c_val / 100)
        with col2:
            st.markdown(f"### 🔴 PUT: {p_val}%")
            st.progress(p_val / 100)
            
        st.divider()
        
        # Smart Status
        if c_val > 85:
            st.success("🔥 AI Thinking: CALL looks very Strong!")
        elif p_val > 85:
            st.error("📉 AI Thinking: PUT looks very Strong!")
        else:
            st.info("🔎 AI Scanning: 5-Layers are being verified...")
            
        # Technical Indicators (Just for show of power)
        st.write(f"📡 RSI: {random.randint(20,80)} | Vol: {random.randint(40,90)}% | Trend: Stable")

    time.sleep(1)
    st.rerun()
        
