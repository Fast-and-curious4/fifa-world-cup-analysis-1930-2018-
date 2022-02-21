import streamlit as st
import helper
import pandas as pd
import plotly.express as px
import numpy as np

df=pd.read_csv('world cup_final.csv')
df['Attendance']=(df['Attendance'].str.replace(',','')).astype('int')
df2=pd.read_csv('all cups.csv')
df3=pd.read_csv('worldcupgoals.csv')

st.sidebar.title("FIFA World Cup Analysis(1930-2018)")
st.sidebar.image("soc_g_WCtrophy_d1_1296x729.jpg")
user_menu=st.sidebar.radio(
    'Select an Option',
    ('Overall Analysis','Year wise analysis','Country wise analysis')
)


if user_menu=='Overall Analysis':
    editions=df['Year'].nunique()
    hosts=df['Country'].nunique()
    winner=df['Winner'].nunique()
    matches=df['MatchesPlayed'].sum()
    goals=df['GoalsScored'].sum()
    attendance=df['Attendance'].sum()

    winners=helper.winner_list(df)
    goal_tally=helper.goals_list(df3)

    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.subheader(editions)
    with col2:
        st.header("Hosts")
        st.subheader(hosts)
    with col3:
        st.header("Winners")
        st.subheader(winner)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Total Matches Played")
        st.subheader(matches)
    with col2:
        st.header("Total Goals Scored")
        st.subheader(goals)
    with col3:
        st.header("Total Attendance")
        st.subheader(attendance)

    fig=px.line(df,x='Year',y='Attendance')
    st.title("Audience over the Years")
    st.plotly_chart(fig)

    st.title("Most Successful Teams")
    st.table(winners)

    st.title("Top 10 Goal Scorers")
    st.table(goal_tally)


if user_menu=='Year wise analysis':

    years=helper.year_list(df2)
    selected_year = st.sidebar.selectbox("Select Year",years)
    countries=helper.country_list(df2,selected_year)
    selected_country = st.sidebar.selectbox("Select Country", countries)

    if selected_country=='Overall':

        st.title(str(selected_year) + " FIFA World Cup Overall Statistics")

        st.header('Host')
        st.subheader((df[df['Year']==selected_year]).iloc[0][1])

        col1,col2,col3=st.columns(3)
        with col1:
            st.header('Winner')
            st.subheader((df[df['Year']==selected_year]).iloc[0][2])
        with col2:
            st.header('Runners up')
            st.subheader((df[df['Year']==selected_year]).iloc[0][3])
        with col3:
            st.header('Third place')
            st.subheader((df[df['Year']==selected_year]).iloc[0][4])

        col1,col2,col3=st.columns(3)
        with col1:
            st.header('Qualified Teams')
            st.subheader((df[df['Year']==selected_year]).iloc[0][7])
        with col2:
            st.header('Matches Played')
            st.subheader((df[df['Year']==selected_year]).iloc[0][8])
        with col3:
            st.header('Total Goals scored')
            st.subheader((df[df['Year']==selected_year]).iloc[0][6])

        st.header('Attendance')
        st.subheader((df[df['Year']==selected_year]).iloc[0][9])

    if selected_country!='Overall':

        st.title(str(selected_country) + " Performance in "+ str(selected_year) +" FIFA World Cup")

        games=df2[(df2['year']==selected_year) & (df2['Team']==selected_country)].iloc[0][2]
        win=df2[(df2['year']==selected_year) & (df2['Team']==selected_country)].iloc[0][3]
        draw=df2[(df2['year']==selected_year) & (df2['Team']==selected_country)].iloc[0][4]
        lost=df2[(df2['year']==selected_year) & (df2['Team']==selected_country)].iloc[0][5]
        goals_scored=df2[(df2['year']==selected_year) & (df2['Team']==selected_country)].iloc[0][6]
        goals_against=df2[(df2['year']==selected_year) & (df2['Team']==selected_country)].iloc[0][7]
        points=df2[(df2['year']==selected_year) & (df2['Team']==selected_country)].iloc[0][8]
        position=df2[(df2['year']==selected_year) & (df2['Team']==selected_country)].iloc[0][0]

        col1,col2,col3 = st.columns(3)
        with col1:
            st.header("Games Played")
            st.subheader(games)
        with col2:
            st.header("Matches won")
            st.subheader(win)
        with col3:
            st.header("Matches draw")
            st.subheader(draw)

        col1,col2,col3 = st.columns(3)
        with col1:
            st.header("Matches lost")
            st.subheader(lost)
        with col2:
            st.header("Goals scored")
            st.subheader(goals_scored)
        with col3:
            st.header("Goals against")
            st.subheader(goals_against)

        col1,col2=st.columns(2)
        with col1:
            st.header("Total points scored")
            st.subheader(points)
        with col2:
            st.header("Postion")
            st.subheader(position)


if user_menu=='Country wise analysis':

    all_country=helper.all_countries(df2)
    sel_country=st.sidebar.selectbox("Select Country",all_country)

    top_perf=helper.top_performances(df2,sel_country)
    titles=top_perf[top_perf['Position']=='Winner'].shape[0]
    st.subheader("No. of titles")
    st.subheader(titles)
    st.title("Performance over the Years")
    perf=df2[df2['Team']==sel_country]
    perf.index = np.arange(1, len(perf) + 1)
    st.table(perf)

    if (top_perf.shape[0]>0):
        st.title("Noteworthy Performances")
        st.table(top_perf)

    st.title("Top Goal Scorer")
    name=df3[df3['Country']==sel_country].iloc[0][0]
    goal_top=df3[df3['Country']==sel_country].iloc[0][1]
    years_top=df3[df3['Country']==sel_country].iloc[0][2]
    st.write("Player:",name)
    st.write("Goals Scored:",goal_top)
    st.write("Years_played:",years_top)