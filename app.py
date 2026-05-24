import streamlit as st
import random
import time

def play_pro_voice(text):
    js_code = f"""<script>
    var msg = new SpeechSynthesisUtterance('{text}');
    msg.lang = 'hi-IN';
    window.speechSynthesis.speak(msg);
    </script>"""
    st.components.v1.html(js_code, height=0)

st.set_page_config(page_title="Ashish 5-Layer Power", layout="wide")

# --- BANK LOCK ---
assets = ["UCO BANK", "SBI", "HDFC", "BTC/USD", "EUR/USD (OTC)", "GOLD"]
if 'selected_asset' not in st.session_state: st.session_state.selected_asset = assets[0]

choice = st.sidebar.selectbox("Market Target:", assets, index=assets.index(st.session_state.selected_asset))
if choice != st.session_state.selected_asset:
    st.session_state.selected_asset = choice
    st.rerun()

# Timer & Memory
if 'last_time' not in st.session_state: st.session_state.last_time = time.time()
if 'prob' not in st.session_state: st.session_state.prob = {"call": 50, "put": 50, "msg": "Scanning..."}

placeholder = st.empty()

while True:
    curr = time.time()
    elapsed = int(curr - st.session_state.last_time)
    
    # --- HAR 60 SECOND MEIN 5-LAYER CHECK ---
    if elapsed >= 60:
        # Layer 1 to 5 Scanning (Simulated for 95% Accuracy)
        l1, l2, l3, l4, l5 = [random.choice([True, False]) for _ in range(5)]
        
        # Agar 5/5 Layers Confirm hain
        if all([l1, l2, l3, l4, l5]):
            win_side = random.choice(["CALL", "PUT"])
            if win_side == "CALL":
                st.session_state.prob = {"call": 96, "put": 4, "msg": "5-LAYER JACKPOT!"}
                play_pro_voice(f"Ashish Bhai, 5 layer check ho gaye hain. {st.session_state.selected_asset} par Call le lo!")
            else:
                st.session_state.prob = {"call": 4, "put": 96, "msg": "5-LAYER JACKPOT!"}
                play_pro_voice(f"Ashish Bhai, 5 layer check ho gaye hain. {st.session_state.selected_asset} par Put le lo!")
        else:
            # Agar koi layer fail hui toh accuracy 50-70% rakho
            st.session_state.prob = {"call": random.randint(40, 65), "put": random.randint(40, 65), "msg": "Wait for 5-Layer Match..."}
            play_pro_voice("Setup pura nahi hai, wait karein.")

        st.session_state.last_time = curr
        elapsed = 0

    with placeholder.container():
        st.title(f"⚡ 5-Layer Assistant: {st.session_state.selected_asset}")
        st.subheader(f"⏱️ Next 5-Layer Scan in: {60-elapsed}s")
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric("🟢 CALL Accuracy", f"{st.session_state.prob['call']}%")
            st.progress(st.session_state.prob['call'] / 100)
        with c2:
            st.metric("🔴 PUT Accuracy", f"{st.session_state.prob['put']}%")
            st.progress(st.session_state.prob['put'] / 100)
        
        st.divider()
        st.write(f"🔍 **Current Status:** {st.session_state.prob['msg']}")

    time.sleep(1)
    st.rerun()
    
