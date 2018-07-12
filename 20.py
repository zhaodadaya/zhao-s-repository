num=int(input('请输入年份\n'))
zhi=num%4
zhi2=num%100
zhi3=num%400
if zhi==0 and num!=0 or num==0:
    print('%d为润年'%num)
else:
    print('%d为平年'%num)
