"""
Tests for the scraper functionality.
"""

import unittest
from core.scraper import Scraper

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.config = {
            "timeout": 30,
            "retry_attempts": 3
        }
        self.scraper = Scraper(self.config)
        
    def test_scrape_valid_url(self):
        """Test scraping a valid URL."""
        url = "https://example.com"
        result = self.scraper.scrape(url)
        self.assertIsNotNone(result)
        
    def test_scrape_invalid_url(self):
        """Test scraping an invalid URL."""
        url = "invalid-url"
        with self.assertRaises(Exception):
            self.scraper.scrape(url) 