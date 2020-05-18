import pandas as pd
import os
from toad.constants import myPath

def load(symbol, start, end):
    mySerie = pd.DataFrame()
    for date in pd.date_range(start, end):
        try:
            tmp = pd.read_pickle(os.path.join(myPath, 'market_data', symbol, f"{date.strftime('%Y%m%d')}_{symbol}.pickle"))
            mySerie = mySerie.append(tmp)
        except:
            pass
    return mySerie