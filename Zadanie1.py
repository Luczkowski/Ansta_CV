# Zadanie 1
def get_postcodes(start = "79-990", end = "80-155"):

    codes_list = []

    for code in range(int(start.replace("-", "")), int(end.replace("-", "")) + 1):
        code = str(code)
        postcode = code[0:2] + "-" + code[2:5]
        codes_list.append(postcode)

    return codes_list
