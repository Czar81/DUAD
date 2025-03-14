def sort_string(unsort_string=""):
    #if unsort_list == None:
     #   return None
    unsort_list = unsort_string.split('-')
    unsort_list.sort(key=str.lower)
    sorted_string = " ".join(unsort_list)# Sorted string
    return sorted_string
