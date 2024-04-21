from random import randint
def get_numbers_ticket(mn, mx, quantity):
    arr_uniq = set()
    empty_lst = []
    if  mx - mn < (quantity - 1) :
        return empty_lst
    while len(arr_uniq) != quantity:
        arr_uniq.add(randint(mn,mx))
    return sorted(list(arr_uniq))
print(get_numbers_ticket(2,6,5))