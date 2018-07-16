for a in range(1,10):
    for b in range(1,10):
        c=a*b
        print(b,'*',a,'=',c,'\t',end='')
        if a == b:
            print('')
            break
