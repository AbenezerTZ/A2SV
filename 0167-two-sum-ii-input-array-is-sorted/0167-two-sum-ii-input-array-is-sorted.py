class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        start = 0
        end = l-1
        result = [  ]
        while start < end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end-=1 
            elif sum < target:
                start+=1
            else:
                return [start+1, end+1]