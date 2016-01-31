# coding: utf-8

import datetime
import time

def zeit_formatieren(zeitstring):
    zeitteile = []
    if zeitstring.find(':'):
        zeitteile = [int(teil) for teil in zeitstring.split(':')]
    else:
        zeitteile = [int(zeitstring)]
    while len(zeitteile) < 3:
        zeitteile.insert(0, 0)
    zeitstring = datetime.time(*zeitteile).strftime('%H:%M:%S')
    return(zeitstring)


def zeit2seks(zeitstring):
    zeitstring = zeit_formatieren(zeitstring)
    (stds, mins, seks) = zeitstring.split(':')
    zeitseks = int(seks) + (int(mins)*60) + (int(stds)*60*60)
    return(zeitseks)

def seks2zeit(zeitseks):
    return(time.strftime('%H:%M:%S', time.gmtime(zeitseks)))
