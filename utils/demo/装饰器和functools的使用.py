# coding:utf-8
import functools

def login_required(func):
    @functools.wraps(func)  # 会把wrapper的所有信息__name__, __doc__ 之类全部恢复为func的信息
    def wrapper(*args, **kwargs):  # 因为装饰器会改变装饰函数的相关属性.
        pass
    print("func.__name__-----:", func.__name__)
    return wrapper

@login_required
def itcast():
    """
    装饰器的测试代码
    :return:
    """
    pass


# 使用__name__和__doc__来测试, 不加装饰器的时候显示 itcast的名字和doc
# print(itcast.__name__)
# print(itcast.__doc__)

# 使用__name__和__doc__来测试, 加装饰器的时候显示 login_required的wrapper的__name__和__doc__
print(itcast.__name__)
print(itcast.__doc__)

# 使用__name__和__doc__来测试, 使用了wrapper后, 再加上functools 又显示了itcast的__name__和__doc__
print(itcast.__name__)
print(itcast.__doc__)
