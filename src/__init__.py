"""
src - The Updating Package

This package automates portfolio updates, including data extraction, screenshot generation, 
and content updates.

Available modules:
- installer: Installs required Python packages and Playwright.
- update-data: Extracts portfolio data from README.md and saves it as data/portfolio.json.
- update-ss: Captures and updates website screenshots based on portfolio data.
- update-site: Updates the website content using portfolio.json data and screenshots from 
               update-ss.
- utils: Provides helper functions for JSON operations.
"""

VERSION = "0.0.1"
AUTHOR = "Odhy Pradhana"
