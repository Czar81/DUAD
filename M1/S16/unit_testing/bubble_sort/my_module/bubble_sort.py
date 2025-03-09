def bubble_sort_list(this_list, outindex=0):
    changed = False
    if not isinstance(this_list, list):
        raise TypeError
    
    if not this_list:
        return []
    
    for i in range(len(this_list) - 1 - outindex):
        if this_list[i] > this_list[i + 1]:
            this_list[i], this_list[i + 1] = this_list[i + 1], this_list[i]
            changed = True
    if not changed:
        return this_list
    return bubble_sort_list(this_list, outindex + 1)


def main():
    try:
        #list = [64,28,3,6,14,10,30]
        list ="dsdsd"
        print(bubble_sort_list(list))
    except TypeError:
        print("The argument must be a list: ")
    

if __name__ == '__main__':
    main()