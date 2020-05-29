# Zadanie 3

def decimal_list():

    x = 2.0
    my_list = []

    while x <= 5.5:
        my_list.append(Decimal(x))
        x += 0.5

    return my_list
