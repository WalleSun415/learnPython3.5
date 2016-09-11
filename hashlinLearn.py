import hashlib

db = {}


def get_md5(password_encode):
    md5 = hashlib.sha1() # or MD5
    password_encode += 'the-Salt'
    md5.update(password_encode.encode('utf-8'))
    return md5.hexdigest()


def register(username, password):
    if username in db:
        print('该用户名已被注册，请更改用户名！')
    else:
        db[username] = get_md5(username + password)
        print('%s注册成功!' % username)


def login(username, password):
    if username in db:
        if db[username] == get_md5(username + password):
            print('%s登陆成功!' % username)
        else:
            print('%s密码错误！' % username)
    else:
        print('用户名%s不存在' % username)


register('swl', 'dasdas')
register('liming', '12345')
register('han', 'das')
login('liming', '12345')
login('han', 'dasdsds')
login('hssan', 'dasdsds')
print(db)