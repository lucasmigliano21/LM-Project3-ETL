import pandas as pd
import datetime

def column_cleaning(df):
    ''' Changing date to year in order to work with years'''
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year

    '''droping unwanted columns'''
    df = df.drop(['date','tournament','neutral','city','country'], axis=1, inplace=True) 
   
    return df

def filter(df):
    ''' as 'the best' award started to be awarded in 2000, we will keep only rows after 2000'''
    df = df.loc[(df['year'] >= 2000)]
    df.reset_index(drop=True, inplace=True)

    return df

def winner(df):
    ''' extract the winner between teams'''
    df['winner'] = pd.Series(dtype='str')
    df['winner'] = df.apply(lambda x : x['home_team'] if x['home_score'] > x['away_score'] else (x['away_team'] if x['home_score'] < x['away_score'] else 'draw'),
    axis=1)

    return df

def copy(df):

    df = df[['year', 'winner']].copy()
    return df