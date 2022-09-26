#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the body of the response"""

if __name__ == "__main__":
    import requests
    from sys import argv
    
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
