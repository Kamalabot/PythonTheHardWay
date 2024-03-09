from pathlib import Path
import json

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
    # assign the topic_related_data to the topic key in the dictionary
    question_dict[topic] = topic_related_data

# write out the dictionary
with open('structured_data.json', 'w') as struc:
    json.dump(question_dict, struc)
