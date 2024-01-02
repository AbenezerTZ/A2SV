t = int(input())
for _ in range(t):
    n = list(map(int, input().split()))
    tests = list(map(int, input().split()))
    freq = {}
    count = 0
    for i in tests:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for key, value in freq.items():
        if value > n[1]:
            count += n[1]
        else:
            count += value
    print(count)
