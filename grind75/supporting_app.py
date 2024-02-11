import streamlit as st
import json
import pathlib
st.set_page_config(layout='wide')

st.title("Grind 75: Problems and Approaches.")
current_dir = pathlib.Path(__file__).resolve()
files_location = current_dir / "approach_prob.json"
files_location = "approch_prob.json"

with open(files_location, 'r') as grind:
    approach_json = json.load(grind)

num_slider = st.slider('Selector',
                       min_value=0,
                       max_value=74)

data = approach_json[num_slider]

st.write(data['challenge_statement'])

with st.expander('See Approach', expanded=False):
    st.write(data['Approcach'])
