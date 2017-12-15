# --coding:utf-8--
import time


def runFunc(t):
    print 'start sleeping for %ss' % t
    time.sleep(t)
    print 'ok'


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        dct = self.__dict__
        return "Coord: " + str(dct)


class B(object):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print 'a=', self.__a, 'b=', self.__b

    def __call__(self, num):
        print 'call:', num + self.__a


class A(object):
    def __init__(self,a,b):
        self.a1 = a
        self.b1 = b
        print 'init'

    def mydefault(self):
        print 'default'

    def mydefault1(self, *args):
        print 'default:' + str(args[0])

    def __getattr__(self,name):
        print "other fn:", name
        func = self.mydefault
        # return self.mydefault
        return self.mydefault1


if __name__ == '__main__':
    # t = 15
    # runFunc(t)
    # c = Coordinate(100, 200)
    # x = c.x
    # y = c.y
    # print c,x,y
    # a1 = A(10, 20)
    # a1.myprint()
    # a1(80)
    a1 = A(10, 20)
    a1.fn1(['12ad',3,4])
    a1.fn2(1)
    a1.fn3(2)