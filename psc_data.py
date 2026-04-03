#%%
import numpy as np
import pandas as pd

#yahoo finance
import yfinance as yf #using yahoo finance as main source

#plot
# import matplotlib.pyplot as plt
# import plotly.express as px
# import seaborn as sns

#date time
import datetime as datetime
from datetime import timedelta, datetime
#%%
#get date time
today_date = datetime.today().date()

#%%

#fill psc list here / either manually fill or import file
ks_psc = ['ALAB','BE','CRDO','FN','RKLB','TSEM']
#%%
rows = []
for t in ks_psc:
    info = yf.Ticker(t).info
    rows.append({
        "ticker": t,
        "name": info.get("longName"),
        "exchange": info.get("exchange"),
        "currency": info.get("currency"),
        "marketCap": info.get("marketCap"),
        "sharesOutstanding": info.get("sharesOutstanding"),
    })

df_info = pd.DataFrame(rows)

shares_out = np.array(df_info.sharesOutstanding)

#%% get last 4 quarter data
df=yf.download(ks_psc, start="2025-01-01", end='2026-03-31')['Close']

df = df*1.

#perform multiplcation to get daily market cap
df = shares_out * df

#group by quarter ???

#
#df.to_csv('output/csv/psc_stocks_close.csv')
#%% 1.
