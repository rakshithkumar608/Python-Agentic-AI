from time import time
import requests
import threading
import time

def download_image(url, name):
    print(f"Startign Download from {url}")
    resp = requests.get(url)
    print(f"Download completed from {url}, size: {len(resp.content)} bytes")
    
urls = [
    "https://www.python.org/static/community_logos/python-logo.png",
    "https://www.python.org/static/community_logos/python-powered-h-140x182.png",
    "https://www.python.org/static/community_logos/python-powered-w-100x40.png"
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download_image, args=(url, ))
    t.start()
    threads.append(t)
    
for t in threads:
    t.join()


ems = time.time()

print(f"Total time taken to download : {ems - start: .2f} seconds")