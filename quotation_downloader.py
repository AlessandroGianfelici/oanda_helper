import pandas as pd
from toad.position import position
from toad.plotter import plot_hist_prices
from toad.constants import oanda_token
from numpy.random import randint
import oandapyV20
import oandapyV20.endpoints.trades as trades
import os, sys
import logging
from datetime import datetime, timedelta

oanda_av_inst_full = pd.read_csv(os.path.join('data', 'available_instruments.csv'), sep='\t')
oanda_av_inst = oanda_av_inst_full['name']

start = datetime(2015, 1, 1)
end = datetime.today()

myPath = '/home/alessandro/Documenti/oanda_helper/data/market_data'

dates = pd.date_range(start, end)

def file_folder_exists(path: str):
    """
    Return True if a file or folder exists.

    :param path: the full path to be checked
    :type path: str
    """
    try:
        os.stat(path)
        return True
    except:
        return False


def select_or_create(path: str):
    """
    Check if a folder exists. If it doesn't, it create the folder.

    :param path: path to be selected
    :type path: str
    """
    if not file_folder_exists(path):
        os.makedirs(path)
    return path


logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y %I:%M:%S%p",
    )

logger = logging.getLogger(__name__)

for strumento in oanda_av_inst:
    logger.info(f"Processing {strumento}...")
    myfolder = select_or_create(os.path.join(myPath, strumento))
    for date in dates:
        mypickle = os.path.join(myPath, strumento,f"{date.strftime('%Y%m%d')}_{strumento}.pickle")
        if file_folder_exists(mypickle):
            #logger.info(f"File {mypickle} already found, skipping")
            continue
        try:
            d1=date.strftime('%Y-%m-%d')
            d2=(date+timedelta(1)).strftime('%Y-%m-%d')
            my_pos = position(strumento)
            history = my_pos.load_history(d1, d2, granularity='M1')
            history.to_pickle(mypickle)
            logger.info(f"Saving file {mypickle}")
        except:
            pass