if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    arr.sort(reverse=True)
    if len(arr) > 1:
        print(arr[1])
