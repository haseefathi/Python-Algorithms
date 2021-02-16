class UnionFind:
    count = 0
    ids = list()

    def __init__(self,N):
        self.count = N
        for i in range(0,N):
            self.ids.append(i)

    def getIdArray(self):
        return self.ids

    def connected(self,p,q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.count

    def find(self, p):
        return self.ids[p]

    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)
        if pid == qid:
            return 
        for i in range(0, len(self.ids)):
            if self.ids[i] == pid:
                self.ids[i] = qid
        self.count -= 1



def main():
    
    try:
        N = int(input("\nEnter the number of components: "))
    except:
        print('Number of components must be an integer! Try again...')
        N = int(input("\nEnter the number of components: "))


    uf = UnionFind(N)
    
    while True:
        print('\n-------------OPERATIONS-------------\n1.Union\n2.Check Connection\n3.Display ID Array\n4.Gte number of connected components\n5.Quit')

        try:
            choice = int(input('\nEnter choice (1/2/3/4/5): '))
        except:
            print('Invalid choice entered! Try again')
            choice = int(input('\nEnter choice (1/2/3/4/5): '))

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
            print('Number of connected components:',uf.count())
            
        elif choice == 5:
            print('\n\nAdios!')
            break

        else:
            print('Invalid choice!')


if __name__ == "__main__":
    main()