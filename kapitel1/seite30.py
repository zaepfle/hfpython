
filme = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, 
                ["Graham Chapman", ["Michael Palin", "John Cleese",
                        "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


def print_lvl(a_list):
    for daten in a_list:
        if isinstance(daten, list):
            print_lvl(daten)
        else:
            print(daten)
            

print_lvl(filme)
