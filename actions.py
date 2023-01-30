import requests
from bs4 import BeautifulSoup as bs
import re
import random
import json
import datetime
import time
#from requests_html import HTMLSession



def parse_int_as_basestr(n: int , base: int):
    convertString = "0123456789abcdef"
    if n < base:
        return convertString[n]
    else:
        return parse_int_as_basestr(n//base,base) + convertString[n%base]


def get_csrf_token(session): #csrf-token, global token
    page = session.get("https://web.simple-mmo.com/").content
    csrf_token = bs(page, features="html.parser").find("meta", attrs={"name":"csrf-token"})["content"]
    #global_token = re.search(r"var token = (.*?);", str(bs(page, features="html.parser").find_all("script"))).group(0).split('"')[1]
    return csrf_token

def get_webapi_token(session, browser, account_data):
    browser.open("https://simple-mmo.com/home")
    browser.driver.delete_all_cookies()
    browser.send_keys("input#email", account_data.email)
    browser.type("input#password", account_data.email)
    browser.click("(//button)[1]")
    time.sleep(2000)



def sign_up(session, account_data, csrf_token):

    data = {
    '_token': csrf_token,
    'name': account_data.username,
    'email': account_data.email,
    'password': account_data.password,
    'password_confirmation': account_data.password,
    'avatar': random.choice(["1", "5", "35", "3", "4", "20", "26"]),
    'tos': 'true',
    'privacy': 'true',
    'contact_email': '',
}

    session.get("https://web.simple-mmo.com/register")
    register = session.post("https://web.simple-mmo.com/register", headers= {'referrer': 'https://web.simple-mmo.com/register',
    'Origin': 'https://web.simple-mmo.com'}, data=data, allow_redirects=True)
    print(register.status_code)
    print(data)

    if register.status_code == 200:
        return True

def log_in(session, account_data, csrf_token):

    data = {
    '_token': csrf_token,
    'email': account_data.email,
    'password': account_data.password,
    }
    login = session.post("https://web.simple-mmo.com/login", data=data, allow_redirects=True)




def send_session(session, csrf_token):
    #hash = parse_int_as_basestr((int(str(random.random())[2:])/20), 20)
    session.cookies.set("d_h", "true")

    fp = ''.join(random.choice('0123456789abcdef') for i in range(32))


    headers= {'referrer': 'https://web.simple-mmo.com/home',
    'Origin': 'https://web.simple-mmo.com'}

    session.post('https://web.simple-mmo.com/fp', data={'_token': csrf_token, 'fp': fp}, headers=headers)
    session.post("https://web.simple-mmo.com/api/session-hash", data={}, headers=headers)


def update_session_cookies(session):
    """
    "function setCookie(cname,cvalue,exdays){var d=new Date();d.setTime(d.getTime()+(exdays*24*60*60*1000));var expires=\"expires=\"+d.toUTCString();document.cookie=cname+\"=\"+cvalue+\";\"+expires+\";path=/\";}" 
    """

    epoch_with_expiry = ((datetime.datetime.now(datetime.timezone.utc) - datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)) / datetime.timedelta(seconds=1)) + 0.005*24*60*60 #js epoch time with simplemmo expiry

    expiry = datetime.date.strftime(datetime.datetime.utcfromtimestamp(epoch_with_expiry), '%Y-%m-%dT%H:%M:%SZ')

    csrf_token = session.cookies.get_dict()["XSRF-TOKEN"]
    laravel_token = session.cookies.get_dict()["laravelsession"]

    print(expiry)

    #set cookies here

    # for cookie in session.cookies:
    #     print(cookie.name)
    #     if cookie.name == "laravelsession":
    #         cookie.rest = {'expires': expiry}
    #     if cookie.name == "XSRF-TOKEN":
    #         cookie.rest = {'expires': expiry}


    