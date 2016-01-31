#! /usr/local/bin/python3

import json
import sportlermodell
import yate

namen = sportlermodell.namen_ids_lesen()

print(yate.antwort_anfang('application/json'))
print(json.dumps(sorted(namen)))
