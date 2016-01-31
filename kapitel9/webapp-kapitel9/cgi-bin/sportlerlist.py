# coding: utf-8

class SportlerList(list):
    def __init__(self, ein_name, ein_geb=None, ein_zeiten=[]):
        self.name = ein_name
        self.geb = ein_geb
        self.extend(ein_zeiten)

    @property  
    def top3(self):
        return(sorted(set([saeubern(t) for t in self]))[0:3])
    @property
    def saubere_daten(self):
        return(sorted(set([saeubern(t) for t in self])))
    @property
    def als_dict(self):
        return({'Name':  self.name,
                'Geb':   self.geb,
                'Top3':  self.top3})
    
def saeubern(zeit_string):
    if '-' in zeit_string:
        trenner = '-'
    elif ':' in zeit_string:
        trenner = ':'
    else:
        return(zeit_string)
    (mins, seks) = zeit_string.split(trenner)
    return(mins + '.' + seks)
