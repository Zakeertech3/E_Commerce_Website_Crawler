from setuptools import setup, find_packages

setup(
    name="product_url_crawler",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "aiohttp",
        "streamlit",
        "lxml",
        "selenium"
    ],
    entry_points={
        'console_scripts': [
            'run_crawler=crawler.main:main',
        ],
    },
)
