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

ron = sorted([säubern(t) for t in ron])
julie = sorted([säubern(t) for t in julie])
mark = sorted([säubern(t) for t in mark])
sarah = sorted([säubern(t) for t in sarah])

ron_eindeutig = []
for zeit in ron:
    if zeit not in ron_eindeutig:
        ron_eindeutig.append(zeit)
print(ron_eindeutig[0:3])

julie_eindeutig = []
for zeit in julie:
    if zeit not in julie_eindeutig:
        julie_eindeutig.append(zeit)
print(julie_eindeutig[0:3])

mark_eindeutig = []
for zeit in mark:
    if zeit not in mark_eindeutig:
        mark_eindeutig.append(zeit)
print(mark_eindeutig[0:3])

sarah_eindeutig = []
for zeit in sarah:
    if zeit not in sarah_eindeutig:
        sarah_eindeutig.append(zeit)
print(sarah_eindeutig[0:3])
