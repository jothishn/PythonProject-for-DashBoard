
import pandas as pd
import plotly.express as px
import streamlit as st

dash=pd.read_csv("C:\\Users\\JOTHISH N\\Desktop\\my project\\DASHBOARD.csv")

st.set_page_config(page_title='T20 MATCHES',layout="wide")
st.header('T20 Results')
#st.subheader('Winner details')

team= dash['team'].unique().tolist()

st.sidebar.title("Teams")
option=st.sidebar.selectbox("Teams",(team))

team_1 = dash['team'] == option
bar_chart = px.bar(dash[team_1],x='year',y='win_runs',template='plotly_dark',color_discrete_sequence=['green'])
bar_chart.update_yaxes(showgrid=False)
line_chart = px.line(dash[team_1],x='year',y='win_times',template="plotly_dark",color_discrete_sequence=['blue'])
line_chart.update_yaxes(showgrid=False)
left_column, right_column=st.columns(2)
left_column.plotly_chart(bar_chart,use_container_width=True)
right_column.plotly_chart(line_chart,use_container_width=True)
tree = px.treemap(dash[team_1], path=[px.Constant(option), 'year', 'win_bowling'],values='year',color='win_bowling',hover_data=['year'],color_discrete_sequence=['turquoise'],color_continuous_scale='PuBu')
st.plotly_chart(tree)


pie_1=px.pie(dash[team_1],'year','loss',hole=.4)
pie_2=px.pie(dash[team_1],'year','win_times')


left_column, right_column=st.columns(2)
left_column.plotly_chart(pie_1,use_container_width=True)
right_column.plotly_chart(pie_2,use_container_width=True)