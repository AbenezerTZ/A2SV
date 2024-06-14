class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_list = path.split('/')
        ans = []
        for part in dir_list:
            if part == '..':
                if ans:
                    ans.pop()
            elif part == '.' or part == '':
                continue
            else:
                ans.append(part)
        ans = '/' + '/'.join(ans)
        return ans if ans else '/'