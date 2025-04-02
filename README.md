<div align="center">
  <h1>🕸️ Product URL Crawler</h1>
  <p><em>A high-performance, asynchronous web crawler for e-commerce product discovery</em></p>
  
  <p>
    <a href="#overview">Overview</a> •
    <a href="#features">Features</a> •
    <a href="#demo">Live Demo</a> •
    <a href="#installation">Installation</a> •
    <a href="#usage">Usage</a> •
    <a href="#architecture">Architecture</a> •
    <a href="#contributing">Contributing</a>
  </p>
  
  ![GitHub](https://img.shields.io/badge/python-3.8+-blue.svg)
  ![License](https://img.shields.io/badge/license-MIT-green)
  ![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
</div>

## 🔍 Overview

The **Product URL Crawler** is a robust, scalable, and asynchronous web crawler engineered specifically for e-commerce ecosystems. It systematically discovers and catalogs product URLs across multiple websites, handling complex site hierarchies with intelligent pattern recognition.

## ✨ Features

- **🔎 Smart URL Discovery** - Intelligently identifies product pages using advanced URL pattern matching
- **⚡ Asynchronous Architecture** - Leverages Python's `asyncio` and `aiohttp` for parallel execution
- **📊 Live Dashboard** - Real-time visualization of crawling progress with Streamlit
- **🛡️ Robust Error Handling** - Gracefully manages broken links, timeouts, and rate limiting
- **🔄 Adaptive Scaling** - Efficiently crawls from small boutiques to enterprise marketplaces

## 🖼️ Demo

### Live Dashboard
**Try it now:** [E-Commerce Crawler Dashboard](https://ecommerce-crawler-dashboard.streamlit.app/)

<div align="center">
  <h3>Streamlit Interactive Dashboard</h3>
  <img src="https://github.com/user-attachments/assets/50ce1e65-53a4-4dcc-9152-0b2935f6b49a" alt="Streamlit Dashboard" width="800"/>
  
  <img src="https://github.com/user-attachments/assets/8369a1c1-3b87-4988-b662-b0be87738ebc" alt="Architecture Diagram" width="800"/>
  
  <img src="https://github.com/user-attachments/assets/4b0c0464-abed-4963-a968-a8834057bc2b" alt="Crawler Process Flow" width="800"/>
</div>

## 🛠️ Requirements

```
Python 3.8+
aiohttp
beautifulsoup4
streamlit
lxml
selenium
pytest
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

# Set up the project
python setup.py install
```

## 🚀 Usage

### Running the Crawler

For command line:

```bash
python crawler/main.py
```

### Launching the Dashboard

For the Streamlit dashboard:

```bash
streamlit run streamlit_app.py
```

### Testing

To ensure everything is working as expected, run the tests using pytest:

```bash
pytest tests/
```

### Supported Domains

The crawler is pre-configured for these e-commerce sites:
- [virgio.com](https://www.virgio.com/)
- [westside.com](https://www.westside.com/)

Add your own domains by modifying the `DOMAINS` list in `crawler/main.py`.

### Output Format

Results are saved as structured JSON:

```json
{
    "https://www.virgio.com/": [
        "https://www.virgio.com/product/123",
        "https://www.virgio.com/item/456"
    ],
    "https://www.westside.com/": [
        "https://www.westside.com/products/789",
        "https://www.westside.com/catalog/101"
    ]
}
```

## 🏗️ Architecture

### Project Structure

```
product-url-crawler/
├── requirements.txt            # List of required libraries
├── setup.py                    # (Optional) Packaging script
├── streamlit_app.py            # Streamlit UI to run the crawler interactively
├── crawler/                    
│   ├── __init__.py             # Package initializer
│   ├── main.py                 # Orchestrates crawling for multiple domains
│   ├── async_crawler.py        # Contains asynchronous crawling and recursive logic
│   ├── parser.py               # Extracts product URLs and internal links with enhanced patterns
│   ├── utils.py                # Utility functions (e.g., URL normalization)
├── tests/                      
│   ├── __init__.py             # Tests package initializer
│   ├── test_crawler.py         # Unit tests for parser and utils functions
└── data/                       
    └── output.json             # (Generated) Output mapping domains to product URLs
```

### Key Components

#### 1. Async Crawler Engine
The heart of the system utilizes Python's asyncio for non-blocking I/O operations, allowing hundreds of concurrent connections while respecting robots.txt and rate limits.

#### 2. Intelligent Parser
Uses BeautifulSoup and custom heuristics to identify product URLs through pattern matching, handling diverse e-commerce platforms.

#### 3. Real-time Dashboard
Streamlit-powered interface providing live statistics, crawl depth visualization, and domain coverage metrics.

## 👥 Contributing

Developers are free to use this repository and make additional changes to improve it further. I welcome contributions of all kinds!

To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

Some ideas for improvements:
- Expanding the pattern recognition for more e-commerce platforms
- Adding export options for different formats (CSV, Excel, etc.)
- Implementing a proxy rotation system for larger scale crawling
- Enhancing the visualization with more detailed metrics

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [aiohttp](https://docs.aiohttp.org/) for asynchronous HTTP
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing
- [Streamlit](https://streamlit.io/) for the interactive dashboard

---

<div align="center">
  <p>Happy Crawling! 🚀</p>
  <p>
    <a href="mailto:zakeer1408@gmail.com">Contact</a>
  </p>
</div>
