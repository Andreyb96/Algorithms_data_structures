from io import StringIO

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1
        self.sum = key
        # self.parent = None


class AVL:
    @staticmethod
    def insert(root: Node, key: int) -> Node:
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = AVL.insert(root.left, key)
        else:
            root.right = AVL.insert(root.right, key)
        return AVL.balance(root)

    @staticmethod
    def remove(root: Node, key: int) -> Node:
        if root is None:
            return None
        if key < root.key:
            root.left = AVL.remove(root.left, key)
        elif key > root.key:
            root.right = AVL.remove(root.right, key)
        else:
            l = root.left
            r = root.right
            if l is None:
                return r
            max_node = AVL.findmax(l)
            max_node.left = AVL.removemax(l)
            max_node.right = r
            return AVL.balance(max_node)
        return AVL.balance(root)

    @staticmethod
    def find(root: Node, key: int) -> bool:
        if root is None:
            return False
        if key < root.key:
            return AVL.find(root.left, key)
        elif key > root.key:
            return AVL.find(root.right, key)
        else:
            return True

    @staticmethod
    def merge(v1, v2) -> Node:
        if v1 is None:
            return v2
        elif v2 is None:
            return v1
        T = AVL.findmax(v1)
        v1 = AVL.removemax(v1)
        return AVL.avl_merge_with_root(v1, v2, T)

    @staticmethod
    def split(root: Node, key: int) -> tuple:
        if root is None:
            return (None, None)
        if key < root.key:
            left_split = AVL.split(root.left, key)
            right_tree = AVL.avl_merge_with_root(left_split[1], root.right, root)
            return (left_split[0], right_tree)
        else:
            right_split = AVL.split(root.right, key)
            left_tree = AVL.avl_merge_with_root(root.left, right_split[0], root)
            return (left_tree, right_split[1])

    @staticmethod
    def sum_less_than(root: Node, key: int) -> bool:
        if root is None:
            return 0
        if key < root.key:
            return 0 + AVL.sum_less_than(root.left, key)
        elif key > root.key:
            return (root.left.sum if root.left is not None else 0) + root.key + AVL.sum_less_than(root.right, key)
        else:
            return root.left.sum if root.left is not None else 0

    @staticmethod
    def sum_greater_than(root: Node, key: int) -> bool:
        if root is None:
            return 0
        if key < root.key:
            return (root.right.sum if root.right is not None else 0) + root.key + AVL.sum_greater_than(root.left, key)
        elif key > root.key:
            return 0 + AVL.sum_greater_than(root.right, key)
        else:
            return root.right.sum if root.right is not None else 0

    @staticmethod
    def sum_modified(root: Node, l: int, r: int) -> int:
        if root is None:
            return 0
        return max(root.sum - AVL.sum_less_than(root, l) - AVL.sum_greater_than(root, r), 0)

    @staticmethod
    def sum(root: Node, l: int, r: int) -> tuple:
        split1 = AVL.split(root, max(l-1, 0))
        split2 = AVL.split(split1[1], r)
        lr_sum = AVL.get_sum(split2[0])
        root = AVL.merge(split1[0], AVL.merge(split2[0], split2[1]))
        return lr_sum, root

    @staticmethod
    def merge_with_root(v1: Node, v2: Node, T: Node) -> Node:
        T.left = v1
        T.right = v2
        return T

    @staticmethod
    def avl_merge_with_root(v1: Node, v2: Node, T: Node) -> Node:
        if abs(AVL.get_height(v1) - AVL.get_height(v2)) <= 1:
            merged = AVL.merge_with_root(v1, v2, T)
            AVL.update(merged)
            # return AVL.balance(merged)
            return merged
        elif AVL.get_height(v1) > AVL.get_height(v2):
            right_merged = AVL.avl_merge_with_root(v1.right, v2, T)
            v1.right = right_merged
            # right_merged.parent = v1
            return AVL.balance(v1)
        else:
            left_merged = AVL.avl_merge_with_root(v1, v2.left, T)
            v2.left = left_merged
            # left_merged.parent = v2
            return AVL.balance(v2)

    @staticmethod
    def findmax(root: Node) -> Node:
        return AVL.findmax(root.right) if root.right is not None else root

    @staticmethod
    def removemax(root: Node) -> Node:
        if root.right is None:
            return root.left
        root.right = AVL.removemax(root.right)
        return AVL.balance(root)

    @staticmethod
    def get_height(root: Node) -> int:
        return root.height if root is not None else 0

    @staticmethod
    def get_size(root: Node) -> int:
        return root.size if root is not None else 0

    @staticmethod
    def get_sum(root: Node) -> int:
        return root.sum if root is not None else 0

    # должен быть -1, 0 или 1
    # если -2 или 2, то нужно применять повороты
    @staticmethod
    def get_balance_factor(root: Node) -> int:
        return AVL.get_height(root.right) - AVL.get_height(root.left)

    @staticmethod
    def update(root: Node) -> None:
        root.height = max(AVL.get_height(root.right), AVL.get_height(root.left)) + 1
        root.size = AVL.get_size(root.left) + AVL.get_size(root.right) + 1
        root.sum = AVL.get_sum(root.right) + AVL.get_sum(root.left) + root.key

    @staticmethod
    def rotate_right(root: Node) -> Node:
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        AVL.update(root)
        AVL.update(new_root)
        return new_root

    @staticmethod
    def rotate_left(root: Node) -> Node:
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        AVL.update(root)
        AVL.update(new_root)
        return new_root

    @staticmethod
    def balance(root: Node) -> Node:
        AVL.update(root)
        if AVL.get_balance_factor(root) == 2:
            if AVL.get_balance_factor(root.right) < 0:
                root.right = AVL.rotate_right(root.right)
            return AVL.rotate_left(root)
        if AVL.get_balance_factor(root) == -2:
            if AVL.get_balance_factor(root.left) < 0:
                root.left = AVL.rotate_right(root.left)
            return AVL.rotate_right(root)
        return root

    @staticmethod
    def walk(root: Node):
        if root is None:
            return
        AVL.walk(root.left)
        print(root.key, end=' ')
        AVL.walk(root.right)

def task44():
    def f(x):
        return (x+s) % 1000000001

    n, s, root = int(input()), 0, None
    for _ in range(n):
        line = input().split()
        if line[0] == '+':
            value = f(int(line[1]))
            if not AVL.find(root, value):
                root = AVL.insert(root ,value)
        elif line[0] == '-':
            value = f(int(line[1]))
            if AVL.find(root, value):
                root = AVL.remove(root ,value)
        elif line[0] == '?':
            value = f(int(line[1]))
            print('Found' if AVL.find(root, value) else 'Not found')
        elif line[0] == 's':
            left, right = f(int(line[1])), f(int(line[2]))
            s = AVL.sum_modified(root, left, right)
            print(s)
            
task44()