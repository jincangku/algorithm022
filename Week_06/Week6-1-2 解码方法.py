class Solution:
    def numDecodings(self, s):
        if s[0]=="0":return 0
        ans=[0 for i in range(len(s)+1)]
        ans[0]=1
        ans[1]=1
        for i in range(1,len(s)):
            if s[i]==0 and not(s[i-1]=="1" or s[i-1]=="2"):
                return 0
            elif 0<int(s[i]):
                ans[i+1]+=ans[i]
            if 9<int(s[i-1:i+1])<27:
                ans[i+1]+=ans[i-1]
        return ans[-1]