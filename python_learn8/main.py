#捕获异常，在可能出现异常的语句捕获异常，提供解决方案，而不是任由其程序无法运行，有点类似于C语言中的Warning
#捕获异常的语法,捕获全部异常
# try:                           #后面放置可能出现的语句
#     f = open("E:/ABC.txt","r",encoding="UTF_8")
# except:
#     f = open("E:/ABC.txt","w",encoding="UTF_8")
#     print("出现异常")
# #捕获指定异常，要知道异常的名字
# try:                           #后面放置可能出现的语句
#     f = open(name)
# except NameError as e:         #程序中的NameError就是异常名称，e为对该异常的解释
#     name = 0
#     print(name)
#     print(e)
#用Exception来捕获所有的异常
# try:                           #后面放置可能出现的语句
#     f = open(name)
# except Exception as e:         #程序中的Exception是最高级异常名称，可以捕获所有异常，并用e为输出该异常的解释，并进行其他操作
#     name = 0
#     print(name)
#     print(e)
# else:                          #如果没有出现异常的情况，要进行的操作
#     print("happy")
# finally:                       #无论有没有异常出现都要运行
#     print("check-succeed")
#异常的传递性，可以在不同的函数之间进行传递
# def func1():
#     number = 1/0
# def func2():
#     func1()
# def main():
#     try:
#         func2()
#     except Exception as e:
#         print(e)
#         print("传递成功")
# main()
#Python自带模块的使用方法
#import导入全部的模块函数
# import time
# print("你好，世界")
# time.sleep(3)
# print("Hellow world")
#from函数引入个别函数类型
# from time import sleep
# print("你好，世界")
# sleep(3)
# print("Hellow world")
#用*来引出全部的函数名称，注意此时不能用模块名称来引出对应函数
# from time import *
# print("你好，世界")
# sleep(3)
# print("Hellow world")
#用as来改写模块或者是函数的名称
# import time as Delay
# print("你好，世界")
# Delay.sleep(3)
# print("Hellow world")
#修改函数名称
# from time import sleep as Delay
# print("你好，世界")
# Delay(3)
# print("Hellow world")
#自定义外部模块,简单运用
# import test
# test.test1(2,1)
# test.test2(2,1)
#main变量的功能，导入该模块后，如果在自定义模块中有输出，而我不想输出这个数据，则用main标记要不需要外部运行的程序
# import test
#当使用*号引出所有的模块函数的时候，用All来标记哪些功能会被导入，若没有all，则默认全部导入，All是一个数组
# from test import *
# test1(2,1)
# test2(2,1)
#不同模块的同名函数，后导入的会覆盖先导入的
# from test import *
# from test2 import *
# test1(2,1)
#Python数据包相当于一个自建的存放自己外部的模块的文件夹，跟Handware很像
# from my_package.moudle_1 import  test3
# from my_package.moudle_2 import  test1
# test1(2,1)
# test3(2,1)
#*的使用与模块的*类似，即在_init_.py中来标记处可以使用的模块
#第三方包的下载-国外网站 pip install 包名称
#第三方包的下载-国内网站 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称
#综合案例制作，自定义工具包

