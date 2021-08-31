# Let's import some packages
import talib 
import yfinance as yf
import matplotlib.pyplot as plt

# Let's download stock_data and plot it
stock_data = yf.download("AAPL", start="2020-01-01", end="2021-01-01")
plt.plot(stock_data['Close'], color='blue')
plt.title("Daily Close Price (AAPL)")
plt.show()

# Let's calculate the SMA_20 days and the SMA 50 days
stock_data['SMA_20'] = talib.SMA(stock_data['Close'], timeperiod=20)
stock_data['SMA_50'] = talib.SMA(stock_data['Close'], timeperiod=50)

#Let's plot it
plt.plot(stock_data['Close'], color='blue', label='Daily Close Price')
plt.plot(stock_data['SMA_20'], color='green', label='SMA 20')
plt.plot(stock_data['SMA_50'], color='red', label='SMA 50')
plt.legend()
plt.title('Simple Moving Averages')
plt.show()

# Now let calculates the EMA_20 days and the EMA_50 days
stock_data['EMA_20'] = talib.EMA(stock_data['Close'], timeperiod=20)
stock_data['EMA_50'] = talib.EMA(stock_data['Close'], timeperiod=50)
# Let's plot it
plt.plot(stock_data['Close'], color='blue', label='Daily Close Price')
plt.plot(stock_data['EMA_20'], color='green', label='EMA 20')
plt.plot(stock_data['EMA_50'], color='red', label='EMA 50')
plt.legend()
plt.title('Exponential Moving Averages')
plt.show()

# Let's plot also SMA_50 vs EMA_50
plt.plot(stock_data['Close'], color='blue', label='Daily Close Price')
plt.plot(stock_data['SMA_50'], color='green', label='SMA 50')
plt.plot(stock_data['EMA_50'], color='red', label='EMA 50')
plt.legend()
plt.title('SMA 50 vs EMA 50')
plt.show()

# Now we create the ADX and plot it
stock_data['ADX'] = talib.ADX(stock_data['High'], stock_data['Low'], stock_data['Close'], timeperiod=14)
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.set_ylabel('Price')
ax1.plot(stock_data['Close'])
ax2.set_ylabel('ADX')
ax2.plot(stock_data['ADX'], color='green')
ax1.set_title('Daily Close Price and ADX')
ax2.axhline(y = 50, color = 'r', linestyle = '-')
ax2.axhline(y = 25, color = 'r', linestyle = '-')
plt.show()

# To create the MACD we have to code this
macd, macdsignal, macdhist = talib.MACD(stock_data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
# Let's plot it
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.set_ylabel('Price')
ax1.plot(stock_data['Close'])
ax2.set_ylabel('MACD')
ax2.plot(macdsignal, color='green', label='Signal Line')
ax2.plot(macd, color='red', label='MACD')
ax2.bar(macdhist.index, macdhist, color='purple')
ax1.set_title('Daily Close Price and MACD')
plt.legend()
plt.show()


