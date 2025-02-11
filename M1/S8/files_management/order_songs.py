def read_file(path):
    unorder_list = []
    with open(path, 'r') as file:
        for text in file:
            print(text.strip())
            unorder_list.append(text.strip())    
    return unorder_list


def order_file(unorder_list):   
    unorder_list.sort()
    return unorder_list
    

def write_file(path,order_list):
    order_list.sort()
    order_text = "\n".join(order_list)
    with open(path,'w', encoding='utf-8') as file:
        file.write(order_text)


def main():
    unorder_list = read_file('songs.txt')
    order_list = order_file(unorder_list)
    write_file('order_songs.txt', order_list)


if __name__ == '__main__':
    main()