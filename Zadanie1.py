# Zadanie 1
def get_postcodes(start = "79-990", end = "80-155"):
    return [str(code)[0:2] + "-" + str(code)[2:5]for code in range(int(start.replace("-", "")), int(end.replace("-", "")) + 1)]
