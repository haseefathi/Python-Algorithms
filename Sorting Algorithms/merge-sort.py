class Merge:

    def __init__(self, array):
        self.aux = [None] * len(array)


    def merge(self,array, lo, mid, hi):
        left = lo
        right = mid + 1

        for i in range(lo, hi+1):
            self.aux[i] = array[i]
                
        for k in range(lo, hi+1):
            if left > mid: # left array is completed
                array[k] = self.aux[right]
                right += 1
            elif right > hi: 
                array[k] = self.aux[left]
                left += 1
            elif self.aux[left] < self.aux[right]:
                array[k] = self.aux[left]
                left += 1
            else:
                array[k] = self.aux[right]
                right += 1
    
    def sort(self,array, lo, hi):
        if hi <= lo: return 
        mid = int((lo+hi)/2)
        self.sort(array, lo, mid)
        self.sort(array, mid+1, hi)
        self.merge(array, lo, mid, hi)

    def mergeSort(self, array):
        self.sort(array, 0, len(array)-1)

 
        
def main():
    print('\nEnter the array: ')
    input_array = input().split()
    int_array = []

    for elt in input_array:
        int_array.append(int(elt))

    print('Initial array:',int_array)

    obj = Merge(int_array)
    obj.mergeSort(int_array)

    print('Sorted array:', int_array)
    

if __name__ == "__main__":
    main()
