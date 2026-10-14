class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for i in operations:
            if i=="+":
                if ans[-1] and ans[-2]:
                    ans.append(ans[-1]+ans[-2])
            elif i=="C":
                if ans[-1]:
                    ans.pop()
            elif i=="D":
                if ans[-1]:
                    ans.append(ans[-1]*2)
            else:
                ans.append(int(i))
        return sum(ans)