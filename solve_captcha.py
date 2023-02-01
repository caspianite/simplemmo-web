def bruteforce(session):
    is_solved = False
    while is_solved == False:
        captcha_page = session.get('https://web.simple-mmo.com/i-am-not-a-bot', params={'new_page': 'true'})
        captcha_IDs = "s" #finish
