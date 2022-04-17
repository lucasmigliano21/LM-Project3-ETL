def dataframe_cleaning(df):
    ''' Changing date to year in order to work with years '''
    df_new = df.drop(['tournament','neutral','city','country'], axis=1, inplace=True) 
    return df_new





def drop22(df_new):
    ''' Changing date to year in order to work with years '''
    df_new2 = df.drop(['neutral'],axis=1,inplace=True)
    return df_new2

    #    df_new['date'] = df['date'].astype('datetime64')
    #df_new['date'] = df['date'].dt.year
   # df_new.rename(columns = {'date':'year'}, inplace = True)