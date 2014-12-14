#!/usr/bin/env python
import sys
import json
import argparse
import requests
import pprint

from IPython import embed as qq


try:
    from apikey import API
except ImportError:
    API = input('Please provide your API key ')
    


def parse_arguments():
    parser = argparse.ArgumentParser(description="Mailinator inbox checker")
    parser.add_argument('inbox', nargs=1, help='The inbox that you want to check')
    return parser.parse_args()

def check_inbox(inbox_page):
    return inbox_page['messages']

def get_inbox(inbox):
    return requests.get('https://api.mailinator.com/api/inbox?to={inbox}&token={api}'.format(
        inbox=inbox,
        api=API)).json()

def start_daemon():
    ...

def main():
    args = parse_arguments() 
    start_daemon()
    inbox_page = get_inbox(args.inbox[0])
    emails = check_inbox(inbox_page)

if __name__ == '__main__':
    main()
