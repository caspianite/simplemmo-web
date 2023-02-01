import random

import actions, time

def start(session, csrf, api_token):
    print("started looping travel steps")
    while True:
        step = actions.travel(session, csrf, api_token)
        try:

            print(f'taken step | gold: {(step["gold_amount"])} | exp: {str(step["exp_amount"])} | {step["text"]}')
            time.sleep(((step["wait_length"]) / 1000) + random.randint(5, 15))
        except:
            print("exception")
            print(step)
            time.sleep(1000)

