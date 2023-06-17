from random import choice


def fetch_proxies():
    with open('./%s' % ('./proxies.txt'), 'r', encoding='utf-8') as proxies:
        proxies = choice(proxies.readlines()).replace('http://', '').strip()
    return {
        'http': 'http://%s' % (proxies),
        'https': 'http://%s' % (proxies)
    }