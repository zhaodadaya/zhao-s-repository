print(' ')
print('为了您和他人的安全，严禁酒后驾车！')
num=int(input('请输入每100毫升血液的酒精含量：'))
print(' ')
if num < 9999999:
    if num<20:
        print('您还构不成饮酒行为，可以开车，但是要注意安全')
    elif num>=20 and num<80:
        print('已经到达酒后驾驶标准，请不要开车')
    else:
        print('已经到达醉酒驾驶的标准，请千万不要开车！')
