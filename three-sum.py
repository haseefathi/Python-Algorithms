from SearchAlgorithms.binarySearch import Array

def countTriples(array):
    # counts the triples that add to 0
    count = 0
    n = len(array)

    ar = Array(array)

    for i in range(0,n):
        for j in range(i+1, n):
            if(ar.binarySearch(-array[i]-array[j]) > j):
                string = "Triple {num}: {a}, {b}, {c} "
                count += 1
                print(string.format(num=count, a = array[i], b=array[j], c=-array[i]-array[j]))
                
    return count

def main():
    array = []
    n = int(input('\nEnter the number of elements: '))

    print('Enter the elements of the array:')
    for i in range(0,n):
        elt = int(input())
        array.append(elt)
        
    print()
    count = countTriples(sorted(array))
    print('\nThe number of triples that sum to zero is', count)

if __name__ == '__main__':
    main()
