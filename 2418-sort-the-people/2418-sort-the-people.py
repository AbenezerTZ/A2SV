class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair = {}
        for i in range(len(names)):
            pair[heights[i]] = names[i]
        for i in range(len(heights)):
            for j in range(1,len(heights)):
                if heights[j-1] < heights[j]:
                    heights[j],heights[j-1] = heights[j-1],heights[j]
                    
        for n in range(len(heights)):
            heights[n] = pair[heights[n]]
        return heights
            
        