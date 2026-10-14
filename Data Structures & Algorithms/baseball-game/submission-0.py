class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for i in operations:
            if i=="+":
                if ans[-1] and ans[-2]:
                    ans.append(ans[-1]+ans[-2])
                continue
            if i=="C":
                if ans[-1]:
                    ans.pop()
                continue
            if i=="D":
                if ans[-1]:
                    ans.append(ans[-1]*2)
                continue
            ans.append(int(i))
        return sum(ans)