#from requestium import Session, Keys
import seleniumbase
import undetected_chromedriver as uc
import account_data
import actions
from requests import Session


def start():
        with seleniumbase.SB(demo=True, uc=True) as driver:

                print("start")
                s = Session()
                s.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1"
                 }
                account = account_data.Account()
                csrf = actions.get_csrf_token(s)
                actions.sign_up(s, account, csrf)
                actions.get_webapi_token(s, driver, account)

start()

