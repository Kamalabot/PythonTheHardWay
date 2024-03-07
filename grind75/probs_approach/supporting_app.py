import streamlit as st
import json
import pathlib
st.set_page_config(layout='wide')

st.title("Grind 75: Problems and Approaches.")
current_dir = pathlib.Path(__file__).parent.resolve()
files_location = current_dir / "approach_prob.json"
questions_data = current_dir / "QuestionGroups.json"
files_location = files_location.resolve()
# print(files_location)

with open(files_location, 'r') as grind:
    approach_json = json.load(grind)

with open(questions_data, 'r') as ques:
    q_data = json.load(ques)

q_vals = q_data.values()
all_data = []
for qd in q_vals:
    for x in qd:
        all_data.append(x)
# print(type(approach_json))
# bringing the approach and the challenge statement inside all_data
for ind, vals in enumerate(approach_json):
    all_data[ind]['challenge_statement'] = vals['challenge_statement']
    all_data[ind]['approach'] = vals['approach']


unique_topics = set([item['topic'] for item in all_data])
topics_list = list(unique_topics)
# print(topics_list)

select_topic = st.selectbox(label='topic',
                            options=topics_list,)
# num_slider = st.slider('Selector',
                       # min_value=0,
                       # max_value=74)


def filter_topic(item, tgt_topic):
    if item['topic'] == tgt_topic:
        return True


filtered_data = [item for item in all_data if filter_topic(item, select_topic)]

filtered_slugs = [item['slug'] for item in filtered_data]
select_question = st.selectbox(label='Questions',
                               options=filtered_slugs)


get_slug_idx = filtered_slugs.index(select_question)

# print(get_slug_idx)
# data = approach_json[get_slug_idx]
question = filtered_data[get_slug_idx]

st.markdown(f"### {question['slug']}")

st.markdown("### Challenge Statement")
st.write(question['challenge_statement'])

st.markdown("### Leetcode Link")
st.write(question["url"])

with st.expander('See Approach', expanded=False):
    st.write(question['approach'])
