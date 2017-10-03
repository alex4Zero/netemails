from __future__ import print_function
import urllib2, sys
from HTMLParser import HTMLParser
import time
import random

class GithubHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        attr = dict(attrs)
        if "github" not in attr['href'] and "login" not in attr['href'] and "search" not in attr['href']:
            f = open('accounts.txt', 'a')
            f.write(attr['href'] + '\n')
            f.close()


def extract():
    for x in range(1, 83):
        url = 'https://github.com/search?l=&p=' + str(x) + '&q=language%3AC%23+location%3AMoscow&ref=advsearch&type=Users'

        try:
            f = urllib2.urlopen(url)
            html = f.read()
            f.close()
        except urllib2.HTTPError as e:
            print(e, 'while fetching', url)
            return

        parser = GithubHTMLParser()
        parser.feed(html)
        print(str(x))



extract()