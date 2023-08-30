def gcom(prm=""):
    while True:
        try:
            if prm != "":
                complexnum = complex(input())
            else:
                complexnum = complex(input(prm + " "))
        except ValueError:
            pass
        else:
            return complexnum
            break

def gflt(prm=""):
    while True:
        try:
            if prm != "":
                flt = float(input())
            else:
                flt = float(input(prm + " "))
        except ValueError:
            pass
        else:
            return flt
            break

def gint(prm=""):
    while True:
        try:
            if prm != "":
                integer = int(input())
            else:
                integer = int(input(prm + " "))
        except ValueError:
            pass
        else:
            return integer
            break
