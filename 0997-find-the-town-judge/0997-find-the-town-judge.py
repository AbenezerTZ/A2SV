class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        freq ={}
        check = []
        for i in range(len(trust)):
            if trust[i][0] not in freq:
                freq[trust[i][0]] = [trust[i][1]]
            else:
                freq[trust[i][0]].append(trust[i][1])
            check.append(trust[i][0])
        check = set(check)
        temp = [i for i in range(1,n+1)]
        temp = set(temp)
        judge = temp.difference(check)
        judge = list(judge)
        if len(judge) != 1:
            return -1
        
        for i in range(1,n+1):
            if i != judge[0] and judge[0] not in freq[i]:
                return -1
        return judge[0]