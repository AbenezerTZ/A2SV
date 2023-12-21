class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        visit = []
        sub_domain = []
        res = {}
        ans = []
        for i in range(len(cpdomains)):
            temp = []
            for j in range(len(cpdomains[i])-1):
                if cpdomains[i][j+1] == " ":
                    temp.append(int(cpdomains[i][0:j+1]))
                    temp.append(cpdomains[i][j+2:])
                    visit.append(temp)
                    break
        for i in range(len(visit)):  
            temp = []
            temp.append(visit[i][1])
            for j in range(len(visit[i][1])):
                if visit[i][1][j] == ".":
                    temp.append(visit[i][1][j+1:])
            sub_domain.append(temp)
        for i in range(len(sub_domain)):  
            for j in range(len(sub_domain[i])):
                if sub_domain[i][j] in res :
                    res[sub_domain[i][j]] += visit[i][0]
                else:
                    res[sub_domain[i][j]] = visit[i][0]
        for a,b in res.items():
            temp = str(b) + " " + a
            ans.append(temp)
        return ans
