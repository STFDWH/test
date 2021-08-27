
class PoolEmptyError(Exception):
    def __str__(self):
        return "proxies pool is empty"

if __name__ == '__main__':
    try:
        raise PoolEmptyError
    except PoolEmptyError as err:
        print("error: {}".format(err))