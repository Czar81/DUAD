def sort_string(unsort_string):
    unsort_list = unsort_string.split('-')
    unsort_list.sort()
    sorted_string = " ".join(unsort_list)#Lista ordanada
    print(sorted_string)

unsort_string = input("Ingrese las palabras separadas con guiones: ")
sort_string(unsort_string)