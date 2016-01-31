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

print(sorted(set([säubern(t) for t in ron]))[0:3])
print(sorted(set([säubern(t) for t in julie]))[0:3])
print(sorted(set([säubern(t) for t in mark]))[0:3])
print(sorted(set([säubern(t) for t in sarah]))[0:3])
