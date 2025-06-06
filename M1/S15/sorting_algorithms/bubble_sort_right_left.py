def bubble_sort(list, startindex = 0):
    changed = False
    for i in range(len(list) - 1, startindex, -1):
        if list[i] < list[i - 1]:
            list[i], list[i - 1] = list[i - 1], list[i]
            changed = True
    if not changed:
        return list
    return bubble_sort(list, startindex + 1)


def main():
    list = [64,28,3,6,14,10,30]
    print(bubble_sort(list))
    

if __name__ == '__main__':
    main()