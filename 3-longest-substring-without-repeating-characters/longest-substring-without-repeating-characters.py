class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        st=""
        for ch in s:
            while ch in st:
                st=st[1:]
            st+=ch
            l=max(l,len(st))
        return l