# LinkCrawler
A LinkCrawler is a Python module that takes a url on the web (ex: http://python.org), fetches the web-page corresponding to that url, and parses all the links on that page into a repository of links. Next, it fetches the contents of any of the url from the repository just created, parses the links from this new content into the repository and continues this process for all links in the repository until stopped or after a given number of links are fetched.

Requirements
============

* Python 3.5+
* Works on Linux, Windows, Mac OSX, BSD

# Install

The quick way::

    pip install dist/LinkCrawler-1.0.0-py2.py3-none-any.whl

# Logs
```bash
 ~user/.crawler/
 ```
 # Usage 
 
```python
from crawler import Crawler
with Crawler("https://www.python.org", output_path= "D://links.txt",LOG=Crawler.INFO_LOG) as crawler:
     crawler.crawl()
     
with Crawler("https://www.python.org", output_path= "D://links.txt",LOG=Crawler.INFO_LOG) as crawler:
     for links in crawler.crawl_next():
          print(links)
          
with Crawler("https://www.python.org", output_path= "D://links.txt",LOG=Crawler.DEBUG_LOG) as crawler:
     crawler.crawl(1000)
```