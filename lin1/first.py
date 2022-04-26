# 林睿江
# 新的一天，新的活力，新的希望
# print(520)
# print('helloworld')
# print(3+1)
# fp=open('D:/test.txt', 'a+')
# # 文件不存在就创建，存在就追加
# print('helloworld', file=fp)
# fp.close()
# print('hello','world','python')
# # 同行输出
# print('hello\rworld')
# # 覆盖
# print('hello\b')
# # 回退
# print(r'hello\nworld')
# # 加r或R输出原字符而不是转义字符，最后一个字符不能是反斜杠
# print(chr(0b100111001011000))
# # 二进制编码
# print(ord('乘'))
# f1=True
# f2=False
# print(f1+f2)
# #  单引号，双引号，三引号（可以在多行显示字符串）
# name = '张三'
# age = 20
# print('我叫'+name+'，今年'+str(age)+"岁")
#  数据类型转换，转成string,int,float
# 整数字符串可以转为int，小数字符串不可以转
# 非数字串不允许转换，整数转float加.0，比如98转为98.0
# 单行注释，三引号多行注释，中文编码声明 #coding:utf-8
# present = input('我想要变得强大')
# print(present , type(present))
# print (type('python'))
# a=input('请输入一个加数:')
# b=input('请输入另一个加数:')
# a=int(a)
# b=int(b)
# print (type(a),type(b))
# print (a+b)
# print(1/2)
# print(11//2)
# print(2**4)
#  除法/  整除//  取余（模）% 幂运算 ** 一正一负向下取整
#  赋值运算符顺序从右到左，链式赋值a=b=c=20，a,b,c=20,30,40
# a,b=10,20
# a,b=b,a
# print(a,b)
# 可以实现交换
# ==比较的是值，is比较的是标识(id)，创建一个变量值相同时就会指向这个标识
# a,b=10,10
# print( a == b)
# print( a is b)
# and 并符号 or 或符号 not 取反 in 在当中 not in 不在当中
# # 例：
# s= 'helloword'
# print('w' in s)
# print('k' not in s)

# 位与&，位或|，<<左移
# print(4<<1)
# print(4<<2)
# print(4>>1)
# print(4>>2)
# 优先级:括号>算术运算符>按位运算符>比较运算符>布尔运算符>赋值运算符,位左右移大于按位与大于按位或，并and大于或or
# print('1')
# print('2')
# print('3')
# print('4')
# a=100
# if  a > 101:
#     print(a)
# else:
#     print(a-100)
# 没有分号，严格缩进来表示分号
# pass 跳过，先占一个语句的位置
# range()内置函数,range(start,stop,step)创建一个[start,stop）之间的整数序列，步长为step；
# a=1
# while a<10:
#     print(a)
#     a+=1
# for item in 'Python':
    # 可迭代序列
    # print(item)
    # 在循环体中不用自定义变量，可将自定义变量写为‘_’
    # for _ in range(5)
    # break,没区别，continue结束当前循环，进入下一循环
    # 列表 增加操作
# lst=[10,20,30]
# print ('添加元素之前',lst,id(lst))
# lst.append(100)
# print('添加元素之后',lst,id(lst))
# lst2=['hello','world']
# lst.append(lst2)
# print(lst)
# lst.extend(lst2)
# print(lst)
# # append 在列表末尾添加一个元素，extend，在列表末尾添加至少一个元素
# lst.insert(1,90)
# print(lst)
# # insert 在指定位置插入一个元素
# lst3=[True,False,'hello']
# lst[1:]=lst3
# print(lst)
# 切片,在列表任意位置添加至少一个元素
# lst=[10,20,30,40,50,60,30]
# # lst.remove(30)
# # print(lst)
# # # remove移除指定元素,重复元素移除第一个
# # # pop,删除指定索引,不指定删除列表最后一个元素,不存在和超出都会报错
# # lst.pop(2)
# # print(lst)
# # new_list=lst[1:3]
# # print(lst)
# # print(new_list)
# # # 切片,产生一个新的列表对象
# # lst[1:3]=[]
# # print(lst)
# # # 对原列表做切片,用一个空列表接受,从而删除原列表中的内容,不产生新的列表对象
# # lst.clear()
# # print(lst)
# # del lst
# # print(lst)
# # #clear清空列表,delete删除列表
# 修改直接指定索引段即可
# 排序,sort(),默认升序,在原列表基础上进行的
# lst=[10,20,40,90,30,60]
# lst.sort()
# print('排序后的列表',lst)
# lst.sort(reverse=True)
# 降序
# new_list=sorted(lst)
# print(lst)
# print(new_list)
# desc_list=sorted(lst,reverse=True)
# print(desc_list)
# # sorted生成新的列表排序,对原列表不产生改变
# lst=[i for i in range(1,10)]
# lst1=[i*i for i in range(1,10)]
# print(lst)
# print(lst1)
# 列表生成式

