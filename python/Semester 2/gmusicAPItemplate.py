#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "gmusicAPItemplate.py", "14/07/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print authorship_string,

from gmusicapi import Mobileclient

api = Mobileclient()

logged_in = api.login('lorryarmstrong@gmail.com', '', '38DA130100EA7920')

print logged_in

api.logout()