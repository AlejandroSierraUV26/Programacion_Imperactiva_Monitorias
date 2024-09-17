# Conjetura de Collatz


# Num -> Par => num/2
# Num -> InPar => (num * 3) + 1


def Es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def collazt(num):
    if Es_par(num):
        return num/2
    else:
        return (num * 3) + 1
num = 10000000
i = 1
while i<=num*2:
    num = collazt(num)
    print(num)
    print()
    
    i+=1