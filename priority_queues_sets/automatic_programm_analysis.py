import sys
sys.setrecursionlimit(50000)

class DisjointSet:
    def __init__(self, n):
        self.a = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def union(self, l, r):
        lp = self.find(l)
        rp = self.find(r)
        if self.rank[lp] > self.rank[rp]:
            self.a[rp] = lp
        else:
            self.a[lp] = rp
            self.rank[lp] += 1

    def find(self, i):
        p = i
        while True: 
            if p == self.a[p]:
                break
            p = self.a[p]

        # flatten:
        # if i != self.a[i]:
        #    self.a[i] = self.find(self.a[i])
        return self.a[p]


def readinput():
    n, e, d = [int(i) for i in input().strip().split(' ')]
    ds = DisjointSet(n)
    for k in range(e):
        i, j = [int(i) for i in input().strip().split(' ')]
        i -= 1
        j -= 1
        ds.union(i, j)
    for k in range(d):
        i, j = [int(i) for i in input().strip().split(' ')]
        i -= 1
        j -= 1
        if ds.find(i) == ds.find(j):
            print(0)
            exit()
    print(1)

if __name__ == '__main__':
    readinput()