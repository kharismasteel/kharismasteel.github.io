#!/usr/bin/env python3
"""
Scrape product pages from bintangpasundan.com to collect product image URLs.

It finds product links on the product listing page and for each product extracts
the `og:image` meta or the first product thumbnail image. Writes mapping to
`_data/product_images.yml` as `slug: url`.

Run: python3 scripts/scrape_bintang_images.py
"""
import sys
from pathlib import Path
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import yaml

BASE = Path(__file__).resolve().parents[1]
DATA_FILE = BASE / '_data' / 'product_images.yml'

START_URLS = [
    'https://www.bintangpasundan.com/home-produk/',
    'https://www.bintangpasundan.com/',
]

HEADERS = {'User-Agent': 'kharismasteel-scraper/1.0 (+https://kharismasteel.github.io)'}

def get_soup(url):
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    return BeautifulSoup(r.text, 'html.parser')

def gather_product_links():
    links = set()
    for url in START_URLS:
        try:
            soup = get_soup(url)
        except Exception as e:
            print('Failed to fetch', url, e)
            continue
        for a in soup.find_all('a', href=True):
            href = a['href']
            if '/product/' in href or '/produk/' in href:
                full = urljoin(url, href)
                links.add(full)
    return sorted(links)

def extract_image_from_product(url):
    try:
        soup = get_soup(url)
    except Exception as e:
        print('Error fetching product', url, e)
        return None
    # Try og:image
    og = soup.find('meta', property='og:image')
    if og and og.get('content'):
        return urljoin(url, og['content'].strip())
    # Try first product image
    img = soup.find('img')
    if img and img.get('src'):
        return urljoin(url, img['src'].strip())
    return None

def slug_from_url(url):
    path = urlparse(url).path.rstrip('/')
    if not path:
        return None
    return Path(path).name

def main():
    try:
        import bs4
    except Exception:
        print('BeautifulSoup not installed. Run: pip install requests beautifulsoup4 pyyaml')
        sys.exit(2)
    links = gather_product_links()
    print(f'Found {len(links)} candidate product links')
    mapping = {}
    for l in links:
        slug = slug_from_url(l)
        if not slug:
            continue
        img = extract_image_from_product(l)
        if img:
            mapping[slug] = img
            print('OK', slug, img)
        else:
            print('No image for', slug)

    # Merge with existing data
    if DATA_FILE.exists():
        try:
            existing = yaml.safe_load(DATA_FILE.read_text()) or {}
        except Exception:
            existing = {}
    else:
        existing = {}
    existing.update(mapping)
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(yaml.dump(existing, sort_keys=True, allow_unicode=True))
    print('Wrote', DATA_FILE)

if __name__ == '__main__':
    main()
