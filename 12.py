print('在古希腊神话中，玫瑰集爱情与美丽于一身，所以人们常用玫瑰来表达爱情')
print('但是不同的朵数的玫瑰花代表的含义是不同的')

num=int(input('请输入您想送几朵玫瑰花，我会告诉你玫瑰花的含义：'))
if num==1:
    print('1朵：你是我的唯一')
elif num==3:
    print('3朵：I Love You')
elif num==10:
    print('10朵：十全十美')
elif num==99:
    print('99朵：天长地久')
elif num==108:
    print('108朵：求婚')
elif num==999:
    print('999朵：土豪')
else:
    print('我也不知道了，你可以考虑送1朵、3朵、10朵...')

