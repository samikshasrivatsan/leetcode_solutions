class Solution:
    def reverseWords(self, s: str) -> str:
        l=list(s.split())
        l1=[]
        for i in range(len(l)):
            l[i].strip()
            l1.append(l[i])
        l1.reverse()
        st=""
        for a in l1:
            st=st+a+" "
        st=st[:-1]
        return st
        