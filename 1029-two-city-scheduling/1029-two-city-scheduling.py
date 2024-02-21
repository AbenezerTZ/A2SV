class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        comp = {}
        ans = 0
        k = []
        const = 0.1
        for i in range(len(costs)):
            x = abs(costs[i][0]-costs[i][1])
            if x in comp:
                comp[x + const] = costs[i]
                const += 0.1
            else:
                comp[x] = costs[i]
        for key, value in comp.items():
            k.append(key)
        k.sort(reverse=True)
        a = b = len(costs)//2
        for i in range(len(k)):
            if a == 0:
                ans += comp[k[i]][1]
                del comp[k[i]]
            elif b == 0:
                ans += comp[k[i]][0]
                del comp[k[i]]
            else:
                temp = min(comp[k[i]])
                if temp == comp[k[i]][0] and a > 0:
                    ans += temp
                    del comp[k[i]]
                    a -= 1
                elif temp == comp[k[i]][1] and b > 0:
                    ans += temp
                    del comp[k[i]]
                    b -= 1
        return ans