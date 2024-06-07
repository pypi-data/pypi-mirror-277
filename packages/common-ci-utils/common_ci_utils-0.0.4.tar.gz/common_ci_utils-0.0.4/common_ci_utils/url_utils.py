"""
This module purpose is to hold all utils functions for URL requests.
"""

import requests

from common_ci_utils.exceptions import WrongResponseError


def get_html_content(url, username=None, password=None):
    auth = None
    if username and password:
        auth = (username, password)
    # Fetch the HTML content with authentication
    response = requests.get(url, auth=auth)

    # Check if the request was successful
    if response.status_code == 200:
        return response.text
    else:
        raise WrongResponseError(
            f"Status code is {response.status_code} when trying to get {url} content!"
        )
