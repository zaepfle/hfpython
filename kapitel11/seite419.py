
import time

def zeit_formatieren(zeitstring):
    anz_z = len(zeitstring)
    if anz_z < 3:
        originalformat = '%S'       
    elif anz_z < 6:
        originalformat = '%M:%S'
    else:
        originalformat = '%H:%M:%S'
    zeitstring = time.strftime('%H:%M:%S', time.strptime(zeitstring, originalformat))
    return(zeitstring)

def zeit2seks(zeitstring):
    (stds, mins, seks) = zeitstring.split(':')
    zeitseks = int(seks) + (int(mins)*60) + (int(stds)*60*60)
    return(zeitseks)

def seks2time(zeitseks):
    return(time.strftime('%H:%M:%S', time.gmtime(zeitseks)))
