# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())
flag = True
for _ in range(n):
    test = set(map(int, input().split()))
    temp = test.difference(A)
    if len(temp) != 0:
        flag = False
print(flag)
