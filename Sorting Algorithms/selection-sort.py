class Selection:
    
    array = list()

    def __init__(self,a):
        self.array = a
    
    def compare(self,a,b):
        if self.array[a] < self.array[b]: return -1
        elif self.array[a] > self.array[b]: return 1
        else: return 0

    def less(self, a,b):
        return self.compare(a,b) == -1
    
    def exchange(self, idx1, idx2):
        self.array[idx1], self.array[idx2] = self.array[idx2], self.array[idx1]

    def sort(self):
        N = len(self.array)
        for i in range(0,N):
            smallestIdx = i
            for j in range(i+1, N): 
                if self.less(j, smallestIdx): smallestIdx = j
            self.exchange(i,smallestIdx)

    def showArray(self):
        return self.array


def main():
    a = []
    n = int(input('\nEnter the number of elements in the array:'))

    print('Enter the elements of the array:')
    for i in range(0,n):
        element = int(input())
        a.append(element)

    array = Selection(a)
    print('Initial array:',array.showArray())
    array.sort()
    print('Array after Selection sort:',array.showArray())

if __name__ == "__main__":
    main()
