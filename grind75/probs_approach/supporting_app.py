import streamlit as st
import json
import pathlib
import sqlite3


st.set_page_config(layout='wide')

st.title("Grind 75: Problems and Approaches.")
current_dir = pathlib.Path(__file__).parent.resolve()
questions_data = current_dir / "structured_data.json"
files_location = questions_data.resolve()

with open(files_location, 'r') as ques:
    q_data = json.load(ques)

unique_topics = list(q_data.keys()) 

select_topic = st.selectbox(label='topic',
                            options=unique_topics,)

filtered_slugs = [item['slug'] for item in q_data[select_topic]]
select_question = st.selectbox(label='Questions',
                               options=filtered_slugs)


get_slug_idx = filtered_slugs.index(select_question)

# print(get_slug_idx)
# data = approach_json[get_slug_idx]
question = q_data[select_topic][get_slug_idx]

title, complete = st.columns(2)

title.markdown(f"### {question['slug']}")
complete.markdown(f"Commenting Completed : {question['commented']}")

st.markdown("### Challenge Statement")
st.write(question['challenge'])

st.markdown("### Leetcode Link")
st.write(question["url"])

with st.expander('See Approach', expanded=False):
    st.write(question['approach'])

# ----- Commenting and Uncommenting ------ #
if not question['commented']:
    done_comment = st.button('Commenting Done')

    if done_comment:
        print('Comment status updated')
        q_data[select_topic][get_slug_idx]['commented'] = True 
        with open(files_location, 'w') as updt:
            json.dump(q_data, updt)

        st.rerun()
else:
    uncomment = st.button('Not Commented')
    if uncomment:
        print('Comment status falsed')
        q_data[select_topic][get_slug_idx]['commented'] = False
        with open(files_location, 'w') as updt:
            json.dump(q_data, updt)
        st.rerun()
# ----- Commenting and Uncommenting ------ #
