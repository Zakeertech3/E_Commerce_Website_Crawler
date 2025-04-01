import pytest
from crawler.parser import extract_product_urls, extract_internal_links
from crawler.utils import normalize_url

def test_extract_product_urls():
    html = '''
    <html>
      <body>
        <a href="/products/123">Product 123</a>
        <a href="/item/456">Product 456</a>
        <a href="/non-product/">Not a Product</a>
      </body>
    </html>
    '''
    base_url = "https://example.com/"
    result = extract_product_urls(html, base_url)
    assert any("products/123" in url for url in result)
    assert any("item/456" in url for url in result)
    assert not any("non-product" in url for url in result)

def test_normalize_url():
    base_url = "https://example.com/"
    relative_url = "/product/123"
    full_url = normalize_url(relative_url, base_url)
    assert full_url == "https://example.com/product/123"
