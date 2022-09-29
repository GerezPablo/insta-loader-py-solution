import re


def handle_url(url):
    result = re.search(
        "https://www\.instagram\.com/p/(?P<short_code>[A-Za-z0-9\-\_]*)/$", url)

    return result.group(1)
