# --coding:utf-8--
import time


def outer(x):
    def inner():
        print(x)

    return inner
outer(5)()
closure = outer(5)
closure()


def runFunc(t):
    print 'start sleeping for %ss' % t
    time.sleep(t)
    print 'ok'


if __name__ == '__main__':
    t = 15
    runFunc(t)
