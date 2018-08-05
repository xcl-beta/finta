import pytest
import os
import pandas as pd
from finta import TA
import talib


@pytest.fixture
def rootdir():

    return os.path.dirname(os.path.abspath(__file__))


data_file = os.path.join(rootdir(), 'data/bittrex:btc-usdt.csv')

ohlc = pd.read_csv(data_file, index_col='date',
                   parse_dates=True)


def test_sma():
    '''test TA.SMA'''

    ma = TA.SMA(ohlc, 14)
    talib_ma = talib.SMA(ohlc['close'], timeperiod=14)

    assert round(talib_ma[-1], 6) == round(ma.values[-1], 6)


def test_ema():
    '''test TA.EMA'''

    ma = TA.EMA(ohlc, 50)
    talib_ma = talib.EMA(ohlc['close'], timeperiod=50)

    assert round(talib_ma[-1], 6) == round(ma.values[-1], 6)


def test_dema():
    '''test TA.DEMA'''

    ma = TA.DEMA(ohlc, 50)
    talib_ma = talib.DEMA(ohlc['close'], timeperiod=50)

    assert round(talib_ma[-1], 6) == round(ma.values[-1], 6)


def test_tema():
    '''test TA.TEMA'''

    ma = TA.TEMA(ohlc, 50)
    talib_ma = talib.TEMA(ohlc['close'], timeperiod=50)

    assert round(talib_ma[-1], 6) == round(ma.values[-1], 6)


def test_trima():
    '''test TA.TRIMA'''

    ma = TA.TRIMA(ohlc, 30)
    talib_ma = talib.TRIMA(ohlc['close'])

    assert round(talib_ma[-1], 6) == round(ma.values[-1], 6)


def test_trix():
    '''test TA.TRIX'''

    ma = TA.TRIX(ohlc, 20)
    talib_ma = talib.TRIX(ohlc['close'], timeperiod=20)

    assert round(talib_ma[-1], 6) == round(ma.values[-1], 6)


def test_tr():
    '''test TA.TR'''

    tr = TA.TR(ohlc)
    talib_tr = talib.TRANGE(ohlc['high'], ohlc['low'], ohlc['close'])

    assert round(talib_tr[-1], 6) == round(tr.values[-1], 6)


def test_atr():
    '''test TA.ATR'''

    tr = TA.ATR(ohlc, 14)
    talib_tr = talib.ATR(ohlc['high'], ohlc['low'], ohlc['close'],
                         timeperiod=14)

    assert round(talib_tr[-1], 6) == round(tr.values[-1], 6)


def test_mom():
    '''test TA.MOM'''

    mom = TA.MOM(ohlc, 15)
    talib_mom = talib.MOM(ohlc['close'], 15)

    assert round(talib_mom[-1], 6) == round(mom.values[-1], 6)


def test_rsi():
    '''test TA.RSI'''

    rsi = TA.RSI(ohlc, 9)
    talib_rsi = talib.RSI(ohlc['close'], 9)

    assert int(talib_rsi[-1]) == int(rsi.values[-1])


def test_mfi():
    '''test TA.MFI'''

    mfi = TA.MFI(ohlc, 9)
    talib_mfi = talib.MFI(ohlc['close'], 9)

    assert int(talib_mfi[-1]) == int(mfi.values[-1])


def test_bbands():
    '''test TA.BBANDS'''

    bb = TA.BBANDS(ohlc, 20)
    talib_bb = talib.BBANDS(ohlc['close'], timeperiod=20, nbdevup=2, 
                            bdevdn=2, matype=0)

    assert round(bb['BB_UPPER'][-1], 6) == round(talib_bb[0].values[-1], 6)
