print('2017~2018赛季NBA西部联盟前8名：')
name=['火箭','勇士','开拓者','爵士','鹈鹕','马刺','雷霆','森林狼']
for a,b in enumerate(name):
    c={a:b}
    for i in c.keys():
        if i%2==0:
            print(c[a],'\t',end='')
        else:
            print(c[a],'\n')
