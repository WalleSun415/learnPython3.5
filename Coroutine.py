# [PRODUCER]Producing 1...
# [CONSUMER]Consuming 1...
# [PRODUCER]Consumer return: 200 OK
# [PRODUCER]Producing 2...


# def consumer():
#     r = ""
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER]Consuming %s...' % n)
#         r = '200 OK'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n += 1
#         print('[PRODUCER]Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER]Consumer return: %s' % r)
#     c.close()
#
# c = consumer()
# produce(c)

def consumer():
    r = ""
    while True:
        print('r-->%s' % r)
        n = yield r + ' 1000 OK'
        # 1.  对于send(None)为启动生成器，执行到yield r + ' 1000 OK'时暂停，保存环境，返回值为' 1000 OK'，即m为' 1000 OK'
        # 1.1 send(None)相当于第一次执行next(),send和next相比;多了一次赋值的动作，其他的流程是相同的
        # 2.  对于send(1)，先是执行n = yield部分传递参数，并不执行yield后的语句部分;到下一个循环执行yield r + ' 1000 OK'时再暂停保存环境，
        #     返回值为r + ' 1000 OK'，即m为'200 OK 1000 OK'
        # 3.1 对于n = yield r + ' 1000 OK'，(yield r + ' 1000 OK')为一个表达式，值为send(msg)传递的msg
        # 3.2 对于n = yield r + ' 1000 OK'，每次保存环境并返回，保存当前的r值，返回值为yield后的表达式，即r + ' 1000 OK'
        if not n:
            return
        print('[CONSUMER]Consuming %s...' % n)
        r = ' 200 OK' + r


def produce(c):
    m = c.send(None)
    print('m-->%s' % m)
    n = 0
    while n < 2:
        n += 1
        print('[PRODUCER]Producing %s...' % n)
        h = c.send(n)
        print('[PRODUCER]Consumer return: %s' % h)
    c.close()

a = consumer()
produce(a)
