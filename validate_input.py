def gcom(prm):
    while True:
        try:
            complexnum = complex(input(prm + " "))
        except ValueError:
            pass
        else:
            return complexnum
            break

def gflt(prm):
    while True:
        try:
            flt = float(input(prm + " "))
        except ValueError:
            pass
        else:
            return flt
            break

def gint(prm):
    while True:
        try:
            integer = int(input(prm + " "))
        except ValueError:
            pass
        else:
            return integer
            break
