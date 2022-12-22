import requests
import random
import time

chars = "AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn123456790"

while True:
    gid = "".join(random.choices(chars, k=16))
    req = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{gid}")

    print(f"gift id: {gid}, status code: {req.status_code}")

    if req.status_code == 429:
        time.sleep(65)

    if req.status_code == 200:
        gifts = open("gifts.txt", "a")
        gift.write(gifs.read().join(f"\nhttps://discord.gift/{gid}"))
