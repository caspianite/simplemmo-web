import threading, actions, random, time
def start_autosell(s, csrf):
    time.sleep(150)
    while True:
        item_list = actions.enum_inventory(s)
        actions.quicksell_items(s, csrf, item_list)
        time.sleep(random.randint(1500, 1700))

