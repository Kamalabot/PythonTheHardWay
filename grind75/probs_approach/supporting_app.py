import streamlit as st
import json
import pathlib
st.set_page_config(layout='wide')

st.title("Grind 75: Problems and Approaches.")
current_dir = pathlib.Path(__file__).parent.resolve()
files_location = current_dir / "approach_prob.json"
questions_data = current_dir / "QuestionGroups.json"
files_location = files_location.resolve()
print(files_location)

with open(files_location, 'r') as grind:
    approach_json = json.load(grind)

with open(questions_data, 'r') as ques:
    q_data = json.load(ques)

q_vals = q_data.values()
all_data = []
for qd in q_vals:
    for x in qd:
        all_data.append(x)

num_slider = st.slider('Selector',
                       min_value=0,
                       max_value=74)

data = approach_json[num_slider]
question = all_data[num_slider]

st.markdown(f"### {question['slug']}")

st.markdown("### Challenge Statement")
st.write(data['challenge_statement'])

st.markdown("### Leetcode Link")
st.write(question["url"])

with st.expander('See Approach', expanded=False):
    st.write(data['approach'])
