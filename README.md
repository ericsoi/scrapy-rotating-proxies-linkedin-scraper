# LinkedIn Profile Scraper using Scrapy and Scrapy Rotating Proxies

![Scrapy Logo](https://th.bing.com/th/id/R.046a54a1580183dc0922655b300a8a4d?rik=KeNQmuu3KzXsbQ&pid=ImgRaw&r=0)

This project demonstrates how to scrape LinkedIn profiles using Scrapy and Scrapy Rotating Proxies. Scrapy is a powerful web crawling and scraping framework, and Scrapy Rotating Proxies allows us to easily rotate IP addresses and avoid IP blocking during scraping

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Overview

Web scraping is an essential technique for extracting data from websites, but it often requires rotating IP addresses to avoid getting blocked by websites. Scrapy-Rotating-Proxies is an extension for Scrapy that enables you to seamlessly switch between different proxies while scraping.

This project provides a basic example of setting up a Scrapy spider with rotating proxies, helping you get started with your own web scraping tasks.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/scrapy-rotating-proxies-linkedin-scraper.git
   cd scrapy-rotating-proxies-linkedin-scraper
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## Usage

1. Modify the spiders/linkedinspider.py file to define your scraping logic.

2. Configure your proxies and settings in the settings.py file under ROTATING_PROXY_LIST.

3. Run the Scrapy spider:
    ```bash
    scrapy crawl linkedinspider
    ```
4. Add the list of profiles to crawl in the spider ``linkedin/spiders/linkedinspider.py`` under ``profile_list = ['linkedin_user-1', 'linkedin_user-2', 'linkedin_user-n']``

## Configuration

In the settings.py file, you can customize various settings:
- ROTATING_PROXY_LIST: List of proxy URLs to rotate.
- Other Scrapy settings: User-Agent, download delay, etc.

Refer to the Scrapy documentation and Scrapy-Rotating-Proxies documentation for more configuration options.
