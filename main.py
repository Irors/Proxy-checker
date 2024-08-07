from proxystr import Proxy, check_proxies
from other import *


def proxy_reader():
    with open('proxy.txt') as file:

        return [i.strip() for i in file]


def check_proxy(proxies):
    _proxies = []

    clear_file(path='result/good proxy.txt')
    clear_file(path='result/bad proxy.txt')

    for proxy in proxies:
        _proxies.append(Proxy(proxy))

    good_proxies, bad_proxies = check_proxies(proxies, with_info=True)

    for proxy in good_proxies:
        write_success(data=proxy[0])

    for proxy in bad_proxies:
        write_failer(data=proxy[0])

    print(f'count good proxies: {len(good_proxies)}')
    print(f'count bad proxies: {len(bad_proxies)}')


if __name__ == '__main__':
    proxys = proxy_reader()
    interface(_len=len(proxys))

    check_proxy(proxies=proxys)
