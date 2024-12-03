import requests
from dotenv import load_dotenv
import os

load_dotenv()


def get_input(day: int) -> str:
    cookie = os.environ["COOKIE"]
    url = f"https://adventofcode.com/2024/day/{day}/input"

    r = requests.get(url, cookies={"session": cookie})
    return r
