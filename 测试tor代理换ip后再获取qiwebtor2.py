#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import requests
import requesocks

url = 'https://api.ipify.org?format=json'


def getip_requests(url):
    print "(+) Sending request with plain requests..."
    r = requests.get(url)
    print "(+) IP is: " + r.text.replace("\n", "")


def getip_requesocks(url):
    print "(+) Sending request with requesocks..."
    session = requesocks.session()
    session.proxies = {'http': 'socks5://14.63.227.176:9050',
                       'https': 'socks5://14.63.227.176:9050'}
    r = session.get(url)
    print "(+) IP is: " + r.text.replace("\n", "")


def main():
    print "Running tests..."
    getip_requests(url)
    getip_requesocks(url)
    os.system("""(echo authenticate '"mypassword"'; echo signal newnym; echo quit) | nc localhost 9051""")
    getip_requesocks(url)


if __name__ == "__main__":
    main()
