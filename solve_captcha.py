import re, random, time, json
def bruteforce(session):
    timer_start = time.perf_counter()

    is_solved = False
    retries = 0
    while is_solved == False:
        captcha_page = (session.get('https://web.simple-mmo.com/i-am-not-a-bot', params={'new_page': 'true'}).content).decode("utf-8")
        time.sleep(0.5)
        captcha_IDs = re.findall("chooseItem\('(.*?)'", captcha_page)
        x_pos = random.randint(500, 600)
        y_pos = random.randint(300, 400)

        captcha_answer = json.loads((session.post("https://web.simple-mmo.com/api/bot-verification", data={
            "data": random.choice(captcha_IDs),
            "x": x_pos,
            "y": y_pos


        }).content).decode("utf-8"))

        if captcha_answer["type"] == "success":
            is_solved = True
            print(f"solved captcha in {str((time.perf_counter() - timer_start))} seconds, retries: " + str(retries))
        else:
            retries += 1
            #time.sleep(random.randint(3, 7))



