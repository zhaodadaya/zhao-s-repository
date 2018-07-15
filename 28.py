age=int(input('请输入您的年龄:'))
subject=input('请输入您的专业:')
college=input('请输入重点大学or非重点大学:')
if subject == '电子信息工程':
    if age > 25 or college == '重点大学':
        print('恭喜获得面试资格')
elif age < 28 and subject == '计算机专业':
    print('恭喜获得面试资格')
else:
    print('抱歉，您未达到面试要求') 
