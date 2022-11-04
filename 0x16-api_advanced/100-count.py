#!/usr/bin/python3
"""
recursive
"""
import requests as r
from sys import argv


def count_words(subreddit, word_list, key=""):
    headers = {"User-Agent": "Frocuts"}
    endpoint = "http://reddit.com/r/{}/hot.json?after={}"
    subs = r.get(endpoint.format(subreddit, key), headers=headers)
    if subs.status_code != 200:
        print(None)
        return 0
    subs = subs.json()
    if subs["kind"] == "Listing":
        for word in word_list:
            print('{}: {}'.format(word, 0))
    else:
        print(None)
