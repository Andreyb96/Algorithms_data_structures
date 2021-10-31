from io import StringIO

def task45():
    string = input()
    n = int(input())
    for _ in range(n):
        i, j, k = map(int, input().split())
        substring = string[i:j+1]
        string = string[:i] + string[j+1:]
        string = string[:k] + substring + string[k:]
    print(string)

task45()