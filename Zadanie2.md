# Zadanie 2
def check_number(second_list =  [2,3,7,4,9], number = 10):
  orginal_list = [x + 1 for x in range(number)]
  return list(set(orginal_list)-set(second_list))
