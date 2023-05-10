"""
The python file to run the strategies

"""

import configparser
import Supertrend as st
import sys
sys.path.append('C:/Users/sawan/Projects/QuantBinary')
import Base.utilities.utils as utils
# import Robin.robin as robin
import datetime


config = configparser.ConfigParser()
config.read('config.ini')

# API keys and secret keys
api_key = str(config.get('DEFAULT', 'api_key'))
secret_key = str(config.get('DEFAULT', 'secret_key'))

yr, month, day = (int(config.get('DEFAULT', 'start_date_yr')), int(config.get('DEFAULT', 'start_date_month')), int(config.get('DEFAULT', 'start_date_day')))


data = utils.get_historical_stock_data(api_key, secret_key, str(config.get('DEFAULT', 'ticker')), start_date=datetime.datetime(yr, month, day))
# print(data.head())
# print("Output")

investment = float(config.get('DEFAULT', 'investment'))
commission = float(config.get('DEFAULT', 'commission'))
share = int(config.get('DEFAULT', 'share'))
lookback = int(config.get('DEFAULT', 'lookback'))
period = int(config.get('DEFAULT', 'period'))
periods = [int(i) for i in (config.get('DEFAULT', 'periods').split(' '))]
multipliers = [float(i) for i in (config.get('DEFAULT', 'multipliers')).split(' ')]
ema_period = float(config.get('DEFAULT', 'ema_period'))


# st.backtest_supertrend(data, investment = investment)
# st.backtest_supertrend_with_mcginley(data, investment=investment)
# st.backtest_supertrend_with_ema_and_mcginley(data, investment=investment)
# st.triple_bullish_with_ema(data, investment=100000, multipliers=multipliers, periods=periods, ema_period=ema_period)

def __init__():
    strategies = (config.get('DEFAULT', 'strategy').split(' '))
    for strategy in strategies:
        if strategy is '1':
            print('Backtesting Supertrend Strategy: ')
            st.backtest_supertrend(data, investment=investment, commission=commission, share=share)
            print()

        if strategy is '2':
            print('Backtesting Supertrend with McGinley Strategy: ')
            st.backtest_supertrend_with_mcginley(data, investment=investment, commission=commission, share=share, lookback=lookback)
            print()

        if strategy is '3':
            print('Backtesting Supertrend with EMA and McGinley Strategy: ')
            st.backtest_supertrend_with_ema_and_mcginley(data, investment=investment, commission=commission, share=share, period=period, lookback=lookback)
            print()

        if strategy is '4':
            print('Backtesting Triple Bullish Trend Strategy: ')
            st.triple_bullish_trend(data, investment=investment, multipliers=multipliers, commission=commission, share=share, periods=periods)
            print()

        if strategy is '5':
            print('Backtesting Triple Bullish trend with EMA Strategy: ')
            st.triple_bullish_with_ema(data, investment=investment, multipliers=multipliers, commission=commission, share=share, periods=periods, ema_period=ema_period)
            print()

__init__()