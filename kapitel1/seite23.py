for daten in filme:
    if isinstance(daten, list):
        for teildaten in daten:
            print(teildaten)
    else:
        print(daten)