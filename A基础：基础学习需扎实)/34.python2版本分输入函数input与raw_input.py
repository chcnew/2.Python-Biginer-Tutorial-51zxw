"""引用元组与字典的实验：
小明 年龄13 语文90 数学92 理综212
小红 年龄14 语文121 数学95 理综235
小岑 年龄15 语文135 数学145 理综295
请使用做一个字典以输入某同学的名字查出该同学的全部信息。

了解输入函数input 和 raw_input
1.input()函数输入：
格式： 变量名=input('请输入文字说明')
2. raw_input函数输入：
格式：变量名=raw_input('请输入说明文字')
3. input()和raw_input()的区别

"""
xiaoming = ("姓名:小明", "年龄:13", "语文:90", "数学:92", "理综:212")
xiaohong = ("姓名:小红", "年龄:14", "语文:121", "数学:95", "理综:235")
xiaocen = ("姓名:小岑", "年龄:15", "语文:135", "数学:145", "理综:295")

a = {"小明": xiaoming, "小红": xiaohong, "小岑": xiaocen}
b = input("请输入你要查询的名字：")

if b == "小明" or b == "小红" or b == "小岑":
    print("查询信息的名字为：", b)
    c = a[b]
    print(c)
else:
    print("输入信息错误！")
