class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        elif arr[0] > arr[1]:
            return False
        i = 0
        flag = True
        
        while i < len(arr)-1 and flag:
            if arr[i] < arr[i+1]:
                i += 1
            elif arr[i] > arr[i+1]:
                flag = False
            else:
                return False
        if i == len(arr)-1:
            return False
        
        while i < len(arr)-1:
            if arr[i] > arr[i+1]:
                i += 1
            else:
                return False
        return True
                