import pandas as pd
import oandapyV20
import oandapyV20.endpoints.accounts as accounts
from constants import accountID, oanda_token

client = oandapyV20.API(access_token=oanda_token)

r = accounts.AccountInstruments(accountID=accountID)
client.request(r)
test = r.response['instruments']
test_df = pd.DataFrame(test)
test_df = test_df.loc[test_df['type'] != 'CFD'] #tolgo i derivati
test_df.to_csv('available_instruments.csv', sep='\t')
test_df
