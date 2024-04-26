#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using urllib package."""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(type(content), content, content.decode('utf-8')))
