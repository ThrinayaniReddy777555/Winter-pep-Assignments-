class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # str1 = num1
        # str2 = num2
        # str3=str1+str2
        # return str3
        i,j=len(num1)-1,len(num2)-1
        ans=[]
        c=0
        while i>=0 or j>=0 or c:
            a=0 if i < 0 else int(num1[i])
            b=0 if j < 0 else int(num2[j])
            c,v=divmod(a+b+c,10)
            ans.append(str(v))
            i-=1
            j-=1

        return "".join(ans[::-1]) 