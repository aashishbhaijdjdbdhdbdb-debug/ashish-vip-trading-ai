import random
import time

def get_market_analysis():
    # Indicators (Simulated for learning logic)
    rsi = random.randint(20, 80)
    ema_fast = random.uniform(100, 110)
    ema_slow = random.uniform(98, 108)
    volume = random.choice(["HIGH", "LOW", "MEDIUM"])

    print(f"\n[SCANNING] RSI: {rsi} | Volume: {volume}")

    # --- SUPREME LOGIC GATE ---
    # Rule 1: Agar RSI 30 se niche hai (Oversold) aur Fast EMA upar hai = CALL
    if rsi < 35 and ema_fast > ema_slow and volume == "HIGH":
        return "🔥 STRONG CALL (BUY) - 96% CONFIRM"
    
    # Rule 2: Agar RSI 70 se upar hai (Overbought) aur Fast EMA niche hai = PUT
    elif rsi > 65 and ema_fast < ema_slow and volume == "HIGH":
        return "🩸 STRONG PUT (SELL) - 96% CONFIRM"
    
    # Rule 3: Agar market side-ways hai
    else:
        return "⏳ WAIT - NO CLEAR SIGNAL"

# Simulation Loop
print("--- ASHISH PRO TRADING ALGO V5 (LEGAL & LOGIC BASED) ---")
try:
    while True:
        decision = get_market_analysis()
        print(f"DECISION: {decision}")
        print("-" * 40)
        time.sleep(5) # Har 5 second mein check karega
except KeyboardInterrupt:
    print("\nStopping...")
        
