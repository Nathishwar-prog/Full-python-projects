import logging
import feedparser
from datetime import datetime
from sources import ContentSource

logger = logging.getLogger(__name__)

class RSSFetcher(ContentSource):
    """Fetches content from RSS feeds."""
    
    def fetch(self):
        """Fetch content from all configured RSS feeds."""
        all_items = []
        
        for feed_config in self.config.get('feeds', []):
            try:
                feed_url = feed_config['url']
                logger.info(f"Fetching RSS feed: {feed_url}")
                
                feed = feedparser.parse(feed_url)
                source_name = feed_config.get('name') or feed.feed.get('title', feed_url)
                
                for entry in feed.entries[:feed_config.get('max_items', 10)]:
                    published_at = None
                    
                    # Try different date fields that might be available
                    date_fields = ['published_parsed', 'updated_parsed', 'created_parsed']
                    for field in date_fields:
                        if hasattr(entry, field) and getattr(entry, field):
                            published_at = datetime(*getattr(entry, field)[:6])
                            break
                    
                    # If no date fields are available, use current time
                    if not published_at:
                        published_at = datetime.now()
                    
                    item = {
                        'title': entry.get('title', 'No title'),
                        'description': entry.get('summary', entry.get('description', '')),
                        'url': entry.get('link', ''),
                        'published_at': published_at,
                        'source': source_name,
                        'source_type': 'rss'
                    }
                    
                    all_items.append(item)
            
            except Exception as e:
                logger.error(f"Error fetching RSS feed {feed_config.get('url')}: {e}")
        
        return all_items