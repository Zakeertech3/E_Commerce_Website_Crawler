import aiohttp
import asyncio
import logging
from asyncio import Semaphore
from cachetools import TTLCache
import time

logging.basicConfig(level=logging.DEBUG)

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/115.0 Safari/537.36")
}

RATE_LIMIT = Semaphore(10)  # Maximum concurrent requests
URL_CACHE = TTLCache(maxsize=1000, ttl=3600)  # Cache URLs for 1 hour

def create_session():
    """Creates and returns an aiohttp ClientSession with custom headers."""
    return aiohttp.ClientSession(headers=HEADERS)

async def fetch_html_with_session(url, session):
    """Fetch HTML content with rate limiting and caching, skipping on first failure."""
    if url in URL_CACHE:
        return URL_CACHE[url]
    
    async with RATE_LIMIT:
        try:
            async with session.get(url, timeout=10) as response:
                logging.debug(f"Fetching URL: {url}")
                if response.status == 200:
                    text = await response.text()
                    URL_CACHE[url] = text
                    logging.debug(f"Response status: {response.status} for {url}")
                    return text
                else:
                    logging.error(f"Failed to fetch {url}, status: {response.status}")
        except Exception as e:
            logging.error(f"Error fetching {url}: {e}")
        logging.warning(f"Skipping URL: {url}")
        return None

async def crawl_recursive(url, domain, session, max_depth=2, visited=None, product_urls=None):
    """Optimized recursive crawler with concurrent processing."""
    if visited is None:
        visited = set()
    if product_urls is None:
        product_urls = set()

    if url in visited or len(visited) > 1000:
        return visited, product_urls
    
    visited.add(url)
    html = await fetch_html_with_session(url, session)
    
    if html:
        from crawler.parser import extract_product_urls, extract_internal_links
        found_products = extract_product_urls(html, domain)
        product_urls.update(found_products)
        
        if max_depth > 0:
            internal_links = extract_internal_links(html, domain)
            tasks = []
            for link in internal_links:
                if link not in visited:
                    tasks.append(crawl_recursive(link, domain, session, max_depth - 1, visited, product_urls))
            if tasks:
                await asyncio.gather(*tasks)
    
    return visited, product_urls
