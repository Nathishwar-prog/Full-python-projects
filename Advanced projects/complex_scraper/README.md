# Complex Scraper
# Developed by : Nathishwar
A powerful and flexible web scraping framework with support for handling complex scenarios including CAPTCHA solving, data storage, and more.

## Features

- Modular architecture for easy extension
- Built-in CAPTCHA solving support
- Multiple storage backends (Database and File)
- Configurable scraping behavior
- Comprehensive test suite

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Nathishwar-prog/complex-scraper.git
cd complex-scraper
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage example:

```python
from core.scraper import Scraper
from config.config import load_config

# Load configuration
config = load_config()

# Initialize scraper
scraper = Scraper(config)

# Start scraping
results = scraper.scrape("https://example.com")
```

## Configuration

Edit `config/config.json` to customize the scraper behavior:

- Timeout settings
- Retry attempts
- User agent
- Storage settings
- CAPTCHA service configuration

## Testing

Run the test suite:

```bash
pytest tests/
```

## License

MIT License

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request 