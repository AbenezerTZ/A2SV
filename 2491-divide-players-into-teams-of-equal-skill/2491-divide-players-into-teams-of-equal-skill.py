class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        skill.sort()
        temp = skill[0] + skill[-1]
        j = len(skill) - 1
        for i in range(len(skill)//2):
            if (skill[i] + skill[j]) == temp:
                ans += (skill[i] * skill[j])
            else:
                return -1
            j -= 1
        return ans
        