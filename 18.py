name=123456
num=123456
money=100
in_name=int(input('请输入您的帐号\n'))
in_num=int(input('请输入您的密码\n'))
if in_name==name and in_num==num:
    print('密码正确，请输入取款金额')
    in_money=int(input())
    balance=money-in_money    
    if balance>=0:
        print('您已支取%d元，剩余%d元'%(in_money,balance))
    else:
        print('金额不足')
else:
    print('非法账户')
