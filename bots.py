
import threading
import time
import json

f = open('inventory.dat', 'r')
inventory = json.load(f)
f.close()



print(type(inventory)) 
print(inventory)



def bot_fetcher(items, cart, lock):
   for item in items:
        time.sleep(inventory[item][1])
        with lock:
            cart.append([item, inventory[item][0]])

def bot_clerk(items):
    cart = []
    lock = threading.Lock()
    fetcher_lists = [[] for _ in range(3)]

    for i, item in enumerate(items):
        fetcher_lists[i % 3].append(item)

    threads = []
    for i, fetcher_list in enumerate(fetcher_lists, start=1):
        thread = threading.Thread(target=bot_fetcher, args=(fetcher_list, cart, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return cart




