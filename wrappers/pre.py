def wrap(pre):
    def decorate(func):
        def call(*args, **kwargs):
            pre()
            result = func(*args, **kwargs, k=6)
            return result
        return call
    return decorate


def pre_func(*args, **kwargs):
    print('Do something before wrapped function')


@wrap(pre_func)
def div(x, y, **kwargs):
    print('Other Kwargs:', kwargs)
    try:
        return x/y
    except:
        return False


if __name__ == '__main__':
    result = div(10, 2)
    print(result)