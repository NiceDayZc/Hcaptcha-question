from components.captcha import hCaptcha
from threading import Thread


def solve():
    captcha = hCaptcha.solve(
        sitekey='4c672d35-0701-42b2-88c3-78380b0db560',
        host='discord.com',
        proxies=True
    )

    print(captcha)

if (__name__ == '__main__'):
    for _ in range(100):
        Thread(target=solve).start()