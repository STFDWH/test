from ProxyPool.utils import get_page, add_white_sheet

class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies


    def crawl_jiguang(self):
        """
        获取极光代理
        :return: 代理
        """
        white_sheet_url = 'http://webapi.jghttp.alicloudecs.com/index/index/save_white?neek=38049&appkey=4c95266213e2a4f7e15b793816ed6da4&white={}'
        api = 'http://d.jghttp.alicloudecs.com/getip?num=10&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='
        # 先将本机ip添加到白名单
        add_white_sheet(white_sheet_url)
        res = get_page(api).json()
        datas = res['data']
        for data in datas:
            ip, port = data['ip'], str(data['port'])
            #print('%s:%d' % (ip,port))
            yield ':'.join([ip, port])


    def crawl_zhima(self):
        """
        获取芝麻代理
        :return: 代理
        """
        white_sheet_url = 'https://wapi.http.linkudp.com/index/index/save_white?neek=466922&appkey=3ed534835844f69a47f207e71113c9f4&white={}'
        api = 'http://webapi.http.zhimacangku.com/getip?num=10&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='
        add_white_sheet(white_sheet_url)
        res = get_page(api).json()
        datas = res['data']
        for data in datas:
            ip, port = data['ip'], str(data['port'])
            #print('%s:%d' % (ip,port))
            yield ':'.join([ip, port])

if __name__ == '__main__':
    crawl = Crawler()
    crawl.crawl_jiguang()
    crawl.crawl_zhima()