print('欢迎进入10086自助查询系统：')
num=int(input('查询当前余额请输入：1 \r\n查询当前剩余流量请输入：2 \r\n查询当前剩余通话分钟数请输入：3 \r\n请输入您要查询内容的数字：'))
if num==1:
    print('当前余额为：')
elif num==2:
    print('当前剩余流量为：')
elif num==3:
    print('当前剩余通话分钟数为：')
else:
    print('输入错误，请重新登录')


