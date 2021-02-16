
import numpy as np
import pandas as pd
import pickle
import streamlit as st

st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
)

st.title('Ames Predict-O-Matic!')

st.write('Use the sidebar to select a page to view.')

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
    st.write('Hello, World, to my sliiiiick Streamlit App!')

if page == 'Form':
    # header
    st.subheader('Home Qualities')
    st.write('''Input the qualities of the home
    for which you want the price predicted.''')

    # get user input
    qual = st.number_input('Neighboorhood Quality Index', format='%d', min_value=int(0), value=int(0))
    bath = st.number_input('Local Positive Features', format='%d', min_value=int(0), value=int(0))
    garage = st.number_input('Single Story Building', format='%d', min_value=int(0), step=100, value=int(0))
    lot = st.number_input('Multiple Story Building', format='%d', min_value=int(0), step=1000, value=int(0))

    data = np.array([qual, bath, garage, lot]).reshape(1, -1)

    st.subheader('Make a prediction')

    with open('./model/model.p', 'rb') as pickle_in:
        model = pickle.load(pickle_in)

    predicted_price = model.predict(data)[0]

    st.subheader('Results:')
    st.write(f'Your home is worth {round(predicted_price, 2)}. Go you!')
