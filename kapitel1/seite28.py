for daten in filme:
    if isinstance(daten, list):
        for teildaten in daten:
            if isinstance(teildaten, list):
                for teilteildaten in teildaten:
                    if isinstance(teilteildaten, list):
						for teilteilteildaten in teilteildaten:
						    print(teilteilteildaten)
					else:
						print(teilteildaten)
			else:
				print(teildaten)
	else:
	    print(daten)