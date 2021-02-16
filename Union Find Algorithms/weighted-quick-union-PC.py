class UnionFind:  # weighted quick-union with path compression implementation
    count = 0
    ids = list()
    size = list()

    def __init__(self,N):
        self.count = N
        for i in range(0,N):
            self.ids.append(i)
            self.size.append(1)

    def getIdArray(self):
        return self.ids

    def getSizeArray(self):
        return self.size

    def connected(self,p,q):
        return self.find(p) == self.find(q)

    def getCount(self):
        return self.count

    def find(self, p):  
        # keep going higher in the tree till you reach root node
        while(p!=self.ids[p]): 
            self.ids[p] = self.ids[self.ids[p]] # path compression line
            p = self.ids[p]

        # returns the root node
        return p


    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)

        # already joined to each other...so do nothing
        if pRoot == qRoot:
            return 

        # not connected...so change the values in the ids array
        # change the values of the p component to that of the q component
        if self.size[pRoot] < self.size[qRoot]:
            self.ids[pRoot] = qRoot
            self.size[qRoot] += self.size[pRoot]
        else:
            self.ids[qRoot] = pRoot
            self.size[pRoot] += self.size[qRoot]


        self.count -= 1


def main():
    
    try:
        N = int(input("\nEnter the number of components: "))
    except:
        print('Number of components must be an integer! Try again...')
        N = int(input("\nEnter the number of components: "))


    uf = UnionFind(N)
    
    while True:
        print('\n-------------OPERATIONS-------------\n1.Union\n2.Check Connection\n3.Display ID Array\n4.Display Size Array\n5.Get number of connected components\n6.Quit')

        try:
            choice = int(input('\nEnter choice (1/2/3/4/5/6): '))
        except:
            print('Invalid choice entered! Try again')
            choice = int(input('\nEnter choice (1/2/3/4/5/6): '))

        if choice == 1:
            print('\n---------------UNION---------------')
            sites = input('\nEnter p, q: ')
            siteList = sites.split(' ')
            p = int(siteList[0])
            q = int(siteList[1])
            try:
                uf.union(p,q)
                print('Sites joined!')
            except:
                print('Invalid sites entered!')


        elif choice == 2:
            print('\n-----------CONNECTED-----------')
            sites = input('\nEnter p, q to check connection: ')
            siteList = sites.split(' ')
            p = int(siteList[0])
            q = int(siteList[1])
            try:
                if uf.connected(p,q):
                    print('\nThey are connected')
                else:
                    print('\nThey are not connected')
            except:
                print('Invalid sites entered!')

        elif choice == 3:
            print('Current ID Array: ', uf.getIdArray())
            
        elif choice == 4:
            print('Current Size Array: ', uf.getSizeArray())

        elif choice == 5:
            count = uf.getCount()
            print('Number of connected components: ',count)
            
        elif choice == 6:
            print('\n\nAdios!')
            break

        else:
            print('Invalid choice!')


if __name__ == "__main__":
    main()