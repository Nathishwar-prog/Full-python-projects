# Content Aggregator

**Developed by: Nathishwar**

A powerful Python application for aggregating content from multiple sources including RSS feeds, news websites, Reddit, and Twitter/X.

## Features

- **Multi-source Content Aggregation**
  - RSS feeds
  - News websites (via NewsAPI)
  - Reddit subreddits
  - Twitter/X searches

- **Smart Content Processing**
  - Parallel fetching from all sources
  - Keyword-based filtering
  - Chronological sorting
  - Flexible export options (JSON, CSV)

- **User-friendly Web Interface**
  - Clean, responsive design
  - Content filtering by source type and keywords
  - Pagination for browsing large datasets
  - Direct links to original content

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nathishwar/content-aggregator.git
   cd content-aggregator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a configuration file:
   - Copy `config.json.example` to `config.json`
   - Add your API keys for NewsAPI and Twitter
   - Customize your content sources

## Usage

### Command Line Usage

**Basic usage:**
```bash
python main.py --config config.json
```

**Start web interface:**
```bash
python main.py --config config.json --web
```

**Export content to JSON:**
```bash
python main.py --config config.json --export json --output content.json
```

**Export content to CSV:**
```bash
python main.py --config config.json --export csv --output content.csv
```

**Filter by keywords:**
```bash
python main.py --config config.json --keywords python programming
```

### Configuration

Create a `config.json` file with your preferred sources:

```json
{
  "rss": {
    "feeds": [
      {
        "name": "BBC News",
        "url": "http://feeds.bbci.co.uk/news/rss.xml",
        "max_items": 10
      },
      {
        "name": "Tech Crunch",
        "url": "https://techcrunch.com/feed/",
        "max_items": 10
      }
    ]
  },
  "news": {
    "newsapi": {
      "api_key": "your_newsapi_key_here",
      "categories": ["technology", "business"],
      "language": "en",
      "max_items": 10
    }
  },
  "reddit": {
    "subreddits": [
      {
        "name": "programming",
        "category": "hot",
        "max_items": 10
      }
    ]
  },
  "twitter": {
    "bearer_token": "your_twitter_bearer_token_here",
    "searches": [
      {
        "query": "python programming",
        "max_items": 10
      }
    ]
  }
}
```

## Project Structure

```
content_aggregator/
├── __init__.py
├── main.py               # Entry point
├── aggregator.py         # Core functionality
├── sources/              # Source-specific modules
│   ├── __init__.py
│   ├── rss.py
│   ├── news.py
│   ├── reddit.py
│   └── twitter.py
├── exporters/            # Export functionality
│   ├── __init__.py
│   ├── json_exporter.py
│   └── csv_exporter.py
├── web/                  # Web interface
│   ├── __init__.py
│   ├── app.py
│   └── templates/
│       └── index.html
└── requirements.txt
```

## API Keys

You'll need the following API keys:
- **NewsAPI**: Get from [newsapi.org](https://newsapi.org/)
- **Twitter/X**: Get a Bearer Token from the [Twitter Developer Portal](https://developer.twitter.com/)

## Extending the Application

This application is designed to be easily extended:

1. **Add New Content Sources**:
   - Create a new class in the `sources` directory that inherits from `ContentSource`
   - Implement the `fetch()` method to retrieve content

2. **Create New Export Formats**:
   - Add a new class in the `exporters` directory that inherits from `Exporter`
   - Implement the `export()` method for your format

3. **Enhance the Web Interface**:
   - Modify templates in the `web/templates` directory
   - Add new routes in `web/app.py`

## License

MIT License

## Contact

For questions, suggestions, or contributions, please contact:
- Nathishwar
- GitHub: [github.com/Nathishwar](https://github.com/Nathishwar-prog)

---

© 2025 Nathishwar. All rights reserved.
