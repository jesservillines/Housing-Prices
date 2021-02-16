
import numpy as np
import pandas as pd
import pickle
import streamlit as st
from sklearn.linear_model import lasso


st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
)

st.title('Home Buyers Toolbox!')

st.write('Use the sidebar to select a page to view.')
st.write(np.__version__)

page = st.sidebar.selectbox(
    'Page',
    ('Home', 'Form')
)

# @st.cache
# def load_data():
#     df = pd.read_csv('data/austen_poe.csv')
#     return df

if page == 'Home':
    st.subheader('Home Page')
    st.write('Hello, welcome to the Home Buyers Toolbox!')

if page == 'Form':
    # header
    st.subheader('Home Qualities')
    st.write('''Input the qualities of the home
    for which you want the price predicted.''')

    # get user input
    neigh_qual = st.number_input('Neighboorhood Quality Index', format='%d', min_value=int(0), value=int(0))
    local_feature = st.number_input('Local Positive Features', format='%d', min_value=int(0), value=int(0))
    single_story = st.number_input('Single Story Building', format='%d', min_value=int(0), step=1, value=int(0))
    multi_story = st.number_input('Multiple Story Building', format='%d', min_value=int(0), step=1, value=int(0))

    data = np.array([neigh_qual, local_feature, single_story, multi_story]).reshape(1, -1)

    st.subheader('Make a prediction')

    with open('./model/model_ames.p', 'rb') as pickle_in:
        model = pickle.load(pickle_in)

    predicted_price = model.predict(data)[0]

    st.subheader('Results:')
    st.write(f'Your home is worth {round(predicted_price, 2)}. Go you!')
