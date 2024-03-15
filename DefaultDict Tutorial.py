# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
freq = {}
for i in range(n):
    A = input()
    if A in freq:
        freq[A].append(i+1)
    else:
        freq[A] = [i+1]

for j in range(m):
    B = input()
    if B in freq:
        print(' '.join(map(str, freq[B])))
    else:
        print(-1)
