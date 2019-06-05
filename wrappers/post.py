def wrap(post):
    def decorate(func):
        def call(*args, **kwargs):
            result = func(*args, **kwargs, k=6)
            post()
            return result
        return call
    return decorate


def post_func(*args, **kwargs):
    print('Do something after wrapped function')


@wrap(post_func)
def div(x, y, **kwargs):
    print('Other Kwargs:', kwargs)
    try:
        return x/y
    except:
        return False


if __name__ == '__main__':
    result = div(10, 2)
    print(result)