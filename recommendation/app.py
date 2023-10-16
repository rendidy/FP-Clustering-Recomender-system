import streamlit as st
import prediction
import recommend_deploy

navigation = st.sidebar.selectbox('Pages:', ('Cluster Prediction', 'Recommendation System'))

if navigation == 'Cluster Prediction':
    prediction.run()
else:
    recommend_deploy.run()