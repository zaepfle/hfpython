def säubern(zeit_string):
    if '-' in zeit_string:
        trenner = '-'
    elif ':' in zeit_string:
        trenner = ':'
    else:
        return(zeit_string)
    (mins, seks) = zeit_string.split(trenner)
    return(mins + '.' + seks)

with open('ron.txt') as rod:
    daten = rod.readline()
ron = daten.strip().split(',')
with open('julie.txt') as jud:
    daten = jud.readline()
julie = daten.strip().split(',')
with open('mark.txt') as mad:
    daten = mad.readline()
mark = daten.strip().split(',')
with open('sarah.txt') as sad:
    daten = sad.readline()
sarah = daten.strip().split(',')

ron_sauber = []
julie_sauber = []
mark_sauber = []
sarah_sauber = []

for zeit in ron:
    ron_sauber.append(säubern(zeit))
    
for zeit in julie:
    julie_sauber.append(säubern(zeit))
    
for zeit in mark:
    mark_sauber.append(säubern(zeit))
    
for zeit in sarah:
    sarah_sauber.append(säubern(zeit))

print(sorted(ron_sauber))
print(sorted(julie_sauber))
print(sorted(mark_sauber))
print(sorted(sarah_sauber))
