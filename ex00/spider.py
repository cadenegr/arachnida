# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    _spider.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cadenegr <neo_dgri@hotmail.com>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/20 11:11:11 by cadenegr          #+#    #+#              #
#    Updated: 2024/11/20 13:34:19 by cadenegr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
from bs4 import BeautifulSoup
import os
import argparse
from urllib.parse import urljoin


EXT = [".jpg", ".jpeg", ".gif", ".png", ".bmp"]


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/",
    "Upgrade-Insecure-Requests": "1",
}

def extract_depth(url, save_path, depth, visited):
    if depth < 1 or url in visited:
        return  # Stop if max depth is reached or URL is already visited.

    visited.add(url)
    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()

        if not resp.content.strip():
            print(f"Empty content for {url}")
            return

        soup = BeautifulSoup(resp.content, "html.parser")
        if not soup.find():
            print(f"Failed to parse HTML for {url}")
            return

        # First, download images on the current page
        extract_images(url, save_path)

        # Process links for deeper exploration
        links = soup.find_all("a", href=True)
        print(f"Total links on {url}: {len(links)}")

        for link in links:
            next_url = link.get("href", "")
            if next_url.startswith("//"):
                next_url = "https:" + next_url
            elif next_url.startswith("/"):
                next_url = urljoin(url, next_url)
            elif not next_url.startswith(("http:", "https:")):
                continue

            if next_url not in visited:
                extract_depth(next_url, save_path, depth - 1, visited)
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")


def extract_images(url, save_path):
    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()

        if not resp.content.strip():
            print(f"Empty content for {url}")
            return

        soup = BeautifulSoup(resp.content, "html.parser")
        if not soup.find():
            print(f"Failed to parse for {url}")
            return

        img_tags = soup.find_all("img")
        print(f"Total image tags on {url}: {len(img_tags)}")
        for img in img_tags:
            img_url = img.get("src")
            if not img_url:
                continue
            if img_url.startswith("//"):
                img_url = "https:" + img_url
            elif img_url.startswith("/"):
                img_url = urljoin(url, img_url)

            if not img_url.lower().endswith(tuple(EXT)):
                continue
            img_name = os.path.basename(img_url)
            if not img_name or img_name == "/":
                print(f"Skipping invalid image URL: {img_url}")
                continue
            img_path = os.path.join(save_path, img_name)

            try:
                img_resp = requests.get(img_url, headers=headers)
                img_resp.raise_for_status()

                with open(img_path, "wb") as image:
                    image.write(img_resp.content)
                print(f"Downloaded: {img_path}")
            except Exception as e:
                print(f"Failed to download: {img_path}: {e}")
    except Exception as e:
        print(f"Failed to fetch images from {url}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Spider - Download images script.")
    parser.add_argument("url", help="URL to extract from.")
    parser.add_argument("-r", action="store_true", help="Recursive link exploration.")
    parser.add_argument("-l", type=int, default=5, help="Depth of exploration.")
    parser.add_argument("-p", type=str, default="./spider", help="Path for downloads.")

    args = parser.parse_args()
    os.makedirs(args.p, exist_ok=True)

    visited = set()
    depth = args.l if args.r else 1
    extract_depth(args.url, args.p, depth, visited)


if __name__ == "__main__":
    main()
