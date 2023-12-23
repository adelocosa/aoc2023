import requests
import os
from dotenv import load_dotenv


def get_input(day: int) -> list[str]:
    if os.path.isfile("cache"):
        with open("cache", "r") as cache:
            cache_day = cache.readline()
            if day == int(cache_day):
                return cache.read().splitlines()

    load_dotenv()
    SESSION_ID = os.environ.get("SESSION_ID")
    headers = {"Cookie": f"session={SESSION_ID}"}
    r = requests.get(f"https://adventofcode.com/2023/day/{day}/input", headers=headers)
    with open("cache", "w") as cache:
        cache.write(f"{day}\n")
        cache.write(r.text)
    return r.text.split("\n")[:-1]
