def add_two_numbers() -> int:
    x=input()
    s=x.split(",")
    su=0
    for i in s:
        su+=int(i)
    return su



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
