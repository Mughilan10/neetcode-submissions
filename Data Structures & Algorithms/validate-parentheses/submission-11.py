class Solution:
    def isValid(self, s: str) -> bool:
        d={"{":"}","[":"]","(":")"}
        st=[]
        for i in s:
            if i in d:
                st.append(i)
            elif st and i==d[st[-1]]:
                st.pop()
            else:
                return False
        return len(st)==0