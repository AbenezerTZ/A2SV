class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        col = [0] * len(mat[0])
        row = [0] * len(mat)

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                row[r] += mat[r][c]
                col[c] += mat[r][c]
        
        ans = 0
        for r in range(len(row)):
            for c in range(len(col)):
                if mat[r][c] == 1 and row[r] + col[c] == 2:
                    print(r, c)
                    ans += 1
        return ans