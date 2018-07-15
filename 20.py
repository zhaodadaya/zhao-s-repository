num=int(input('请输入年份\n'))
if num%4 == 0 and num%100 != 0 or num%400 == 0:
    print('%d为润年'%num)
else:
    print('%d为平年'%num)
