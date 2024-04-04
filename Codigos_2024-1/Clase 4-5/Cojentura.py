def conjetura(num):
    print(num)
    if num == 1:
        return 1
    elif num % 2 == 0:
        return conjetura(num/2)
    else:
        return conjetura((3* num) + 1)
        
print(conjetura(10000))