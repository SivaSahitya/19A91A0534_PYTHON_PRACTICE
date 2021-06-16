n = input()
a = set(map(int, input().split()))
n = input()
b = set(map(int, input().split()))
print(len(a.difference(b)))


INPUT:
8
1 2 3 4 5 6 7 8
8
11 4 7 24 5 6 1 9
OUTPUT:
3






