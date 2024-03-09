from pathlib import Path
import json
import sqlite3


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


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)


def create_question(conn, question):
    """
    Create a new question 
    :param conn:
    :param question:
    :return:
    """
    sql = ''' INSERT INTO chalap(topic,slug,challenge,approach,url,commented)
              VALUES(?,?,?,?,?,?); '''
    cur = conn.cursor()
    cur.execute(sql, question)
    conn.commit()

    return cur.lastrowid


def update_comment(conn, question):
    """
    update comment status of a question 
    :param conn:
    :param question:
    :return: project id
    """
    sql = ''' UPDATE chalap 
              SET commented = ? ,
              WHERE slug = ?'''
    cur = conn.cursor()
    cur.execute(sql, question)
    conn.commit()


current_dir = Path(__file__).parent.resolve()
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

# bringing the approach and the challenge statement inside all_data
for ind, vals in enumerate(approach_json):
    all_data[ind]['challenge_statement'] = vals['challenge_statement']
    all_data[ind]['approach'] = vals['approach']
    all_data[ind]['commented'] = False

# get the unique topics
unique_topics = list(set([data['topic'] for data in all_data]))
print('cheking unique topics: ', unique_topics)

db_file = current_dir / 'solution_approach.db'
conn = create_connection(db_file=db_file)
print('created database')
sql_create_topic_table = """CREATE TABLE IF NOT EXISTS chalap (
                                id integer PRIMARY KEY,
                                topic text NOT NULL,
                                slug text NOT NULL,
                                challenge text NOT NULL,
                                approach text NOT NULL,
                                url text NOT NULL,
                                commented bool NOT NULL
                            );"""

if conn is not None:
    create_table(conn, sql_create_topic_table)
    print("created table")

question_dict = dict()  # create a dictionary store
# enumerate on the topics
for ind, topic in enumerate(unique_topics):
    # filter the all_data list based on the topic on hand
    topic_list = [data for data in all_data if data['topic'] == topic]
    print(f'Problem related to {topic} is {len(topic_list)}')
    # create a store for topic related data
    topic_related_data = []
    for data in topic_list:  # enumerate the data in topic_list
        print(f"append slug {data['slug']}")
        # build a dictionary
        build_dict = dict({
            'slug': data['slug'],
            'challenge': data['challenge_statement'],
            'approach': data['approach'],
            'url': data['url'],
            'commented': False
        })
        # append the dictionary to the topic_list
        topic_related_data.append(build_dict)
        with conn:
            # create data for table
            question_tuple = (topic, data['slug'], data['challenge_statement'],
                              data['approach'], data['url'], False)
            # write to table
            create_question(conn, question_tuple)
    # assign the topic_related_data to the topic key in the dictionary
    question_dict[topic] = topic_related_data
print('Completed writing data to database')
# # write out the dictionary
# with open('structured_data.json', 'w') as struc:
    # json.dump(question_dict, struc)
