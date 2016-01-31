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

print(sorted(ron))
print(sorted(julie))
print(sorted(mark))
print(sorted(sarah))