# {}字典,与列表一样也是可变序列,以键值对的方式存储数据,字典是一个无序的序列,hash函数,根据关键字key查找value值所在的位置
# scores={'张三':100,'李四':98,'王五':45}
# # student=dict(name='jack',age=20)
# # print(scores)
# # print(type(scores))
# # print(student)
# print(scores['张三'])
# print(scores.get('张三'))
# # 查找的两种方式,如果查找的方式不存在,[]会报错,get()则会输出None
# # 判断是否存在,删除\清空和新增\修改
# print('张三' in scores)
# del scores['张三']
# scores.clear()
# print(scores)
# scores['陈六']=100
# print(scores)
# scores['陈六']=123
# print(scores)
# 获取字典视图
# scores={'张三':100,'李四':98,'王五':45}
# keys=scores.keys()
# print(keys)
# print(type(keys))
# print(list(keys))
#
# values=scores.values()
# print(values)
# print(type(values))
# print(list(values))
#
# items=scores.items()
# print(items)
# print(type(items))
# print(list(items))#元组,转换之后的列表元素是由元组组成

# 字典的遍历
# for item in scores:
#     print(item,scores[item],scores.get(item))
# # 字典的key不可以重复,值value可以重复,元素是无序的,字典中的key是不可变对象,不能用列表做key,字典也可以根据需要动态地伸缩
# # 字典会浪费较大的内存,是一种使用空间换时间的数据结构
#
# 字典生成式
# 内置函数zip()
# items=['fruits','books','others']
# prices=[96,78,85]
# d = { item : price for item, price in zip(items, prices)}
# print(d)

# 元组,集合
# 元组是python内置的数据结构之一,是一个不可变序列,即发生改变后地址发生了更改,不允许修改元组中本身不可变对象
# t=('Python','world',98)
# print(t)
# print(type(t))
#
# t='Python','world',98 # 省略了小括号
# print(t)
# print(type(t))
#
# # 元组中只包含一个元素需要使用逗号和小括号,以和int,string区分
# t=('Python',)
# print(t)
# print(type(t))
#
# t1=tuple(('python','world',98))
# print(t1)
# print(type(t1))
#
# lst=[]
# lst1=list()
#
# d={}
# d2=dict()
#
# t4=()
# t5=tuple()
# 空列表\空字典\空元组
# 遍历
# t=('Python','aaaa',98)
# for item in t:
#     print(item)
#     集合，可变类型的序列，
#     集合不允许元素重复，重复元素不会输出
# s={2,3,4,5,6,7,7}
# print(s)
# # 内置函数set(),可以将元组、列表转化为集合，集合元素无序
# s1=set(range(6))
# print(s1,type(s1))
# s2=set([1,2,3,4,5,6,7,8])
# print(s2)
# s3=set('python')
# print(s3,type(s3))
# # 空集合
# set()
# s1={10,20,30,40,50,60}
# print(s1)
# print(10 in s1)
# 添加，add一次一个，update一次至少一个
# s1.add(80)
# print(s1)
# # s1.update({200,300,500})
# # s1.update([200,300,500])
# # s1.update((200,300,500))
# print(s1)
# s1.remove(10)
# print(s1)
# s1.discard(20)
# print(s1)
# discard ,指定元素不存在也不报错
# s1.pop()
# print(s1)
# # pop删除任意一个元素
# s1.clear()
# print(s1)
#
# s1={10,20,30,40,50,60}
# s2={100,30,60}
# #
# print(s1==s2)
# # print(s2.issubset(s1))# 判断是否为子集，子集的反义词是超集
# # print(s1.issuperset(s2)) # 判断是否为超集
# # print(s1.isdisjoint(s2))  # 判断两个集合是否不相交
# print(s1.intersection(s2))
# print(s1&s2)  # 求交集的两种操作
# print(s1.union(s2))
# print(s1|s2)  # 求并集的两种操作
# print(s1.difference(s2))
# print(s1-s2) # 求差集的两种操作
# print(s1.symmetric_difference(s2))
# print(s1^s2) # 求对称差集的两种操作

