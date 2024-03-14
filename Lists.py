if __name__ == '__main__':
    N = int(input())
    ans = []
    for _ in range(N):
        t = list(map(str, input().split()))
        if t[0] == "insert":
            ans.insert(int(t[1]), int(t[2]))
        elif t[0] == "print":
            print(ans)
        elif t[0] == "remove":
            ans.remove(int(t[1]))
        elif t[0] == "append":
            ans.append(int(t[1]))
        elif t[0] == "sort":
            ans.sort()
        elif t[0] == "pop":
            ans.pop()
        elif t[0] == "reverse":
            ans.reverse()
