#! /usr/local/bin/python3

import json
import sportlermodul
import yate

namen = sportlermodul.namen_einlesen()

print(yate.antwort_anfang('application/json'))
print(json.dumps(sorted(namen)))
