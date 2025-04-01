from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def extract_product_urls(html, base_url):
    """
    Extracts product URLs from HTML content using a set of regex patterns.
    Enhanced to include '/products/' and other common segments.
    """
    soup = BeautifulSoup(html, "lxml")
    product_urls = set()
    patterns = [
        r"/product/",
        r"/products/",
        r"/item/",
        r"/p/",
        r"/shop/",
        r"/sku/",
        r"/catalog/"  # Added for Westside-specific URLs
    ]
    for a in soup.find_all("a", href=True):
        href = a['href']
        for pattern in patterns:
            if re.search(pattern, href, re.IGNORECASE):
                product_urls.add(urljoin(base_url, href))
                break
    return list(product_urls)

def extract_internal_links(html, base_url):
    """
    Extracts internal links from HTML content.
    """
    soup = BeautifulSoup(html, "lxml")
    internal_links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/"):
            internal_links.add(urljoin(base_url, href))
        elif base_url in href:
            internal_links.add(href)
    return list(internal_links)
