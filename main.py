#from requestium import Session, Keys
import seleniumbase
import undetected_chromedriver as uc
import account_data
import actions
from requests import Session
import time
import loop_travel

def start():
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

        with seleniumbase.SB(demo=False, uc=True, test=True, rtf=True, headless=False, proxy="socks5://167.172.178.242:59166") as driver:

                print("start")
                account = account_data.Account()
                actions.browser_sign_up(driver, account)
                time.sleep(2)
                csrf_token = actions.get_csrf_token(driver)
                api_token = actions.get_webapi_token(driver)
                print(csrf_token)
                print(api_token)
                for cookie in driver.driver.get_cookies():
                        c = {cookie['name']: cookie['value']}
                        s.cookies.update(c)
                # open("accounts.txt", "a").write(f'{account.email}:{account.password}:{csrf_token}:{api_token}\n')
                # loop_travel.start(s, csrf_token, api_token)
                # time.sleep(1000)


        open("accounts.txt", "a").write(f'{account.email}:{account.password}:{csrf_token}:{api_token}\n')
        loop_travel.start(s, csrf_token, api_token)




                # time.sleep(9999)
                # time.sleep(100)
                # csrf = actions.get_csrf_token(s)
                # actions.sign_up(s, account, csrf)
                # actions.get_webapi_token(s, driver, account)

start()
print()

