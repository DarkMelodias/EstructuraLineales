from doubly_circular_linked import circleDoubleLinkedList

def main():
    circlue_doble_list = circleDoubleLinkedList()
    print('Prueba para ver si se inicializo correctamente:')
    print(circlue_doble_list)
    print(circlue_doble_list.reverse())
    print()


    print('Prueba para agregar un elemento con la lista vacia:')
    circlue_doble_list.unshift(4)
    print(circlue_doble_list)
    print(circlue_doble_list.reverse())
    print()


    print('Prueba de generación de elementos por range:')
    circlue_doble_list.range(1, 6)
    print(circlue_doble_list)
    print(circlue_doble_list.reverse())
    print()


    print('Prueba de recorrido por pasos:')
    print(circlue_doble_list.str_by_steps(12, 'forward'))
    print(circlue_doble_list.str_by_steps(12, 'backward'))
    print()

    print('Prueba de busqueda:')
    circlue_doble_list.search(2)
    print(circlue_doble_list)
    print(circlue_doble_list.reverse())
    print()

    print('Prueba de remplazar un elmento:')
    circlue_doble_list.replace(3, 'replace_item')
    print(circlue_doble_list)
    print(circlue_doble_list.reverse())
    print()

    print('Prueba de insertar un nuevo elmento en head:')
    circlue_doble_list.unshift('unshift')
    print(circlue_doble_list)
    print(circlue_doble_list.reverse())
    print()


    print('Prueba de insertar un nuevo elmento en tail:')
    circlue_doble_list.append('append')
    print(circlue_doble_list)
    print(circlue_doble_list.reverse())
    print()

    print('Prueba de elminar el elemento en head: ')
    circlue_doble_list.shift()
    print(circlue_doble_list)
    print(circlue_doble_list.reverse())
    print()


    print('Prueba de elminar el elemento en tail: ')
    circlue_doble_list.pop()
    print(circlue_doble_list)
    print(circlue_doble_list.reverse())
    print()


    print('Prueba de insertar un elemento por indice: ')
    circlue_doble_list.insert("index", 1)
    print(circlue_doble_list)
    print(circlue_doble_list.reverse())
    print()

    print('Prueba de elminar un elemento por indice: ')
    circlue_doble_list.delete_by_index(3)
    print(circlue_doble_list)
    print(circlue_doble_list.reverse())
    print()


    print('Prueba de limpieza de la lista: ')
    circlue_doble_list.clear()
    print(circlue_doble_list)
    print(circlue_doble_list.reverse())
    print()

if __name__ == '__main__':
    main()