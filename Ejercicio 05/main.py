def es_bisiesto(fecha):
    if (fecha % 4 == 0):
        if (fecha % 100 != 0) and (fecha % 400 != 0):
            return True
        elif (fecha % 100 == 0) and (fecha % 400 == 0):
            return True
        else:
            return False
    else:
        return False