import requests
from fake_useragent import UserAgent

# 获取对应url的网页源代码
def get_page(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }
    return requests.get(url=url, headers=headers)


# 以下方法实现了将本机IP添加到白名单的操作
def get_MyIp():
    url = 'http://httpbin.org/ip'
    res = requests.get(url=url).json()
    #print(res['origin'])
    return res['origin']

def add_white_sheet(url):
    myip = get_MyIp()
    url = url.format(myip)
    requests.get(url=url)


if __name__ == '__main__':
    # get_page('http://www.baidu.com')
    # get_MyIp()
    jiguang = 'http://webapi.jghttp.alicloudecs.com/index/index/save_white?neek=38049&appkey=4c95266213e2a4f7e15b793816ed6da4&white={}'
    zhima = 'https://wapi.http.linkudp.com/index/index/save_white?neek=466922&appkey=3ed534835844f69a47f207e71113c9f4&white={}'
    add_white_sheet(zhima)
