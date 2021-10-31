class MinHeap:
    def __init__(self, elements=None):
        self._size = len(elements) or 0
        self._elements = elements or []
        self._log = []

        length = self._size // 2
        for index in range(length, -1, -1):
            self._sift_down(index)

    @staticmethod
    def _parent(index):
        return (index - 1) // 2

    @staticmethod
    def _left_child(index):
        return 2 * index + 1

    @staticmethod
    def _right_child(index):
        return 2 * index + 2

    def _swap(self, index1, index2):
        self._elements[index1], self._elements[index2] = self._elements[index2], self._elements[index1]

    def _sift_up(self, index):
        if index < 0:
            return

        parent_index = self._parent(index)
        parent = self._elements[parent_index]
        current = self._elements[index]

        while (
            index > 0 and
            parent > current
        ):
            self._elements[parent_index] = current
            self._elements[index] = parent

            index = parent_index
            parent_index = self._parent(index)
            parent = self._elements[parent_index]
            current = self._elements[index]

    def _sift_down(self, index):
        if index < 0:
            return

        while True:
            min_index = index

            left = self._left_child(index)
            if (
                left < self._size and
                self._elements[left] < self._elements[min_index]
            ):
                min_index = left

            right = self._right_child(index)
            if (
                right < self._size and
                self._elements[right] < self._elements[min_index]
            ):
                min_index = right

            if index == min_index:
                break

            self._log.append((index, min_index))
            self._swap(index, min_index)
            index = min_index

    def extract_min(self):
        if self._size == 0:
            return

        result = self._elements[0]

        if self._size > 1:
            self._elements[0] = self._elements.pop()
            self._size -= 1
            self._sift_down(0)

        return result

    def remove(self, index):
        self._elements[index] = float('-inf')
        self._sift_up(index)
        self.extract_min()

    def insert(self, element):
        self._elements.append(element)
        self._sift_up(self._size)
        self._size += 1

    def print_log(self):
        print(len(self._log))

        for item in self._log:
            print(*item)


def main():

    n = int(input())
    A = [int(i) for i in input().split()]

    heap = MinHeap(A)
    heap.print_log()


if __name__ == "__main__":
    main()