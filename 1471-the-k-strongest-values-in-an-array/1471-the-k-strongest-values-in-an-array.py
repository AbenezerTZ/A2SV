class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        num = []
        m = arr[(len(arr)-1)//2]
        i = 0
        j = len(arr)-1
        while i < j:
            if abs(arr[i] - m) > abs(arr[j] - m):
                num.append(arr[i])
                i += 1
            elif abs(arr[i] - m) < abs(arr[j] - m):
                num.append(arr[j])
                j -= 1
            else:
                if arr[i] > arr[j]:
                    num.append(arr[i])
                    i += 1
                else:
                    num.append(arr[j])
                    j -= 1
        num.append(arr[i])
        return (num[:k])
        