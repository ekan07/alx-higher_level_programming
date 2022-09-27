#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    req = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print(' '*4+'- type: {}'.format(type(req.text)))
    print(' '*4+'- content: {}'.format(req.text))
