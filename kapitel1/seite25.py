for daten in filme:
	if isinstance(daten, list):
	    for teildaten in daten:
	        if isinstance(teildaten, list):
	            for teilteildaten in teildaten:
		            print(teilteildaten)
            else:
                print(teildaten)
	else:
	    print(daten)
