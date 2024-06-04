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

    x1 = numpy.random.normal(loc = 0, scale = 1, size = 10)
    x2 = numpy.random.normal(loc = 100, scale = 20, size = 10)
    x3 = ['a'] * 5
    x3.extend(['b'] * 5)
    x4 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    
    _input = {'col1': x1, 'col2': x2, 'col3': x3, 'col4': x4}
    
    df = pandas.DataFrame(_input)
    
    print(df)
    print(df.groupby(by = 'col3').describe())
    
    df = UtilityFunctions.df_normalize(df, gr = 'col3', method = 'log')

    print(df)
    print(df.groupby(by = 'col3').describe())

if __name__ == '__main__':
    main()