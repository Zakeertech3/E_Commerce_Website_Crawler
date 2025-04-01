from urllib.parse import urljoin

def normalize_url(url, base_url):
    """
    Converts a relative URL to an absolute URL based on the provided base_url.
    """
    return urljoin(base_url, url)
