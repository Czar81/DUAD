def bubble_sort(list, outindex=0):
    changed = False #0(1)
    for i in range(len(list) - 1 - outindex): #0(n)
        if list[i] > list[i + 1]: #0(1)
            list[i], list[i + 1] = list[i + 1], list[i] #0(1)
            changed = True #0(1)
    if not changed: #0(1) 
        return list #0(1) 
    return bubble_sort(list, outindex + 1) #0(n)


def main():
    list = [64,28,3,6,14,10,30] #0(1)
    print(bubble_sort(list)) #0(n2)
    

if __name__ == '__main__':
    main() #0(n2)