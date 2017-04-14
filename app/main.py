#!/usr/bin/env python3
import requests
from logging import getLogger, StreamHandler, DEBUG


# Setting of logging function
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)


def main(argv):
    url = 'http://challenge-server.code-check.io/api/hash'

    try:
        query = {"q": argv[0]}
    except NameError:
        logger.debug("parameter is not exist.")
    r = requests.get(url, params=query).json()
    print(r["hash"])
