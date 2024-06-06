import os
import sys
import time
import numpy
import pandas
import pathlib
import datetime
import functools
import matplotlib.pyplot as plt

# add source directory to path
sys.path.insert(0, '../src/FinToolsAP/')

import LaTeXBuilder
import LocalDatabase
import PortfolioSorts
import UtilityFunctions

# set printing options
import shutil
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', shutil.get_terminal_size()[0])
pandas.set_option('display.float_format', lambda x: '%.3f' % x)

# directory for loacl wrds database
LOCAL_DB = pathlib.Path('/home/andrewperry/Documents')

def main():

    data_path = pathlib.Path('/home/andrewperry/Nextcloud/Research/Bank Elasticity')
    tab_path = pathlib.Path('/home/andrewperry/Nextcloud/Research/Bank Elasticity/writeup/tables')
    fig_path = pathlib.Path('/home/andrewperry/Nextcloud/Research/Bank Elasticity/writeup/figures')

    DB = LocalDatabase.LocalDatabase(
        save_directory = data_path, 
        database_name = 'BankElasticityDB'
    ) 

    cds_df = DB.queryDB(DB.DBP.Bloomberg.CDS)
    
    cds_df = cds_df.dropna(axis = 0)
    
    # remove citibank (keep citigroup)
    # remove first-citizens 
    # both due to data avaliability
    # Pre shape = (614, 5)
    # Post shape = (587, 5)
    cds_df = cds_df[~cds_df.id.isin(['citibank'])]

    # standardize cds prices    
    cds_df['close_minmax'] = cds_df.close
    cds_df['close_zscore'] = cds_df.close

    cds_df = UtilityFunctions.df_normalize(df = cds_df,
                                           gr = 'idrssd',
                                           vr = 'close_minmax',
                                           method = 'minmax'
                                        )
    
    cds_df = UtilityFunctions.df_normalize(df = cds_df,
                                           gr = 'idrssd',
                                           vr = 'close_zscore',
                                           method = 'zscore'
                                        )
    
    cds_df = cds_df.set_index('date')
    f, a = plt.subplots(cds_df.fullname.nunique(), 1, figsize = (20, 30), tight_layout = True)
    for i, (name, grp) in enumerate(cds_df.groupby(by = 'fullname')):
        grp.close_minmax.plot(ax = a[i])
        a[i].set_title(name)
    plt.show()

if __name__ == '__main__':
    main()