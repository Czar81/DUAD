def sum_list(number_list):
    if not isinstance(number_list, list):
        raise TypeError
    sum_total = 0
    for i in number_list:
        sum_total += i
    return sum_total