def primo(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

if __name__ == "_main_":
    for i in range(1,100):
        if primo(i):
            print(i)