class StackWithMax:
    def __init__(self):
        self._stack = []

    def push(self, n):
        """Time complexity: O(1)"""
        if not self._stack:
            self._stack.append([n, n])
        else:
            self._stack.append([n, max(self._stack[-1][1], n)])

    def pop(self):
        """Time complexity: O(1)"""
        return self._stack.pop()[0] if not self.is_empty() else None

    def max(self):
        """Time complexity: O(1)"""
        return self._stack[-1][1] if not self.is_empty() else -float('inf')

    def is_empty(self):
        """Time complexity: O(1)"""
        return False if self._stack else True


class QueueWithMax:
    def __init__(self):
        self._left_stack = StackWithMax()
        self._right_stack = StackWithMax()

    def push(self, n):
        """Time complexity: O(1)"""
        self._left_stack.push(n)

    def pop(self):
        """Average time complexity: O(1)
        Worst time complexity: O(n), where n = len(self._left_stack._stack)
        """
        if self._right_stack.is_empty():
            while not self._left_stack.is_empty():
                self._right_stack.push(self._left_stack.pop())
        return self._right_stack.pop()

    def max(self):
        """Time complexity: O(1)"""
        return max(self._left_stack.max(), self._right_stack.max())


def sliding_window_maximums(n, m, array):
    """Time complexity: O(n), where n = len(array)"""
    queue = QueueWithMax()
    for i in range(m):
        queue.push(array[i])
    maximums = [queue.max()]

    for i in range(m, n):
        queue.push(array[i])
        _ = queue.pop()
        maximums.append(queue.max())

    return maximums


def main():
    n = int(input())
    array = [int(i) for i in input().split()]
    m = int(input())

    print(*sliding_window_maximums(n, m, array))


if __name__ == '__main__':
    main()