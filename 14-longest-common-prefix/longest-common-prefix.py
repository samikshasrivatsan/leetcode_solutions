class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=strs[0]
        for a in strs:
            if len(res)>len(a):
                res=res[:len(a)]
            for i in range(len(res)):
                if res[i]!=a[i]:
                    res=res[:i]
                    break
        return res