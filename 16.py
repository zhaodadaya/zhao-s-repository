test={'bh':'1','xz':'水瓶座','rq':'1月20～2月18','xg':'xxx'}
test1={'bh':'2','xz':'双鱼座','rq':'2月19～3月20','xg':'xxx'}
test2={'bh':'3','xz':'白羊座','rq':'3月21～4月18','xg':'xxx'}
test3={'bh':'4','xz':'金牛座','rq':'4月20～5月20','xg':'xxx'}
test4={'bh':'5','xz':'双子座','rq':'5月21～6月21','xg':'xxx'}
test5={'bh':'6','xz':'巨蟹座','rq':'6月21～7月22','xg':'xxx'}
test6={'bh':'7','xz':'狮子座','rq':'7月23～8月22','xg':'xxx'}
test7={'bh':'8','xz':'处女座','rq':'8月23～9月22','xg':'xxx'}
b = input('请输入您的姓名：\n')
a = int(input('请输入数字：'))
if a == 1:
    print('%s您好!%s星座的您分析结果：日期是%s,性格是%s'%(b,test['xz'],test['rq'],test['xg']))
elif a == 2:
    print('%s您好!%s星座的您分析结果：日期是%s,性格是%s'%(b,test1['xz'],test1['rq'],test1['xg']))
elif a == 3:
    print('%s您好!%s星座的您分析结果：日期是%s,性格是%s'%(b,test2['xz'],test2['rq'],test2['xg']))
elif a == 4:
    print('%s您好!%s星座的您分析结果：日期是%s,性格是%s'%(b,test3['xz'],test3['rq'],test3['xg']))
elif a == 5:
    print('%s您好!%s星座的您分析结果：日期是%s,性格是%s'%(b,test4['xz'],test4['rq'],test4['xg']))
elif a == 6:
    print('%s您好!%s星座的您分析结果：日期是%s,性格是%s'%(b,test5['xz'],test5['rq'],test5['xg']))
elif a == 7:
    print('%s您好!%s星座的您分析结果：日期是%s,性格是%s'%(b,test6['xz'],test6['rq'],test6['xg']))
elif a == 8:
    print('%s您好!%s星座的您分析结果：日期是%s,性格是%s'%(b,test7['xz'],test7['rq'],test7['xg']))