# 集合生成式
# s={i*i for i in range(0,10)}
# print(s)
# 字符串，python里相同的字符串就指向一个内存，字符串的驻留机制，交互式时，字符串长度为0或1时，符合标识符的字符串，字符串只在编译时进行驻留，而非运
# 行时，【-5，256】之间的整数数字，pycharm编译会优化
# 优点：避免频繁的创建和销毁，提升效率和节约内存，拼接字符串和修改字符串是会比较影响性能的，字符串拼接时建议用join方法，而非+，join()方法先计算再拷
# 贝，只new一次对象，效率高
# 字符串的查找，+r最后一个，find和index，没找到find（）返回-1，index会抛异常
# s='hello,hello'
# print(s.index('lo'))
# print(s.find('lo'))
# print(s.rindex('lo'))
# print(s.rfind('lo'))
# print(s.find('m'))
# upper() lower() swapcase() capitalize() title()
# 全部大写 全部小写  大写变小写小写变大小 第一个字符转换为大写，其余字符小写 每个单词第一个字符大写，其余小写
# 字符串对齐 center()居中对齐 ljust()左对齐 rjust()右对齐 zfill（） 0填充
# s='python is best'
# # print(s.center(20,'*'))
# # print(s.ljust(20,'*'))
# # print(s.rjust(20,'$'))
# # print(s.zfill(20))
# # 字符串的劈分,rsplit从右往左,maxspilt指定最大分割次数
# print(s.split())
# s1='python|is|best'
# print(s1.split(sep='|'))
# print(s1.split(sep='|',maxsplit=1))
# print(s.rsplit())
# print(s1.rsplit(sep='|',maxsplit=1))
# s='python is good'
# print(s.isidentifier())
# # isidentifier()判断是不是合法的标识符，字母数字下划线
# s1=' \t'
# print(s.isspace())
# print(s1.isspace())
# # 是否全部由空白字符组成
# print(s.isalpha())
# # 是否全部由字母组成
# print(s.isdecimal())
# # 是否全部由十进制数字组成
# s2='四'
# print(s.isnumeric())
# print(s2.isnumeric())
# # 是否全部由数字组成,罗马数字也是数字，中文数字也是数字
# print(s.isalnum())
# 是否全部由字母和数字组成
# s='python is good'
# # 替换与合并,replace第三个参数可以用于控制替换的最多次数
# print(s.replace('python','java',2))
# lst=['hello','java','python']
# t=('hello','java','python')
# print('|'.join(lst))
# print(' '.join(lst))
# print(' '.join(t))
# print('*'.join('python'))
# 两个字符比较的是原始值，ord（）调用原始值，chr()获取原始值对应的字符
# print(chr(97),chr(98))
# print("林">"猪")
# print(ord("林"))
# # print(ord("猪"))
# 字符串不具备增、删、改等操作
# 切片将产生新的对象,有个步长
# s="12143244adada"
# print(s[1:5:1])
# 格式化字符串，同c
# name='张三'
# age=20
# print('%s,%d' % (name,age))
# # print('{0},{1}',format(name,age))
# print(f'{name},{age}')
# print('%10.3f' % 3.1415926)
# print('{0:.3f}'.format(3.1415926))
# 字符串编码与解码，编码与解码方式要相同
# s='我是第一名'
# print(s.encode(encoding='GBK'))
# print(s.encode(encoding='UTF-8'))
# byte=(s.encode(encoding='GBK'))
# print(byte.decode(encoding='GBK'))
# def calc(a,b):
#     c=a+b
#     return c
# # result = calc (100,20)
# result = calc (b=100,a=20)
# print(result)
# 可以根据形参名称进行实参传递，可变对象形参影响实参，不可变不影响
# 返回值为多个时，返回一个元组
# def fun1(*args):
#     print(args)
#
# fun1(10,30)
# #结果为一个元组
# def fun2(**args):
#     print(args)
#
# fun2(a=10)
# #结果为一个字典
# # 个数可变的位置参数和个数可变的关键字参数都只能有一个
# try:
#     a= int (input('请输入一个整数'))
#     b= int (input('请输入一个整数'))
#     result =a /b
# except BaseException as e:
#     print('出错了',e)
# else:
#     print('计算结果为：',result)
# finally:
#     print('谢谢你的使用')
# print('程序结束')
# import traceback
# try:
#     print('--------------------------')
#     print(1/0)
# except:
#     traceback.print_exc()
# i=1
# while i<=10:
#     print(i)
#     i+=1
# 类名的规范，类名的每个单词首字母大写，其余小写,类之外定义成为函数，类之内定为方法
# class Student:
#     pass
# print(Student)
# 学生类模板
# class Student:
#     native_pace='杭州'
#     def __init__(self,name,age):
#          self.name=name
#          self.age=age
#
#     def eat(self):
#         print('学生在吃饭')
#
#     @staticmethod
#     def method():
#         print('静态方法')
#
#
#     @classmethod
#     def cm(cls):
#          print('类方法')
# #  实例对象可以用类指针调用类对象，内存地址不同
#
# stu= Student('张三',20)
# stu.eat()
# Student.eat(stu)
# Student.cm()
# Student.method()

