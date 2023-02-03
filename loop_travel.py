import random

import actions, time, solve_captcha, re, threading, travel_auxiliary

def start(session, csrf, api_token):
    print("started looping travel steps")
    i = 0
    threading.Thread(target=travel_auxiliary.start_autosell, args=(session, csrf,)).start()
    threading.Thread(target=actions.travel_sprint_loop, args=(session,)).start()
    threading.Thread(target=actions.switch_best_town_loop, args=(session, csrf,)).start()
    while True:
        step = actions.travel(session, csrf, api_token)
        i += 1

        try:

            print(f'taken step ({str(i)}) | gold: {(step["gold_amount"])} | exp: {str(step["exp_amount"])} | {step["text"]}')
            time.sleep(((step["wait_length"]) / 1000)) # + random.randint(1, 3) needs random delay to decrease captchas, removed for testing
            if "waveToUser" in step["text"]:
                id = re.findall("waveToUser\((.*?),'", step["text"])[0]
                actions.wave(session, csrf, id)
        except:
            print("caught exception")
            if "i-am-not-a-bot" in step["text"]:
                solve_captcha.bruteforce(session)



