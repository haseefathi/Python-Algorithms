class Array:
    array = list()

    def __init__(self, a):
        self.array = a

    def binarySearch(self, key):
        lo = 0
        hi = len(self.array) - 1
        i = 0
        while lo <= hi:
            mid = int((lo+hi)/2)
            if key < self.array[mid]:
                hi = mid - 1
            elif key > self.array[mid]:
                lo = mid + 1
            else: 
                return mid
        return -1
    
    def getArray(self):
        return self.array

def main():
    array = []
    n = int(input('\nEnter the number of elements: '))

    print('Enter the elements in ascending order:')
    for i in range(0,n):
        elt = int(input())
        array.append(elt)

    ar = Array(array)

    key = int(input('Enter the key: '))
    pos = ar.binarySearch(key)
    print('Your array:', ar.getArray())
    if pos == -1:
        print('The element was not found.')
    else:
        print('The element was found at position', pos + 1)

if __name__ == "__main__":
    main()


