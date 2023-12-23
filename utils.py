import requests
import os
from dotenv import load_dotenv


def get_input(day: int) -> str:
    load_dotenv()
    SESSION_ID = os.environ.get("SESSION_ID")
    headers = {"Cookie": f"session={SESSION_ID}"}
    r = requests.get(f"https://adventofcode.com/2023/day/{day}/input", headers=headers)
    return r.text
