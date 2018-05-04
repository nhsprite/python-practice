import datetime


def year():
    name = input("please input your name:")
    age = int(input("please input your age:"))
    now = datetime.datetime.now()

    # python中的局部变量是小写字母，用_分隔;
    year_gap = 100 - age
    print('hello %s, you will become 100 years old in year %d' % (name, now.year + year_gap))


def repeat():
    msg = input("please some message:")
    count = int(input('please input the repeat count:'))
    print(msg * count)


def repeat_newline():
    msg = input("please some message:")
    count = int(input('please input the repeat count:'))
    print((msg + '\n') * count)


if __name__ == '__main__':
    year()
