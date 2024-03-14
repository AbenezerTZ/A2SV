# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
english = set(map(int, input().split()))
f = int(input())
france = set(map(int, input().split()))
ans = english.difference(france)
print(len(ans))
