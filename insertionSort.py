def insertionSort(arrey):
    for i in range(1, len(arrey)):
        big = 0
        small = 0
        index = i - 1
        
        while(index >= 0 and arrey[i] <= arrey[index]):
            big = arrey[i]
            small = arrey[index]
            arrey[i] = small
            arrey[index] = big
            index -= 1
            i -= 1
            print
    return arrey

values = [-10, 8400, 1.77, 10, 69, 42, 2.33333]
print(insertionSort(values))