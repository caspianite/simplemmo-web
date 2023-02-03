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


def get_csrf_token(browser): #csrf-token, global token
    page = browser.driver.page_source
    csrf_token = bs(page, features="html.parser").find("meta", attrs={"name":"csrf-token"})["content"]
    #global_token = re.search(r"var token = (.*?);", str(bs(page, features="html.parser").find_all("script"))).group(0).split('"')[1]
    return csrf_token

def get_webapi_token(browser):
    html = browser.driver.page_source
    return re.search("api_token=(.*)';}", html).group(1)



def sign_up(s, account_data, csrf_token):

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

    s.get("https://web.simple-mmo.com/register")
    register = s.post("https://web.simple-mmo.com/register", headers= {'referrer': 'https://web.simple-mmo.com/register',
    'Origin': 'https://web.simple-mmo.com'}, data=data, allow_redirects=True)
    print(register.status_code)
    print(data)

    if register.status_code == 200:
        return True

# def log_in(session, account_data, csrf_token):
#
#     data = {
#     '_token': csrf_token,
#     'email': account_data.email,
#     'password': account_data.password,
#     }
#     login = session.post("https://web.simple-mmo.com/login", data=data, allow_redirects=True)




# def send_session(session, csrf_token):
#     #hash = parse_int_as_basestr((int(str(random.random())[2:])/20), 20)
#     session.cookies.set("d_h", "true")
#
#     fp = ''.join(random.choice('0123456789abcdef') for i in range(32))
#
#
#     headers= {'referrer': 'https://web.simple-mmo.com/home',
#     'Origin': 'https://web.simple-mmo.com'}
#
#     session.post('https://web.simple-mmo.com/fp', data={'_token': csrf_token, 'fp': fp}, headers=headers)
#     session.post("https://web.simple-mmo.com/api/session-hash", data={}, headers=headers)
#
#
# def update_session_cookies(session):
#     """
#     "function setCookie(cname,cvalue,exdays){var d=new Date();d.setTime(d.getTime()+(exdays*24*60*60*1000));var expires=\"expires=\"+d.toUTCString();document.cookie=cname+\"=\"+cvalue+\";\"+expires+\";path=/\";}"
#     """
#
#     epoch_with_expiry = ((datetime.datetime.now(datetime.timezone.utc) - datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)) / datetime.timedelta(seconds=1)) + 0.005*24*60*60 #js epoch time with simplemmo expiry
#
#     expiry = datetime.date.strftime(datetime.datetime.utcfromtimestamp(epoch_with_expiry), '%Y-%m-%dT%H:%M:%SZ')
#
#     csrf_token = session.cookies.get_dict()["XSRF-TOKEN"]
#     laravel_token = session.cookies.get_dict()["laravelsession"]
#
#     print(expiry)
#
#     #set cookies here
#
#     # for cookie in session.cookies:
#     #     print(cookie.name)
#     #     if cookie.name == "laravelsession":
#     #         cookie.rest = {'expires': expiry}
#     #     if cookie.name == "XSRF-TOKEN":
#     #         cookie.rest = {'expires': expiry}



def browser_sign_up(browser, account_data):
    browser.open("https://web.simple-mmo.com/register")
    time.sleep(5) # while testing if cf catches the browser
    browser.send_keys('//*[@id="name"]', account_data.username)
    browser.send_keys('//*[@id="email"]', account_data.email)
    browser.send_keys('//*[@id="password"]', account_data.password)
    browser.send_keys('//*[@id="password_confirmation"]', account_data.password)
    browser.click(f'/html/body/div/div[2]/div/form/div[6]/div[{str(random.randint(1,9))}]')
    browser.click("/html/body/div/div[2]/div/form/div[7]/button")
    browser.click("/html/body/div/div[2]/div/form/div[8]/button")
    browser.click("/html/body/div/div[2]/div/form/div[10]/button")
    time.sleep(2)
    browser.open("https://web.simple-mmo.com/home")


def travel(s, csrf, api_token):
    dh = random.randint(500, 800)
    response = s.post('https://api.simple-mmo.com/api/travel/perform/f4gl4l3k', data={
    '_token': csrf,
    'api_token': api_token,
    'd_1': dh,
    'd_2': (dh - random.randint(150, 250)),
    's': 'false',
    'travel_id': '0',
    }
    )
    travel_info = json.loads((response.content).decode("utf-8"))

    return travel_info
    # {'text': 'Welcome to SimpleMMO. This game is incredibly simple. Every time you take a step, you will embark on a small adventure that will be displayed in just a few sentences.', 'resultText': '', 'rewardType': 'none', 'rewardAmount': 0, 'level': 1, 'wait_length': 2813, 'userAmount': '293', 'step_type': 'text', 'heading': 'You take a step...', 'gold_amount': 0, 'exp_amount': 0, 'action': False, 'buttons': False, 'guild_raid_exp': False, 'exp_percentage': 0, 'currentEXP': 0, 'currentGold': 500, 'sprint_expiry': 0, 'travel_background': '/img/bg/6.png', 'modifiers': {'gold_modifiers': [{'amount': 0, 'reason': []}], 'exp_modifiers': [{'amount': 0, 'reason': []}], 'droprate_modifiers': [{'amount': 0, 'reason': []}], 'stepping_modifiers': [{'amount': 0, 'reason': []}]}}



def wave(s, csrf, user_id):
    wave = s.post(f"https://web.simple-mmo.com/api/wave/{str(user_id)}", json={ # bool needs encoding
        "_token": csrf,
        "data": True
    })

    print(f"waving user id {str(user_id)}")
    print(wave.content)


def enum_inventory(s):
    print("enumerating inventory items")
    enumeration_complete = False
    page = 1
    items = []
    items_value_gold = 0
    while enumeration_complete == False:

        inventory = (s.get(f"https://web.simple-mmo.com/inventory?page={str(page)}").content).decode("utf-8")
        items_retrieved = []

        for i in re.finditer("quickSellItem\((.*?)\);", inventory):
            item_string = i.split(",")
            id = int(item_string[0])
            name = item_string[1]
            value = int(item_string[2])
            quantity = int(item_string[4])
            items_retrieved.append({
                "id": id, "name": name, "value": value, "quantity": quantity
            })
            items_value_gold += quantity

        if len(items_retrieved) == 0:
            enumeration_complete = True
            break

        items.append(items_retrieved)
        page += 1
        time.sleep(1)

    print(f"enumerated inventory worth {str(items_value_gold)} gold")


def quicksell_items(s, csrf, items_dict_list):
    for item in items_dict_list:
        sale = (s.post(f"https://web.simple-mmo.com/api/quicksell/{str(item['id'])}/quantity", body={
            "token": csrf, "data": str(item["quantity"])
        }).content).decode("utf-8")

        print(sale)


def travel_sprint_loop(s):
    time.sleep(60)
    while True:

        sprint = s.post('https://web.simple-mmo.com/api/travel/sprint', data={
        'minutes': '4'

        })
        print("sprinted travel")
        time.sleep(300)



