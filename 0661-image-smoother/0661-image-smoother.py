class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        if len(img)==1 and len(img[0])==1:
            return img
        elif len(img[0])==1 and len(img)>1:
            for i in range (len(img)):
                temp = []
                if i == 0 :
                    temp.append((img[0][0] + img[1][0])//2)
                    res.append(temp)
                elif i==len(img)-1:
                    temp.append((img[i][0] + img[i-1][0])//2)
                    res.append(temp)
                else:
                    temp.append((img[i][0] + img[i-1][0] + img[i+1][0])//3)
                    res.append(temp)
            return res
        
        elif len(img)==1 and len(img[0])>1:
            temp = []
            for i in range (len(img[0])):
                
                if i == 0 :
                    temp.append((img[0][0] + img[0][1])//2)
                elif i==len(img[0])-1:
                    temp.append((img[0][i] + img[0][i-1])//2)
                else:
                    temp.append((img[0][i] + img[0][i-1] + img[0][i+1])//3)
            res.append(temp)

            return res
            
        for i in range(len(img)):  # 1 2 3
            tempo = []
            for j in range(len(img[0])): # 1 2 3
                if i!=0 and j!=0 and i!=len(img)-1 and j!=len(img[0])-1:
                    ans = (img[i-1][j-1] + img[i-1][j] + img[i-1][j+1] + img[i][j-1] + img[i][j] + img[i][j+1] + img[i+1][j-1] + img[i+1][j] + img[i+1][j+1])//9
                    tempo.append(ans)
                elif i==0 and j==0:
                    ans = (img[i][j] + img[i][j+1] + img[i+1][j] + img[i+1][j+1])//4
                    
                    tempo.append(ans)
                elif i==0 and j==len(img[0])-1:
                    ans = (img[i][j] + img[i][j-1] + img[i+1][j] + img[i+1][j-1])//4
                    tempo.append(ans)
                elif i!=0 and j==0 and i!=len(img)-1:
                    ans = (img[i-1][j] + img[i-1][j+1] + img[i][j] + img[i][j+1] + img[i+1][j] + img[i+1][j+1])//6
                    tempo.append(ans)
                elif i==len(img[0])-1 and j==0:
                    ans = (img[i][j] + img[i][j+1] + img[i-1][j] + img[i-1][j+1])//4
                    tempo.append(ans)
                elif i==len(img)-1 and j==len(img[0])-1:
                    ans = (img[i-1][j-1] + img[i-1][j] + img[i][j-1] + img[i][j])//4
                    tempo.append(ans)
                elif i==len(img)-1 and j==0:
                    ans = (img[i-1][j+1] + img[i-1][j] + img[i][j+1] + img[i][j])//4
                    tempo.append(ans)
                
                elif i!=0 and j==len(img[0])-1 and i!=len(img)-1 :
                    ans = (img[i-1][j-1] + img[i-1][j] + img[i][j-1] + img[i][j] + img[i+1][j-1] + img[i+1][j])//6
                    tempo.append(ans)
                elif i==0 and j!=0 and j!=len(img[0])-1 :
                    ans = (img[i][j-1] + img[i][j] + img[i][j+1] + img[i+1][j-1] + img[i+1][j] + img[i+1][j+1])//6
                    tempo.append(ans)
                elif i==len(img)-1 and j!=0 and j!=len(img[0])-1 :
                    ans = (img[i-1][j-1] + img[i-1][j] + img[i-1][j+1] + img[i][j-1] + img[i][j] + img[i][j+1])//6
                    tempo.append(ans)

            res.append(tempo)

        return(res)
