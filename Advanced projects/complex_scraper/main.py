"""
Main entry point for the complex scraper.
"""

import json
import os
from core.scraper import Scraper
from storage.database import DatabaseStorage
from storage.file_storage import FileStorage
from captcha.solver import CaptchaSolver

def load_config():
    """Load configuration from config.json."""
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.json')
    with open(config_path, 'r') as f:
        return json.load(f)

def main():
    # Load configuration
    config = load_config()
    
    # Initialize components
    scraper = Scraper(config['scraper'])
    db_storage = DatabaseStorage(config['storage']['database']['connection_string'])
    file_storage = FileStorage(config['storage']['file']['base_path'])
    captcha_solver = CaptchaSolver(config['captcha']['api_key'])
    
    # Example usage
    url = "https://example.com"
    try:
        # Scrape the website
        data = scraper.scrape(url)
        
        # Save to database
        db_storage.save(data)
        
        # Save to file
        file_storage.save(data, 'scraped_data.json')
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main() 