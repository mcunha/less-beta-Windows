#!/usr/bin/env python3

r"""
shared.py
-John Taylor
May-14-2020

Functions shared between build.py and version_compare.py
"""

import re
import time
import urllib.request

LESSURL = "http://greenwoodsoftware.com/less/download.html"
version_beta_url_re = re.compile(r"""Download <strong>BETA</strong> version (.*?) """, re.M | re.S | re.I)
version_recommended_url_re = re.compile(r"""Download <strong>RECOMMENDED</strong> version (.*?) """, re.M | re.S | re.I)
NEWFILE = "new.txt"


def download_less_web_page() -> str:
    """Download LESSURL and save the contents to fname

    Returns:
        An in-memory version of the downloaded web page
    """

    fname = "download.html"
    try:
        urllib.request.urlretrieve(LESSURL, fname)
        time.sleep(1)
    except:
        return False

    try:
        with open(fname) as fp:
            page = fp.read()
    except:
        return False

    return page


def get_latest_recommended_version_url(page: str) -> tuple:
    """Return the URL for the "RECOMMENDED version"

    Args:
        page: an HTML web page, provided in LESSURL

    Returns:
        A tuple containing: (version number, zip archive URL)
        Ex: 551, http://greenwoodsoftware.com/less/less-551.zip
    """

    match = version_recommended_url_re.findall(page)
    if not len(match):
        return (None, None)

    version = match[0]
    archive = "less-%s.zip" % version
    url = LESSURL.replace("download.html", archive)
    return version, url


def get_latest_beta_version_url(page: str) -> tuple:
    """Return the URL for the "BETA version"

    Args:
        page: an HTML web page, provided in LESSURL

    Returns:
        A tuple containing: (version number, zip archive URL)
        Ex: 551, http://greenwoodsoftware.com/less/less-551.zip
    """

    match = version_beta_url_re.findall(page)
    if not len(match):
        return (None, None)

    version = match[0]
    archive = "less-%s-beta.zip" % version
    url = LESSURL.replace("download.html", archive)
    return version, url
