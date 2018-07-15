print('-----跳一跳，请输入‘退出’即可退出游戏-----')
print('欢迎回来，请开始游戏\n请输入\\（中心、音乐模块、微信支付模块）')
while True:
    in_ = input('请输入：')
    if in_ == '中心':
        print('您的分数为：32')
    elif in_ == '音乐模块':
        print('您的分数为：30')
    elif in_ == '微信支付模块':
        print('您的分数为：42')
    elif in_ == '退出':
        print('已退出')
        break
    else:
        print('输入有误，请重新输入')
        continue
    
    
        
