from typing import List

def read_integers() -> List[int]:
    a=[]
    x=input()
    s=x.split(",")
    for i in s:
        a.append(int(i))
    return a

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