# 动态绑定属性和方法
# 封装 继承 多态
# class Car:
#     def __init__(self,brand,age):
#         self.brand=brand
#         self.__age=age
#     def start(self):
#         print('车启动啦')
#         print(self.brand,self.__age)
# car=Car('豹猫',20)
# car.start()
# # __表示不被访问,可以强行访问
# print(car._Car__age)

# 继承，提高代码的复用性，多继承，方法重写
# object类是所有类的父类
# class C(A,B):
# print(class)默认调用__str__方法

# 多态，鸭子类型，动态语言的多态，不需要关心对象是什么类型，只关心对象的行为
# print(dir(object))
# class B:
#     pass
# class A:
#     pass
# class C(A,B):
#     def __init__(self,name):
#         self.name=name
#
# x=C('Jack')
# print(x.__dict__) # 实例对象的属性字典
# print(C.__dict__) # 类对象的属性字典
# print(x.__class__) # 类型
# print(C.__bases__) # 父类的元组
# print(C.__base__) # 父类的第一个元组
# print(C.__mro__) # 类的层次结构
# print(A.__subclasses__()) #子类的列表

# new，init方法，浅拷贝与深拷贝，默认浅拷贝，copy函数子对象不拷贝
# 深拷贝 copy模块的deepcopy，子对象也拷贝
# 模块化编程 Modules

# import  math
# print(math)
# print(dir(math))
# print(math.pow(2,3))
# print(math.ceil(10.5))
# print(math.floor(10.6))
# from math import  pi
# print(pi)
# # import calc
# #导入自定义模块，make directory ,sources root
# def add(a,b):
#     return a+b
# if __name__=='__main__':
#     print(add(10,20))
# 以主程序方式运行，在被调用时不编译
# 包，是一个分层次的目录结构，将一组功能相近的模块组织在一个包下，代码规范，避免模块名称冲突
# 包与目录的区别 ，包有__init__（）函数
# import pageage1.moudule_A as ma
# print(ma,a)
# 常用的内容模块
# import sys
# import time
# import os
# import urllib.request
# #josn,math,re,decimal,logging
#
# print(sys.getsizeof(200))
#
# print(time.time())
# print(time.localtime(time.time()))
# print(urllib.request.urlopen('http://www.baidu.com').read())
#
# import schedule
# import time
# def job():
#     print('哈哈 -------')
#
# schedule.every(3).seconds.do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# python的解释器使用的是U你从的，.py文件在磁盘上使用UTF-8存储（外存），UTF-8是Unicode的实现
# 文件的读写
# IO操作
# import io
# file=open(filename [,mode,encoding]
# file=open('a.txt','r')
# print(file.readline()) # 读取结果是一个列表
# file.close()
# file=open('b.txt','w') # 覆盖原有内容
# file=open('b.txt','a') # 追加内容
# print(file.write('Python')) # 读取结果是一个列表
# file.close()

# src_file=open('logo.png','rb') # 追加内容
# target_file=open('copylogo.png','wb') # 二进制打开,需要与rb，wb等共它模式一起使用
# target_file.write(src_file.read())
# target_file.close()
# src_file.close()
# + 以读写方式打开
# file=open('a.txt','r')
# print(file.read(2))
# print(file.readline())
# print(file.readlines())
# file.close()

# file=open('b.txt','a')
# file.write('hello')
# lst=['java','python','C++']
# file.writelines(lst)
# file.close()

# file=open('a.txt','r')
# file.seek(2)
# print(file.read())
# print(file.tell())
# file.close()
# # utf-8中，一个中文字符和中文符号都占三个字节，英文都是一个字节
# file.flush() # 把缓冲区的内容写入文件，但不关闭文件
#
# with open('a.txt','r') as file:
#     print(file.read())
#  with语句可以自动管理上下文资源，无论什么原因跳出with块，都能确保文件正确的关闭，以达到释放资源的目的
# import os
# # os.system('notepad.exe')
# # os.system('calc.exe')
# # os.startfile('D:\\program files\\tencent\QQ\\Bin\\QQ.exe')
# # print(os.getcwd()) #返回原目录
# # lst=os.listdir('../lin1') #返回指定目录下的文件和目录信息
# # print(lst)
# # 依次为创建目录、创建多级目录、删除目录、删除多级目录、将path设置为当前工作目录
# os.mkdir('newdir2')
# os.makedirs('A/B/C')
# os.rmdir('newdir2')
# os.removedirs(A/B/C)
# os.chdir('D:\\')

# import os.path
# print(os.path.abspath('')) # 获取文件或目录的绝对路径
# os.path.exists(path) # 判断目录是否存在
# join(path,name) # 将目录与目录或者文件名拼接起来
# spiltext() #分离文件名或扩展名
# basename(path) # 从一个目录中提取文件名
# dirname(path) # 从一个路径中提取文件路径，不包括文件名
# isdir(path) # 用于判断是否为路径

