def wrap(pre, post):
    def decorate(func):
        def call(*args, **kwargs):
            pre(func, *args, **kwargs)
            result = func(*args, **kwargs, k=6)
            post(func, *args, **kwargs)
            return result
        return call
    return decorate


def trace_in(func, *args, **kwargs):
    print("Entering function", func.__name__)


def trace_out(func, *args, **kwargs):
    print("Leaving function", func.__name__)


@wrap(trace_in, trace_out)
def div(x, y, **kwargs):
    print('Other Kwargs:', kwargs)
    try:
        return x/y
    except:
        return False


if __name__ == '__main__':
    result = div(10, 2)
    print(result)