import pandas as pd
import numpy as np

def year_list(data):
    years = data['year'].unique().tolist()
    years.sort()
    return years

def country_list(df,year):
    df_=df[df['year']==year]
    country=df_['Team'].unique().tolist()
    country.sort()
    country.insert(0,'Overall')

    return country

def winner_list(df):
    df_=pd.DataFrame(df['Winner'].value_counts())
    df_.reset_index(inplace=True)
    arr=[]
    for country in df_['index'].values:
        lis=(df[df['Winner']==country])['Year'].values
        arr.append(lis)
    df_['years']=arr
    df_['years']=df_['years'].astype('str')
    df_['years']=df_['years'].str.strip('[]')
    df_['years']=df_['years'].str.split(' ')
    df_['years']=df_['years'].str.join(",")
    df_.index = np.arange(1, len(df_) + 1)

    return df_

def goals_list(df):
    df.index = np.arange(1, len(df) + 1)
    goal_tally=df.head(10)

    return goal_tally

def all_countries(df):
    all_countries=df['Team'].unique().tolist()
    all_countries.sort()

    return all_countries

def top_performances(df,country):
    df_=df[(df['Team']==country) & (df['Position']<=4)]
    df_=df_.iloc[:,[0,9]]
    dict={1:'Winner',2:'Runners-Up',3:'Third',4:'Fourth'}
    df_.replace({'Position':dict},inplace=True)
    df_.index = np.arange(1, len(df_) + 1)

    return df_

