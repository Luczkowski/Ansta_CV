# Zadanie 2
def check_number(second_list = [2,3,7,4,9], number = 10):
    return list(set([x + 1 for x in range(number)])-set(second_list))
