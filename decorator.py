# def addspam(fn):
#     def new(*args):
#         print('spam,spam,spam')
#         return fn(*args)
#     return new
#
#
# @ addspam
# def useful(a, b):
#     print(a**2+b**2)
#
# if __name__ == "__main__":
#     useful(5, 4)

# 装饰器的定义是：“为函数动态添加一些功能，并不能改变原函数的行为”。具体参见廖雪峰装饰器章节下面的评论
def typed_detect(fn):
    def wrapper(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return fn(a, b)
        else:
            print('类型错误')
    return wrapper #形成闭包


@ typed_detect
def add(a, b):
    print(a+b)
    return a+b

if __name__ == '__main__':
    add(4, 4)
    add(4.5, 4)
    add(6.3, 4.4)
    add('asda', 7)
    add('dasad', 8.9)
    print(add(4, 5))
    print(typed_detect(add(4, 5)))


# 装饰器可以看作是一种语法糖吧，通过闭包就可以实现了。
# 随手写个简单的例子
#
# def mydecorator(func):
#     def newfunc():
#         xxxx
#         func()
#         xxxx
#     return newfunc
#
# def func():
# xxxx
# func = mydecorator(func)
#
# 就等价于
#
# @mydecorator
# def func():
# xxxx
