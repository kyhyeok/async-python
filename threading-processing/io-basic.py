import requests
import time
import os
import threading


def fetcher(session, url):
    print(f"f{os.getpid()} process | {threading.get_ident()} url: {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com/"] * 50

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 9초
