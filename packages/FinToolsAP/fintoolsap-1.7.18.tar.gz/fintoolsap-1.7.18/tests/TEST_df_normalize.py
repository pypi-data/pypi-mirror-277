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

import collections

# for FutureWarning: downcast object fillna blah blah blah infer_objects(copy = False)
# and the connectorx future warning
import warnings
warnings.simplefilter(action = 'ignore', category = FutureWarning)

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

    # pull in UBPR data and make a full sample
    # find columns that different banks have in common for each table
    columns_used = collections.defaultdict(dict)
    for rssd in list(cds_df.idrssd.unique()):
        _cds_df = cds_df[cds_df.idrssd == rssd]
        _fullname = _cds_df.fullname.unique()[0]
        for i, table in enumerate(DB.DBP.UBPR.TABLES):

            # load data
            table_info = f'UBPR.{table}'
            df = DB.queryDB(table_info, 
                            idrssd = int(rssd), 
                            all_vars = True
                        )

            # subset on dates and remove dumb column
            min_date = _cds_df.date.min()
            max_date = _cds_df.date.max()
            df = df[(df.date >= min_date) & (df.date <= max_date)]

            # front fillna and drop columns that have NaN
            df = df.ffill()
            df = df.dropna(axis = 1, how = 'any')

            # remove columns that are constant
            n_unique = df.nunique()
            cols_to_drop = n_unique[n_unique == 1].index
            df = df.drop(cols_to_drop, axis = 1)

            # remove non numeric columns
            non_numeric_cols = df.select_dtypes(
                exclude = numpy.number
            ).columns
            date_col = df.date
            df = df.drop(columns = non_numeric_cols)

            # add back id column and dates
            df['date'] = date_col
            df['idrssd'] = rssd
            df['fullname'] = _fullname

            # get columns to preform pca on
            pca_col = list(df.columns)
            columns_used[rssd][table] = (pca_col, df)

    # get the columns for each table that every bank has
    cols_by_table = {}
    for table in DB.DBP.UBPR.TABLES:
        list_of_list = [None] * len(list(cds_df.idrssd.unique()))
        for i, rssd in enumerate(list(cds_df.idrssd.unique())):
            list_of_list[i] = columns_used[rssd][table][0]
        
        # make sure every bank has the same columns per table
        cols_by_table[table] = (list(set.intersection(*map(set, list_of_list))))
        if(len(cols_by_table[table]) == 0):
            del cols_by_table[table]

    # combine all tables and banks into one data frame
    # data.shape = (394, 1627)
    dfs_to_concat = []
    for rssd in cds_df.idrssd.unique():
        dfs_to_merge = []
        for table in DB.DBP.UBPR.TABLES:
            _df = columns_used[rssd][table][1]
            _cols = cols_by_table[table]
            _df = _df[_cols]
            dfs_to_merge.append(_df)
        df = functools.reduce(lambda x, y: pandas.merge(x, y, 
                                                        how = 'inner', 
                                                        on = ['date', 'idrssd'], 
                                                        suffixes = (None, '_x')
                                                    ), 
                                                    dfs_to_merge
                                                )
        cols_to_keep = list(df.columns)
        cols_to_keep = [col for col in cols_to_keep if '_x' not in col]
        df = df[cols_to_keep]
        dfs_to_concat.append(df)
    data = pandas.concat(dfs_to_concat)
    
    cds_df = cds_df.drop(columns = ['fullname'])
    data = data.merge(cds_df, how = 'inner', on = ['idrssd', 'date'])

    ## close has 79 NaN values
    #data = data.dropna(axis = 0)

    # there should be no NaNs for PCA
    assert(data.isnull().sum().sum() == 0)
    
    # compute pca for all banks
    # get the first 50 PCs
    NUM_PCS = 50
    pc_cols = [None] * NUM_PCS
    dfs_to_concat = []
    for i, rssd in enumerate(data.idrssd.unique()):
        tmp = data[data.idrssd == rssd]
        tmp = tmp.reset_index(drop = True)
        
        # get columns
        pca_cols = [x for x in tmp.columns if 'ubpr' in x]
        col_var = tmp[pca_cols].var()
        bruh = col_var[col_var == 0].index
        pca_cols = UtilityFunctions.list_diff(pca_cols, bruh)
        
        # pca
        pca_res = UtilityFunctions.pca(X = tmp, vr = pca_cols)
        pcs = pca_res.principal_components[:, :NUM_PCS]
        
        _inpt = {}
        for i in range(NUM_PCS):
            _inpt[f'PC{i + 1}'] = pca_res.principal_components[:, i]
            pc_cols[i] = f'PC{i + 1}'
        _pcs_df = pandas.DataFrame(_inpt)
        
        _pcs_df['idrssd'] = rssd
        _pcs_df['fullname'] = tmp.fullname.unique()[0]
        
        _pcs_df = _pcs_df.merge(tmp[['date', 'close']], 
                                right_index = True,
                                left_index = True)
                   
        dfs_to_concat.append(_pcs_df)
        
    pcs_df = pandas.concat(dfs_to_concat)
    
    print(pcs_df.shape)
    
    pcs_df = UtilityFunctions.df_normalize(df = pcs_df,
                                                      gr = 'idrssd',
                                                      vr = pc_cols,
                                                      method = 'zscore')
    
    print(pcs_df.shape)
    
    print(pcs_df.head(100))

if __name__ == '__main__':
    main()