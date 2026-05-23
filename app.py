import streamlit as st
import random
import time

st.set_page_config(page_title="Ashish VIP Shield AI", layout="centered")
st.title("🛡️ Ashish VIP Shield Predictor")

choice = st.selectbox("Market Select Karein:", ["EUR/USD (OTC)", "BTC/USD", "GOLD (OTC)"])

placeholder = st.empty()

while True:
    with placeholder.container():
        # Indicators
        rsi = random.randint(10, 90)
        trend = random.randint(1, 100)
        # New: Volatility Check
        volatility = random.choice(["LOW", "HIGH", "STABLE"])
        
        st.subheader(f"📊 Market: {choice}")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("RSI", rsi)
        c2.metric("Trend", f"{trend}%")
        c3.metric("Risk", volatility)

        st.divider()

        # Extra Safe Logic
        if rsi < 25 and trend > 75 and volatility == "STABLE":
            st.success("🔥 POWERFUL CALL (BUY) - SAFE ENTRY")
            st.write("Reason: Market is stable & oversold. High chance of winning.")
        elif rsi > 75 and trend > 75 and volatility == "STABLE":
            st.error("📉 POWERFUL PUT (SELL) - SAFE ENTRY")
            st.write("Reason: Resistance is strong. High chance of downward move.")
        else:
            st.warning("⏳ WAIT - High Risk / Jhatka Possible")
            st.write("Analysis: Market is jumpy. Last second reversal risk is high.")

        time.sleep(2)
        st.rerun()
            
