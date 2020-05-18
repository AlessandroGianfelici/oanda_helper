import pandas as pd
import oandapyV20
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.trades as trades
from toad.constants import oanda_token, accountID


client = oandapyV20.API(access_token=oanda_token, environment="live")

r = accounts.AccountInstruments(accountID=accountID)
client.request(r)
test = r.response['instruments']
test_df = pd.DataFrame(test)
#test_df = test_df.loc[test_df['type'] != 'CFD'] #tolgo i derivati
test_df.to_csv('data/available_instruments.csv', sep='\t')
print(test_df)
