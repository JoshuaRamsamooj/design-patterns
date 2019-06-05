def wrap(pre, post):
    def decorate(func):
        def call(*args, **kwargs):
            pre(func, *args, **kwargs)
            try:
                result = func(*args, **kwargs)
                return result
            except:
                raise
            finally:
                post(func, *args, **kwargs)

        return call

    return decorate


def trace_in(func, *args, **kwargs):
    print("Entering function", func.__name__)


def trace_out(func, *args, **kwargs):
    print("Leaving function", func.__name__)


@wrap(trace_in, trace_out)
def calc(x, y):
    # invoke error for testing
    # x = 1/0
    return x + y


if __name__ == '__main__':
    try:
        calc(1, 0)
    except Exception as e:
        print(e)
