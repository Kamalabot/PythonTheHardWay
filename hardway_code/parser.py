#subject = ['player','you']
#verb = ['go', 'kill', 'eat', 'come', 'fight', 'lift']
#stop = ['the', 'in', 'it', 'of', 'a', 'an','from','to']
#object = ['bear', 'princess', 'eyes', 'sword', 'gun']
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

class Sentence(object):
    def __init__(self,sub,obj,verb):
        self.sub = sub
        self.obj = obj
        self.verb = verb

def split_sent(sent):
    return sent.split(' ')

def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None

def match(sentence):#get full sentence & work on it
    scan_sent = split_sent(sentence)
    result = []
    stoper_l = []
    for local in scan_sent:

        if convert_numbers(local):
            tup = ('number',int (local))
        elif local in object:
            tup = ('object',local)
        elif local in verb:
            tup = ('verb', local)
        elif local in stop:
            stoper = ('stop', local)
        elif local in subject:
            tup = ('subject', local)
        else:
            tup = ()
            stoper = ('error',local)
        
        #stoper_l.append(stoper)
        result.append(tup)
    
    return result

def get_subject(result):
    subject = []
    for local in result:
        if local[0] == 'subject':
            subject.append(local[1])
    return subject

def get_verb(result):
    verb = []
    for local in result:
        if local[0] == 'verb':
            verb.append(local[1])
    return verb

def get_object(result):
    object = []
    for local in result:
        if local[0] == 'object':
            object.append(local[1])
    return object

def get_sent(result):
    sub = get_subject(result)
    obj = get_object(result)
    verb = get_verb(result)
    return Sentence(sub,obj,verb)

#trial_result = match("player go left")
#print(trial_result)

sent = get_sent([('subject', 'player'), ('verb', 'go'), ('object', 'left')])
print(type(sent))
print(f"Object are {sent.obj},Subject are {sent.sub},Verb are {sent.verb}")