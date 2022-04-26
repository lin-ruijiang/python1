# 林睿江
# 新的一天，新的活力，新的希望
# fp=open('001.txt','w')
# print('做好自己最重要',file=fp)
# fp.close()
#
# with open('001.txt','w') as file:
#     file.write('做好自己最重要')
#
# print('星期日','今天')
# print('-----------------------------------')
# print('08时','11时','14时','17时','20时','23时')
# print('0 ℃','6 ℃','10 ℃','4 ℃','1 ℃','0 ℃')
# print('-----------------------------------')
# print('明  天','2/23','2℃/11℃')
# print('星期二','2/24','2℃/12℃')
# print('星期三','2/24','-2℃/18℃')
# print('星期四','2/24','6℃/22℃')
# print('星期五','2/24','1℃/13℃')
# print('星期六','2/24','9℃/32℃')
# lst_sig=['1','2','3','4','5']
# lst_name=['A','B','C','D','E']
# for s,name in zip(lst_sig,lst_name):
#     print(s,name)
# print('\033[0;35m\t\t图书音像勋章、033[m')
# height = 178
# weight = 65
# bmi = weight / (height + weight)
# print('你的BMI值为：' + '{:0.2f}'.format(bmi))
# def func():
#     num = int(input('请输入一个十进制数：'))
#     print(bin(num))
#     print(str(num) + '的二进制数为' + bin(num))
#     print('%s的二进制数为%s' % (num, bin(num)))
#     print('{0}的二进制数为{1}'.format(num, bin(num)))
#     print(f'{num}的二进制数为{bin(num)}')
#     print((oct(num)))
#     print(hex(num))
#
#
# if __name__ == '__main__':
#     while True:
#         try:
#             func()
#             break
#         except:
#             print('输入有误，重新输入')

# pwd = input('支付宝支付密码：')
# if pwd.isdigit():
#     print('支付密码合法')
# else:
#     print('支付数字不合法，支付密码只能是数字')

#  print('支付密码合法' if pwd.isdigit() else '支付密码不合法，只能是数字')

# for i in range(1, 10):
#     print(i)
# year = [82, 89, 88, 86, 85, 00, 99]
# for index, value in enumerate(year):
#     if str(value) != '0':
#         year[index] = int('19' + str(value))
#     else:
#         year[index] = int('200' + str(value))
# year.sort()
# print(year)

# cons = ['白羊', '金牛', '双子', '狮子']
# nature = ['积极', '老实', '狡猾', '热情阳光']
# d = dict(zip(cons, nature))
# print(d)

# def calc(a, b, op):
#     if op == '+':
#         return add(a, b)
#     elif op == '-':
#         return sub(a, b)
#     elif op == '*':
#         return mul(a, b)
#     elif op == '/':
#         return div(a, b)
#
#
# def add(a, b):
#     return a + b
#
#
# def sub(a, b):
#     return a - b
#
#
# def mul(a, b):
#     return a * b
#
#
# def div(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return '除数不能为0'
#
#
# if __name__ == '__main__':
#     a = int(input('请输入第一个整数'))
#     b = int(input('请输入第二个整数'))
#     op = input('请输入运算符')
#     print(calc(a, b, op))

# try:
#     score = int(input('请输入分数：'))
#     if 0 <= score <= 100:
#         print('分数为：', score)
#     else:
#         raise Exception('分数不正确')
# except Exception as e:
#     print(e)

# def is_triangle(a, b, c):
#     if a < 0 or b < 0 or c < 0:
#         raise Exception('三角形边长不能为负数')
#
#     if a + b > c and b + c > a and a + c > b:
#         print(f'三角形的边长为a={a},b={b},v={c}')
#     else:
#         raise Exception(f'a={a},b={b},c={c}不能构成三角形')
#
#
# if __name__ == '__main__':
#     try:
#         a = int(input('请输入第一条边'))
#         b = int(input('请输入第二条边'))
#         c = int(input('请输入第三条边'))
#         is_triangle(a, b, c)
#     except Exception as e:
#         print(e)

# class Instrument():
#     def make_sound(self):
#         pass
#
#
# class Erhu():
#     def make_sound(self):
#         print('二胡在演奏')
#
#
# class Piano():
#     def make_sound(self):
#         print('钢琴在演奏')
#
#
# class Violin():
#     def make_sound(self):
#         print('小提琴在演奏')
#
#
# def play(instrument):
#     instrument.make_sound()
#
# class Bird():
#     def make_sound(self):
#         print('小鸟在唱歌')
#
#
# if __name__ == '__main__':
#     play(Erhu())
#     play(Piano())
#     play(Violin())
#     play(Bird()) # 鸭子类
#
# import prettytable as pt
#
#
# def show_ticket(row_num):
#     tb = pt.PrettyTable()
#     tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
#     for i in range(row_num):
#         lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
#         tb.add_row(lst)
#     print(tb)
#
#
# if __name__ == '__main__':
#     row_num = 13
#     show_ticket(row_num)

# import datetime
#
#
# def inputdate():
#     indate = input('输入开始日期')
#     indate = indate.strip()
#     datestr = indate[0:4] + '-' + indate[4:6] + '-' + indate[6:]
#     return datetime.datetime.strptime(datestr, '%Y-%m-%d')
#
#
# if __name__ == '__main__':
#     sdate = inputdate()
#     in_num = int(input('请输入间隔天数：'))
#     fdate = sdate + datetime.timedelta(days=in_num)
#     print(str(fdate).split(' ')[0])

# import time
#
#
# def show_info():
#     print('请输入提示数字，执行相应操作：0.退出 1.查看登录日志')
#
#
# def write_logininfo(username):
#     with open('log.txt', 'a') as file:
#         s = f'用户名{username},登录时间：{time.strftime("%Y-%m-%d %H:%m:%S", time.localtime(time.time()))}'
#         file.write(s)
#         file.write('\n')
#
#
# def read_logininfo():
#     with open('log.txt', 'r') as file:
#         while True:
#             line = file.readline()
#             if line == '':
#                 break
#             else:
#                 print(line, end='')
#
#
# if __name__ == '__main__':
#     # print(time.localtime(time.time()))
#     # print(time.strftime("%Y-%m-%d %H:%m:%S",time.localtime(time.time())))
#     username = input('请输入用户名：')
#     password = input('请输入密码：')
#     if 'admin' == username and 'admin' == password:
#         print('登录成功！')
#         write_logininfo(username)
#         show_info()
#         num = int(input('请输入操作数字：'))
#         while True:
#             if num == 0:
#                 print('退出成功')
#                 break
#             elif num == 1:
#                 print('查看登陆日志')
#                 read_logininfo()
#                 num = int(input('请输入操作数字：'))
#             else:
#                 print('输入数字有误，请重新输入')
#                 show_info()
#                 num = int(input('请输入操作数字：'))
#     else:
#         print('用户名或密码不正确！')


