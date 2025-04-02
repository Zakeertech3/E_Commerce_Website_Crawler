<div align="center">
  <h1>🕸️ Product URL Crawler</h1>
  <p><em>Efficient, Async Web Crawler for E-Commerce Product Discovery</em></p>

  <p>
    <a href="#overview">Overview</a> •
    <a href="#features">Features</a> •
    <a href="#demo">Demo</a> •
    <a href="#installation">Installation</a> •
    <a href="#usage">Usage</a> •
    <a href="#architecture">Architecture</a> •
    <a href="#license">License</a>
  </p>

  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/tests-passing-brightgreen" alt="Tests">
</div>

## 🔍 Overview

**Product URL Crawler** is a lightweight, high-performance, asynchronous crawler tailored for e-commerce platforms. It discovers and extracts product page URLs by traversing internal site links, enabling automated product listing discovery at scale.

## ✨ Features

- **Smart Product Detection**: Identifies product URLs using intelligent pattern matching.
- **Asynchronous Crawling**: Built on `asyncio` and `aiohttp` for fast, non-blocking crawling.
- **Streamlit Dashboard**: Visualize crawling progress and results interactively.
- **Robust Handling**: Manages redirects, broken links, and timeouts gracefully.
- **Scalable Architecture**: Efficiently handles both small and large e-commerce domains.

## 🖼️ Demo

**Live Dashboard:** [ecommerce-crawler-dashboard.streamlit.app](https://ecommerce-crawler-dashboard.streamlit.app)

![Streamlit Dashboard Screenshot](https://github.com/user-attachments/assets/50ce1e65-53a4-4dcc-9152-0b2935f6b49a)

## 🛠️ Requirements

```bash
Python 3.8+
aiohttp
beautifulsoup4
streamlit
lxml
requests
cachetools==5.3.1
```

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Zakeertech3/E_Commerce_Website_Crawler.git
cd E_Commerce_Website_Crawler

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage

### Run from Command Line

```bash
python crawler/main.py
```

### Launch Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

### Output Format

Crawled data is saved to `data/output.json` as:

```json
{
  "https://www.virgio.com/": [
    "https://www.virgio.com/products/example-product"
  ],
  "https://www.westside.com/": [
    "https://www.westside.com/collections/item-name"
  ]
}
```

## 🏗️ Architecture

```
product-url-crawler/
├── requirements.txt
├── streamlit_app.py
├── crawler/
│   ├── main.py
│   ├── async_crawler.py
│   ├── parser.py
│   ├── utils.py
├── data/
│   └── output.json
├── tests/
│   └── test_crawler.py
```

- **main.py**: Initializes and coordinates the crawling workflow
- **async_crawler.py**: Implements the async crawling engine
- **parser.py**: Contains logic for link and product extraction
- **streamlit_app.py**: Frontend dashboard for real-time crawl monitoring

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<div align="center">
  <p>Crafted with 💡 by <a href="https://github.com/Zakeertech3">Zakeertech3</a></p>
</div>

