# --coding:utf-8--
import redis
import time
from email_service import sendEmail


if __name__ == '__main__':

    # host 指定redis服务器，端口，密码
    r = redis.Redis(host='localhost', port=6379, db=0, password='005912')
    # set(name, value, ex=None, px=None, nx=False, xx=False)
    # ex，过期时间（秒）
    # px，过期时间（毫秒）
    # nx，如果设置为True，则只有name不存在时，当前set操作才执行,同setnx(name, value)
    # xx，如果设置为True，则只有name存在时，当前set操作才执行
    r.set('num', 1)   # 添加
    # print (r.get('name'))   #获取
    while True:
        receiver = ['justsososun@sina.com', 'justsososun@126.com']  # 收件人列表
        subject = 'My Test!'
        num = int(r.get('num'))
        if num > 2:
            print 'Break!'
            break
        msg = 'hello,send by Python.....num=%d' % num
        status, output = sendEmail(subject, msg, receiver)
        if status:
            print 'Success！', output
        else:
            print 'Error!', output
        r.incr('num')
        time.sleep(2)

    print 'Done!'
