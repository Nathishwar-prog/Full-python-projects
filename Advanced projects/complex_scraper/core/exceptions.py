"""
Custom exceptions for the scraper.
"""

class ScraperException(Exception):
    """Base exception for scraper errors."""
    pass

class NetworkError(ScraperException):
    """Raised when there are network-related issues."""
    pass

class ParsingError(ScraperException):
    """Raised when there are issues parsing the response."""
    pass 