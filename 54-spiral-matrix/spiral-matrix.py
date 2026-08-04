class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        c=list(range(len(matrix[0])))
        r=list(range(len(matrix)))
        l=[]

        while r and c:
            #right
            for i in range(len(c)):
                l.append(matrix[r[0]][c[i]])
            r=r[1:]
            if not r or not c:
                break
            #down
            for i in range(len(r)):
                l.append(matrix[r[i]][c[-1]])
            c=c[:-1]
            if not r or not c:
                break
            #left
            for i in range(len(c)-1,-1,-1):
                l.append(matrix[r[-1]][c[i]])
            r=r[:-1]
            if not r or not c:
                break
            #up
            for i in range(len(r)-1,-1,-1):
                l.append(matrix[r[i]][c[0]])
            c=c[1:]
            if not r or not c:
                break
        return l
