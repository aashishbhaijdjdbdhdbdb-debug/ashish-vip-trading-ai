import streamlit as st
import yfinance as yf

# Page Configuration
st.set_page_config(page_title="Ashish VIP AI", layout="centered")

# App Header
st.title("📊 Ashish VIP Trading AI")
st.markdown("---")
st.write("Welcome Ashish bhai! Market select kijiye aur signal dekhiye.")

# Market Selection
option = st.selectbox('Kaunsa Market dekhna hai?', ('NIFTY 50', 'BANK NIFTY', 'USD/INR', 'GOLD'))

ticker_map = {
    'NIFTY 50': '^NSEI',
    'BANK NIFTY': '^NSEBANK',
    'USD/INR': 'INR=X',
    'GOLD': 'GC=F'
}

# Signal Generation
if st.button('GET LIVE SIGNAL'):
    with st.spinner('AI analysis kar raha hai...'):
        # Data fetching
        data = yf.download(ticker_map[option], period='1d', interval='1m')
        
        if not data.empty:
            current_price = data['Close'].iloc[-1]
            open_price = data['Open'].iloc[0]
            
            st.metric(label=f"Current Price ({option})", value=f"{current_price:.2f}")
            
            # Call/Put Logic
            if current_price > open_price:
                st.success("🚀 **CALL SIGNAL:** Market Bullish hai. Price upar ja raha hai!")
            else:
                st.error("📉 **PUT SIGNAL:** Market Bearish hai. Price niche gir raha hai!")
        else:
            st.warning("Data nahi mila. Shayad market abhi band hai.")

st.markdown("---")
st.caption("Developed for Ashish - Personal Use Only")
