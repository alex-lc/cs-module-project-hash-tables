# let's make a web client
# it will fetch URLs
# but it will cache the web page that's returned

# PLAN
# How to use hash tables to make a web cache?
# Key: URL
# Value: webpage data

# could make the value store more info
# webpage data
# when we looked it up

import urllib.request
import datetime
import time


class CacheEntry:
    def __init__(self, url, data):
        self.data = data
        self.url = url
        self.time_fetched = datetime.datetime.now().timestamp()


# EXECUTE
cache = {}

url = "https://www.google.com"

TIMEOUT = 10


def get_page(url):

    time_now = datetime.datetime.now().timestamp()

    # given a URL, check to see if it's in the cache
    if url in cache and time_now - cache[url].time_fetched < TIMEOUT:
        # if less than 10 second since our last request
        return cache[url]
    # if so, return that

    # if not, go get it
    else:
        print("going out into the webs to get the page")
        resp = urllib.request.urlopen(url)
        data = resp.read()
        resp.close()

        # put in cache
        cache[url] = CacheEntry(url, data)

    return cache[url]


page = get_page(url)
# print("After this, we get from cache")

print("now we wait")
time.sleep(10)
page = get_page(url)


# REVIEW
# we are caching like we want
# but, assumes page never changes
# and cache will get really large
