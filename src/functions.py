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
    ''' as 'the best' award started to be awarded in 2000 but Champions League has been played since 2002, we will keep only rows after 2002'''
    df = df.loc[(df['year'] >= 2002)]
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


def transform(i):
    lst = []
    for i in players:
        i = i.text.replace('\n', ',,,').replace('  ', ',,,').split(',,,')
        lst.append(i)
    return lst



def replacing(cham):
    ''' replacing rows'''
    cham['Champion'] = cham["Winner"] + " " + cham["Country"]
    cham['Champion']=[c.replace('1. FFC', 'FFC Frankfurt') for c in cham.Champion]
    cham['Champion']=[c.replace('1.', 'FFC Frankfurt') for c in cham.Champion]
    cham = cham.drop(['Winner','Country'], axis=1)
    cham['a']=[c.replace('Frankfurt', 'Germany') for c in cham.a]
    cham['a']=[c.replace('Duisburg', 'Germany') for c in cham.a]
    cham['a']=[c.replace('FF', 'Sweden') for c in cham.a]
    cham = cham.drop('b', axis=1)
    cham.rename(columns = {'a':'Country'}, inplace = True)
    cham = cham.sort_values(by = ['Year'], ascending=True).reset_index().drop('index',axis=1)
    cham['Champion']=[c.replace('Umeå IK', 'Umea IK') for c in cham.Champion]
    cham['Champion']=[c.replace('VfL Wolfsburg', 'Wolfsburg') for c in cham.Champion]
    return cham 