import sys

class Database:
    def __init__(self, tables, _max):
        self.tables = tables
        self.parents = list(range(len(tables)))
        self._max = _max

    def union(self, destination, source):
        if destination == source:
            return
        psource = self._find(source)
        pdestination = self._find(destination)
        if psource == pdestination:
            return
        self._move(pdestination, psource)
        if self._max < self.tables[pdestination]:
            self._max = self.tables[pdestination]

    def _move(self, destination, source):
        self.tables[destination] += self.tables[source]
        self.tables[source] = 0
        self.parents[source] = destination

    def _find(self, i):
        #while i != self.parents[i]:
        #    i = self.parents[i]
        if i != self.parents[i]:
            self._move(self.parents[i], i)
            self.parents[i] = self._find(self.parents[i])
        return self.parents[i]

    def max(self):
        return self._max

    def __repr__(self):
        return ' tables=' + str(self.tables) + ' parents=' + str(self.parents)

def readinput():
    n, m = [int(i) for i in input().strip().split(' ')]
    tables = []
    max_ = 0
    for raw in input().strip().split(' '):
        i = int(raw)
        if max_ < i:
            max_ = i
        tables += [i]
    assert(len(tables) == n)
    db = Database(tables, max_)
    # print(db)

    for i in range(m):
        dest, source = [int(i) for i in input().strip().split(' ')]
        db.union(dest - 1, source - 1)
        print(db.max())
        # print(db)

if __name__ == '__main__':
    readinput()