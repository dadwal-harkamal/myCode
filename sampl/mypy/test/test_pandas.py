import pandas as pd
rd_fl=pd.read_csv('panda.csv',index_col=0)
print(rd_fl[0:3])