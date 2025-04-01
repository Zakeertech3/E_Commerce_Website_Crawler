import asyncio
import json
import logging
import os
import time

from crawler.async_crawler import create_session, crawl_recursive
from crawler.utils import normalize_url

logging.basicConfig(level=logging.INFO)

# List of domains to crawl
DOMAINS = [
    "https://www.virgio.com/",
    "https://www.westside.com/"
]

async def crawl_domain(domain):
    logging.info(f"Starting crawl for domain: {domain}")
    async with create_session() as session:
        try:
            # Start recursive crawling from the homepage with a maximum depth of 2
            visited, product_urls = await crawl_recursive(domain, domain, session, max_depth=2)
            # Normalize discovered URLs
            product_urls = [normalize_url(url, domain) for url in product_urls]
            product_urls = list(set(product_urls))  
            logging.info(f"Found {len(product_urls)} product URLs for domain: {domain}")
            return domain, product_urls
        except Exception as e:
            logging.error(f"Error crawling domain {domain}: {e}")
            return domain, []

async def run_crawler():
    tasks = [crawl_domain(domain) for domain in DOMAINS]
    for task in asyncio.as_completed(tasks):
        domain, urls = await task
        yield domain, urls

async def consume_crawler():
    """Consume the run_crawler generator and save results."""
    start_time = time.time()
    results = {}
    
    os.makedirs("data", exist_ok=True)
    with open("data/output.json", "w") as f:
        async for domain, urls in run_crawler():
            results[domain] = urls
            logging.info(f"Completed crawling {domain} in {time.time() - start_time:.2f} seconds")
            json.dump(results, f, indent=4)
    
    logging.info(f"Total crawling time: {time.time() - start_time:.2f} seconds")

def main():
    asyncio.run(consume_crawler())

if __name__ == "__main__":
    main()
