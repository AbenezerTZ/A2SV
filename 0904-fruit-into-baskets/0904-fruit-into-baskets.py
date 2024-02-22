class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        j = 0
        freq = {}
        maxi = 1
        while j < len(fruits):
            if fruits[j] in freq:
                freq[fruits[j]] += 1
            else:
                freq[fruits[j]] = 1
             
            while len(freq) > 2:
                maxi = max(maxi, j - i)
                freq[fruits[i]] -= 1
                if freq[fruits[i]] == 0:
                    del freq[fruits[i]]
                i += 1
            j += 1      
        maxi = max(maxi, j - i)
            
        return maxi
            
            
        