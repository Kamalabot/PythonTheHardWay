import streamlit as st
import json
import pathlib
import sqlite3


st.set_page_config(layout='wide')


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)

    return conn


def select_question_by_topic(conn, topic):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param topic:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM chalap WHERE topic=?", (topic,))

    rows = cur.fetchall()

    return rows


def select_question_by_slug(conn, slug):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param slug:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM chalap WHERE slug=?", (slug,))

    rows = cur.fetchall()
    # print(rows)
    return rows


def update_comment(conn, comment, slug):
    """
    update comment status of a question
    :param conn:
    :param question:
    :return: project id
    """
    sql = ''' UPDATE chalap
              SET commented = ?
              WHERE slug = ?'''
    cur = conn.cursor()
    cur.execute(sql, (comment, slug))
    conn.commit()


st.title("Grind 75: Problems and Approaches.")
current_dir = pathlib.Path(__file__).parent.resolve()
questions_data = current_dir / "structured_data.json"
db_file = current_dir / "solution_approach.db"
files_location = questions_data.resolve()

with open(files_location, 'r') as ques:
    q_data = json.load(ques)

unique_topics = list(q_data.keys())

select_topic = st.selectbox(label='topic',
                            options=unique_topics,)

conn = create_connection(db_file=db_file)
# print('created db conn')
topicwise_question = select_question_by_topic(conn, select_topic)
# print(topicwise_question)
filtered_slugs = [item[2] for item in topicwise_question]

select_question = st.selectbox(label='Questions',
                               options=filtered_slugs)
print(select_question)

question = select_question_by_slug(conn, select_question)[0]
# print(question)
title, complete = st.columns(2)

title.markdown(f"### {question[2]}")
complete.markdown(f"Commenting Completed : {question[-1]}")

st.markdown("### Challenge Statement")
st.write(question[3])

st.markdown("### Leetcode Link")
st.write(question[5])

with st.expander('See Approach', expanded=False):
    st.write(question[6])

# ----- Commenting and Uncommenting ------ #
if not question[-1]:
    done_comment = st.button('Commenting Done')

    if done_comment:
        print('Comment status updated')
        with conn:
            update_comment(conn, 1, select_question)
        st.rerun()
else:
    uncomment = st.button('Not Commented')
    if uncomment:
        print('Comment status falsed')
        update_comment(conn, 0, select_question)
        st.rerun()
# ----- Commenting and Uncommenting ------ #
