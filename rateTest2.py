import yfinance

df = yfinance.download("KRW=X")

print(df)
now_rate = df['Close'][-1] # 현재 환율
print(df['Close'][-1])