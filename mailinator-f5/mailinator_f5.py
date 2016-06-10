#!/usr/bin/env python3
#encoding: utf-8

import time
import argparse
import requests

try:
    from apikey import API
except ImportError:
    API = input('Please provide your API key ')


CHECKING_FREQ = 30

def parse_arguments():
    parser = argparse.ArgumentParser(description="Mailinator inbox checker")
    parser.add_argument('inbox', nargs=1, help='The inbox that you want to check')
    return parser.parse_args()


def is_new(emails):
    return next((email for email in emails
                 if email['seconds_ago'] <= CHECKING_FREQ),
                False)


def check_inbox(inbox):
    inbox_page = get_inbox(inbox)
    return inbox_page['messages']


def wait_email(inbox):
    while 1:
        emails = check_inbox(inbox)
        if is_new(emails):
            print('New email on {}'.format(time.ctime()))
        time.sleep(CHECKING_FREQ)


def get_inbox(inbox):
    return requests.get('https://api.mailinator.com/api/inbox?'
                        'to={inbox}&token={api}'.format(
                            inbox=inbox,
                            api=API)).json()


def main():
    args = parse_arguments()
    wait_email(args.inbox[0])

if __name__ == '__main__':
    main()
