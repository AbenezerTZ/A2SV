class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        y=x=0
        res = {}
        for i in range(len(path)): # 0 1 2 
            temp = []
            if path[i]=="N":
                y += 1
                temp.append(x)
                temp.append(y)
            elif path[i]=="S":
                y -= 1
                temp.append(x)
                temp.append(y)
            elif path[i]=="E":
                x += 1
                temp.append(x)
                temp.append(y)
            elif path[i]=="W":
                x -= 1
                temp.append(x)
                temp.append(y)
            if tuple(temp) in res:
                res[tuple(temp)]+=1
            else:
                res[tuple(temp)]=1
        for key,value in res.items():
            if value>=2 or key==(0,0):
                return True
        return False   
        