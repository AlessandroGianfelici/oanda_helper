import pandas as pd
import numpy as np
import oandapyV20
import oandapyV20.endpoints.instruments as instruments
from toad.constants import oanda_token, newsapi_token
from toad.domain import Measurement


# qual'è lo scopo di questo modulo? se ho ben inteso, serve a recuperare i dati dei pagamenti indipendentemente dalla api che usiamo
class position:

    def __init__(self, name):

        self.name = name
        # mi salvo anche le connessioni come delle variabili di classe, così non devo ricrearle ogni volta
        self.quote_connection = oandapyV20.API(
            access_token=oanda_token, environment="live")

    def toMeasurement(self, oanda_input):
        volume = oanda_input["volume"]
        bid = oanda_input["bid"]
        ask = oanda_input["ask"]
        time = oanda_input["time"]
        return Measurement(self.name, "oanda", time,  ask["c"], bid["c"], ask["h"], bid["h"], ask["l"], bid["l"], ask["o"], bid["o"], volume)

    def get_day_data(self, day, granularity='M1'):
        day_start = f"{day}T00:00:00"
        day_end = f"{day}T23:59:59"
        params = {'granularity': granularity,
                  'from': day_start,
                  'to': day_end,
                  'price': 'BMA'}
        oanda_req = instruments.InstrumentsCandles(
            instrument=self.name, params=params)
        self.quote_connection.request(oanda_req)
        oanda_output = oanda_req.response['candles']
        if len(oanda_output) < 1:
            raise ValueError("candles empty, can't retrieve bid data")
        else:
            return map(self.toMeasurement, oanda_output)

    def get_last_prices(self):

        return None

    # mi aspetterei che tornasse Measurement, cioè una semplice classe di dati read-only indipendente dalle api
    def load_history(self, d1, d2, granularity):

        # l'idea che avevo avuto era che questo metodo popolasse sia self.historical_prices che self.historical_news, ma per ora popola solo i prezzi
        params = {'granularity': granularity,
                  'from': d1,
                  'to': d2,
                  'price': 'BMA'}

        oanda_req = instruments.InstrumentsCandles(
            instrument=self.name, params=params)
        self.quote_connection.request(oanda_req)
        oanda_output = oanda_req.response
        oanda_df = pd.DataFrame(data=oanda_output['candles'])
        # warning: ci sono dei buchi nella colonna time, bisognerebbe indagare
        oanda_df['time'] = pd.to_datetime(oanda_df['time'])
        oanda_df = oanda_df.set_index('time')

        oanda_df['closeAsk'] = oanda_df['ask'].apply(
            lambda x: np.float32(x['c']))
        oanda_df['closeBid'] = oanda_df['bid'].apply(
            lambda x: np.float32(x['c']))

        oanda_df['highAsk'] = oanda_df['ask'].apply(
            lambda x: np.float32(x['h']))
        oanda_df['highBid'] = oanda_df['bid'].apply(
            lambda x: np.float32(x['h']))

        oanda_df['lowAsk'] = oanda_df['ask'].apply(
            lambda x: np.float32(x['l']))
        oanda_df['lowBid'] = oanda_df['bid'].apply(
            lambda x: np.float32(x['l']))

        oanda_df['openAsk'] = oanda_df['ask'].apply(
            lambda x: np.float32(x['o']))
        oanda_df['openBid'] = oanda_df['bid'].apply(
            lambda x: np.float32(x['o']))

        return oanda_df[['closeAsk', 'closeBid', 'highAsk', 'highBid', 'lowAsk', 'lowBid', 'openAsk', 'openBid', 'volume']]
