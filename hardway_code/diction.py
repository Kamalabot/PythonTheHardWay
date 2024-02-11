import mod
print(mod.tangerine) 
#This import will not only print the below 2 lines, it will do more...
print(f"This stuff comes from mod import {mod.mystuff['apple']}")

mod.apple()
#create a mapping of state to abbreviations

#In the case of the dictionary, the key is a string and the syntax is [key]. In the case of the module, the
#key is an identifier, and the syntax is .key. Other than that they are nearly the same thing.

states = {
    'Tamil Nadu' :'TN',
    'Andra Pradesh': 'AP',
    'Karnataka': 'KA',
    'Sikkim':'SK'
    }

#Create mapping for cities 

cities = {
    'DL':'Delhi',
    'Doon':'Dehradun',
    'NTL':'Nanital',
    'CMB':'Coimbatore'
}

cities['Gurgoan'] = 'GGN'
cities['Chennai'] = 'CHN'

print('-'*10)

print(f"Doon city has {cities['Doon']}")
print(f"NTL city has {cities['NTL']}")

print('*'*10)

print("Andra Pradesh has abbreviation of",states['Andra Pradesh'])
print("Gurgoan has abbreviation of",states['Sikkim'])

#print all state abbreviations
for state, abbrev in list(states.items()):
    print(f"{abbrev} of {state}")

for city, abbre in list(cities.items()):
    print(f"Abbreviation of {city} is {abbre}")

state = states.get('Texas')

if not state:
    print("Sorry, no Texas")

city = cities.get("TX","Does not exist")
print(f"The city for the state 'TX' is : {city}")