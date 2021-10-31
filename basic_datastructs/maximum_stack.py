import sys


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
        return self._stack.pop()[0]

    def max(self):
        """Time complexity: O(1)"""
        return self._stack[-1][1]


def main():
    stack = StackWithMax()
    n_ = input()

    for line in sys.stdin.readlines():
        if line.startswith('pop'):
            stack.pop()
        elif line.startswith('max'):
            print(stack.max())
        else:
            command_, value = line.split()
            stack.push(int(value))


if __name__ == '__main__':
    main()