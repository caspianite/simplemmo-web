import random

import actions, time, solve_captcha

def start(session, csrf, api_token):
    print("started looping travel steps")
    while True:
        step = actions.travel(session, csrf, api_token)
        try:

            print(f'taken step | gold: {(step["gold_amount"])} | exp: {str(step["exp_amount"])} | {step["text"]}')
            time.sleep(((step["wait_length"]) / 1000)) # + random.randint(1, 3) needs random delay to decrease captchas, removed for testing
        except:
            print("caught exception")
            if "i-am-not-a-bot" in step["text"]:
                solve_captcha.bruteforce(session)


