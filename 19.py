tall=int(input('请输入身高\n'))
money=int(input('请输入身价\n'))
num=int(input('请输入颜值分\n'))
if tall>180 and money>1000000 and num>99:
    print('系统判定您为高富帅')
elif money>1000000 and num>99:
    print('系统判定您为富帅')
elif num>99:
    print('系统判定您为帅')
elif tall<160 and money<100 and num<60:
    print('矮穷矬')
