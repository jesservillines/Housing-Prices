
import numpy as np
import pandas as pd
import pickle
import streamlit as st
#from sklearn.linear_model import lasso


st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
)

st.title('Home Buyers Toolbox!')

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
    st.write('Hello, welcome to the Home Buyers Toolbox!')

if page == 'Form':
    # header
    st.subheader('Home Qualities')
    st.write('''Input the qualities of your desired home.''')

    # get user input
    neigh_qual = st.number_input('Neighboorhood Quality Index', format='%d', min_value=int(0), value=int(0))
    overall_qual = st.number_input('Overall Building Quality', format='%d', min_value=int(0), step=1, value=int(0))
    local_feature = st.number_input('Local Positive Features', format='%d', min_value=int(0), value=int(0))
    outside = st.number_input('Outside Grill Space', format='%d', min_value=int(0), step=100, value=int(0))
    shop = st.number_input('Shop Space', format='%d', min_value=int(0), step=100, value=int(0))
    cars_garage = st.number_input('Additional Car Garag', format='%d', min_value=int(0), step=1, value=int(0))
    age = st.number_input('Building Age', format='%d', min_value=int(0), step=1, value=int(0))
    room_size = st.number_input('Size of Rooms', format='%d', min_value=int(0), step=1, value=int(0))
    basement_qual = st.number_input('Basement Quality', format='%d', min_value=int(0), step=1, value=int(0))
    basement_ceiling = st.number_input('Basement Ceiling Height', format='%d', min_value=int(0), step=1, value=int(0))
    bsmt = st.number_input('Finished Basement Sqft', format='%d', min_value=int(0), step=100, value=int(0))
    kitchen = st.number_input('Kitchen Quality', format='%d', min_value=int(0), step=1, value=int(0))
    fire = st.number_input('Fireplace Quality', format='%d', min_value=int(0), step=1, value=int(0))
    upstairs = st.number_input('Finished Upstairs Sqft', format='%d', min_value=int(0), step=1, value=int(0))
    rooms = st.number_input('Rooms Upstairs', format='%d', min_value=int(0), step=1, value=int(0))
    remodel = st.number_input('Remodeled Building', format='%d', min_value=int(0), step=1, value=int(0))
    single_story = st.number_input('Single Story Building', format='%d', min_value=int(0), step=1, value=int(0))
    multi_story = st.number_input('Multiple Story Building', format='%d', min_value=int(0), step=1, value=int(0))
    middle_townhouse = st.number_input('Middle-unit Townhouse', format='%d', min_value=int(0), step=1, value=int(0))
    end_townhouse = st.number_input('End-unit Townhouse', format='%d', min_value=int(0), step=1, value=int(0))
    fam_house = st.number_input('Family House', format='%d', min_value=int(0), step=1, value=int(0))
    exter_qual = st.number_input('External Quality', format='%d', min_value=int(0), step=1, value=int(0))
    type_exter = st.number_input('Type of External Building Feature', format='%d', min_value=int(0), step=1, value=int(0))
    roof_qual = st.number_input('High Roof Quality', format='%d', min_value=int(0), step=1, value=int(0))
    vaneer_sqft = st.number_input('Masonry Vaneer Sqft', format='%d', min_value=int(0), step=100, value=int(0))
    bldg_func = st.number_input('Building Functionality', format='%d', min_value=int(0), step=1, value=int(0))
    lot_front = st.number_input('Lot Frontage', format='%d', min_value=int(0), step=10, value=int(0))
    lot_size = st.number_input('Lot Size', format='%d', min_value=int(0), step=100, value=int(0))
    paved = st.number_input('Paved Driveway', format='%d', min_value=int(0), step=1, value=int(0))
    heater_qual = st.number_input('Heater Quality', format='%d', min_value=int(0), step=1, value=int(0))



    data = np.array([neigh_qual, overall_qual, local_feature, outside, shop,cars_garage, age,room_size,
    basement_qual, basement_ceiling, bsmt, kitchen,fire, upstairs, rooms, remodel, single_story, multi_story, middle_townhouse, end_townhouse,
    fam_house, exter_qual, type_exter, roof_qual, vaneer_sqft, bldg_func, lot_front, lot_size, paved, heater_qual]).reshape(1, -1)

    st.subheader('Make a prediction')

    with open('./model/model_ames.p', 'rb') as pickle_in:
        model = pickle.load(pickle_in)

    predicted_price = model.predict(data)[0]

    st.subheader('Results:')
    st.write(f'Your home is worth {round(predicted_price, 2)}. Go you!')
