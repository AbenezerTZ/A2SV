class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        str1 = ""
        running_sum = 0 
        dict1 = defaultdict(int)

        for i,j,k in shifts:
            if k == 0:
                dict1[i] -= 1 
                dict1[j+1] += 1 
            else: 
                dict1[i] += 1 
                dict1[j+1] -= 1 

        for i in range(n):
            running_sum += dict1[i]
            val = (ord(s[i])-97+running_sum)%26
            str1 += chr(97+val)

        return str1
        