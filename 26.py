i=100
while i<1000:
    a=i%10
    b=(i//10)%10
    c=i//100
    if i == a**3+b**3+c**3:
        print('所有水仙花为:%d'%i)
    i+=1
