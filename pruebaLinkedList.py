from linked_list import SinglyLinkedList
from my_array import Array

def main():
    
    array = Array(3)
    array.__setRandom__()
    print(array)
    datos = SinglyLinkedList()

    for item in array:
        datos.append(item)
    
    print(datos.data)

    current = datos.tail
    print(current)
    while current:
        print(current.data)
        current = current.next


if __name__ == '__main__':
    main()