noun = ['bear', 'princess', 'eyes', 'sword', 'gun', 
        'you','princess','turret','enemy','alien',
        'keypad','room']
verb = ['go', 'kill', 'eat', 'come', 'fight', 'lift', 
        'shoot','walk','crouch','duck','aim','fire',
        'punch','stamp','enter','take','open']
stop = ['the', 'in', 'it', 'of', 'a', 'an','from','to']
direction = ['north', 'south', 'east', 'west','right',
            'up','down','center','top','bottom']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(sentence): 
    result = []
    temp_sent = sentence.split(' ')

    for part in temp_sent:
        if convert_numbers(part):
            tup = ('number',int(part))
        elif part in noun:
            tup = ('noun',part)
        elif part in verb:
            tup = ('verb',part)
        elif part in stop:
            tup = ('stop',part)
        elif part in direction:
            tup = ('direction',part)
        else:
            tup = ('error',part)
        result.append(tup)

    return result 

result = scan('ASFADFADS')

print(result)