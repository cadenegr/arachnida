#!/usr/bin/env python3
"""
Arachnida - Web Scraping and Image Metadata Analysis Suite

A comprehensive toolkit for intelligent web crawling and EXIF metadata extraction.
"""

from setuptools import setup, find_packages

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="arachnida",
    version="1.0.0",
    author="cadenegr",
    author_email="cadenegr@student.42.fr",
    description="Web scraping and image metadata analysis toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cadenegr/arachnida",
    py_modules=["spider", "scorpion"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "spider=spider:main",
            "scorpion=scorpion:main",
        ],
    },
    keywords="web-scraping image-processing metadata exif crawler",
    project_urls={
        "Bug Reports": "https://github.com/cadenegr/arachnida/issues",
        "Source": "https://github.com/cadenegr/arachnida",
        "Documentation": "https://github.com/cadenegr/arachnida#readme",
    },
)