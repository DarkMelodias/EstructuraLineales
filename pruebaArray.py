from my_array import Array

def main():
    
    capacity = int(input("Digite la capacidad del array: "))
    array = Array(capacity)
    print(array)
    
    array.__setRandom__()
    print(array)

    sum = array.__getSum__()
    print(sum)


if __name__ == '__main__':
    main()