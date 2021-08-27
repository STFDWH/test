MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = '8.130.167.87'
REDIS_PORT = 6379
REDIS_PASSWORD = 'foobared'
REDIS_KEY = 'proxies'

import redis
from random import choice
from ProxyPool.MyExceptionError import PoolEmptyError


class RedisClient(object):
    def __init__(self):
        self.db = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0, password=REDIS_PASSWORD)

    def add(self, proxy, score=INITIAL_SCORE):
        """
        添加新代理
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        """
        # 若该代理分数为0，则为新获取到的代理，需将其加入有序代理集合proxies中
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, {proxy:score})

    def random(self):
        """
        随机获取有效代理，首先尝试获取最高分数代理，如果最高分数不存在，则按照排名获取，否则异常
        :return: 随机代理
        """
        # 获取所有可用代理（分数为100的）
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            # 代理按分数从大到小排序,取排名前100个
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError

    def decrease(self, proxy):
        """
        代理值减1分，若分数等于最小值，则删除代理
        :param proxy: 代理
        :return: 修改后的代理分数
        """
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减1')
            return self.db.zincrby(REDIS_KEY, -1, proxy)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
        """
        判断当前代理是否存在
        :param proxy: 代理
        :return: 是否存在
        """
        return not self.db.zscore(REDIS_KEY, proxy)==None

    def max(self, proxy):
        """
        将当前代理分数设置为 MAX_SCORE
        :param proxy: 代理
        :return: 设置结果
        """
        return self.db.zadd(REDIS_KEY, {proxy:MAX_SCORE})

    def count(self):
        """
        获取代理池中的总代理个数
        :return: 代理数量
        """
        return self.db.zcard(REDIS_KEY)

    def all(self):
        """
        获取代理池中的全部代理
        :return: 全部代理
        """
        return self.db.zrange(REDIS_KEY, 0, -1) # self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

if __name__ == '__main__':
    redisdb = RedisClient()
    print(redisdb.all())
    # print(redisdb.max('ip1'))
    print(redisdb.count())
    # print(redisdb.add('ip5', 40))
    # print(redisdb.exists('ip1'))
    print(redisdb.random())
    # print(redisdb.decrease('ip6'))
