"""
学习装饰器
试用场景 日志，测试，缓存，权限检验，固定格式化
"""


def debug(func):
    def wrapper():
        print(f"debug {func.__name__}")
        return func()
    return wrapper


def say_hello():
    print('hello')
    print('-' * 80)


# py < 2.4
decorator_say_hello = debug(say_hello)


@debug
def decorator_say_hello_new():
    say_hello()


def log(func):
    def wrapper():
        print(f"loging {func.__name__}")
        return func()
    return wrapper


# py < 2.4
log_say_hello = log(say_hello)


@log
def log_say_hello_new():
    say_hello()


# 装饰的函数有参数
def param_log(func):
    def wrapper(*args, **kwargs):
        print(f'param loging {func.__name__}')
        return func(*args, **kwargs)
    return wrapper


@param_log
def say(content):
    print(content)

from functools import wraps


# 装饰器带有参数，因为需要参数，所以要再加一层
def logging(level='INFO'):
    def wrapper(func):
        @wraps(func)
        def inner_warpper(*args, **kwargs):
            print(f'[{level}] {func.__name__}')
            res = func(*args, **kwargs)
            print('finish')
            return res
        return inner_warpper
    return wrapper


@logging(level='INFO')  # 相当于一个函数，直接执行，返回 wrapper 函数，参数 level 由于闭包，带给 wrapper
def say1(c):
    print(c)


@logging(level='INfo')
@logging(level='ERROR')  # 相当于一个函数，直接执行，返回 wrapper 函数，参数 level 由于闭包，带给 wrapper
def say2(c):
    print(c)
    return 'ok'


class ClassLog(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'before call {self.func.__name__}')
        my_res = self.func(*args, **kwargs)
        print(f'after call {self.func.__name__}')
        return my_res


class ClassLogParam(object):

    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            print(f'[{self.level}] before call {func.__name__}')
            func_res = func(*args, **kwargs)
            print(f'[{self.level}] after call {func.__name__}')
            return func_res
        return wrapper


@ClassLog
@ClassLogParam(level='INFO')
def class_say(c):
    print(c)
    return 'ok'


# 函数装饰器
def add_tag(func):
    def wrapper(*args, **kwargs):
        print(f'before add tag {func.__name__}')
        func_res = func(*args, **kwargs)
        print(f'after add tag {func.__name__}')
        return func_res
    return wrapper


# 带有参数的函数装饰器
def param_add_tag(tag='[<a>]'):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print(f'{tag} before call {func.__name__}')
            func_res = func(*args, **kwargs)
            print(f'{tag} after call {func.__name__}')
            return func_res
        return inner_wrapper
    return wrapper


# 类装饰器
class ClassAddTag(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'before call {self.func.__name__}')
        func_res = self.func(*args, **kwargs)
        print(f'after call {self.func.__name__}')
        return func_res


# 带有参数的类装饰器
class ClassAddTagParam(object):
    def __init__(self, level='[class<a>----]'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'{self.level} before call {func.__name__}')
            func_res = func(*args, **kwargs)
            print(f'{self.level} after call {func.__name__}')
            return func_res
        return wrapper


@add_tag
def add_tag1(tag='<button>'):
    print(tag)
    return 'ok1'


@param_add_tag(tag='[<a>]')
def add_tag2(tag='<button>'):
    print(tag)
    return 'ok2'


@ClassAddTag
def add_tag3(tag='<button>'):
    print(tag)
    return 'ok3'


@ClassAddTagParam()
def add_tag4(tag='<button>'):
    print(tag)
    return 'ok4'


if __name__ == '__main__':
    # decorator_say_hello()
    # decorator_say_hello_new()
    # log_say_hello()
    # log_say_hello_new()
    # say('i am saying i am ok')
    # say1('hah')
    # res = say2('hah')
    res = add_tag1('saying')
    print(res)
    res = add_tag2('saying')
    print(res)
    res = add_tag3('saying')
    print(res)
    res = add_tag4('saying')
    print(res)
