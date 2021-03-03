class Shell:
    
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
        h = 1
        while(h < N/3):
            h = int(3*h + 1)
        while(h>=1):
            for i in range(h, N):
                for j in range(i, 0, -1):
                    if(self.less(j, j-h)):
                        self.exchange(j,j-h)
            h = int(h/3)

    def showArray(self):
        return self.array


def main():
    a = []
    n = int(input('\nEnter the number of elements in the array:'))

    print('Enter the elements of the array:')
    for i in range(0,n):
        element = int(input())
        a.append(element)

    array = Shell(a)
    print('Initial array:',array.showArray())
    array.sort()
    print('Array after Shell sort:',array.showArray())

if __name__ == "__main__":
    main()
