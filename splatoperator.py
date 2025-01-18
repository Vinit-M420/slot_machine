numbers = [1, 2, 3]
print(*numbers)


def multiple(a,b,c):
    total = a * b * c
    return total
    
result = multiple(*numbers)
print(result)    