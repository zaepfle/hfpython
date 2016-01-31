
import time

def zeit2seks(zeitstring):
    (stds, mins, seks) = zeitstring.split(':')
    zeitseks = int(seks) + (int(mins)*60) + (int(stds)*60*60)
    return(zeitseks)

def seks2time(zeitseks):
    return(time.strftime('%H:%M:%S', time.gmtime(zeitseks)))
