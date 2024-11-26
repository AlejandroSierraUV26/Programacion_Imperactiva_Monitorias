# for i in range(0,50):
#     if i%2== 0:
#         print(i)
        
        
        
# i = 1
# acc = 0 
# while acc<25000:
#     if i % 7 == 0:
#         acc+=1
#         print(i)
#     i+=1




def Es_primo(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

i = 2
while i<30:
    if Es_primo(i):
        print(i)
    i+=1 