import logging
import requests
from datetime import datetime
from sources import ContentSource

logger = logging.getLogger(__name__)

class NewsFetcher(ContentSource):
    """Fetches content from news APIs."""
    
    def fetch(self):
        """Fetch content from news APIs."""
        all_items = []
        
        # For NewsAPI.org
        if 'newsapi' in self.config:
            try:
                api_key = self.config['newsapi'].get('api_key')
                if not api_key:
                    logger.error("NewsAPI API key not provided")
                    return all_items
                
                categories = self.config['newsapi'].get('categories', ['general'])
                for category in categories:
                    logger.info(f"Fetching news for category: {category}")
                    url = f"https://newsapi.org/v2/top-headlines"
                    params = {
                        'apiKey': api_key,
                        'category': category,
                        'language': self.config['newsapi'].get('language', 'en'),
                        'pageSize': self.config['newsapi'].get('max_items', 10)
                    }
                    
                    response = requests.get(url, params=params)
                    if response.status_code == 200:
                        news_data = response.json()
                        
                        for article in news_data.get('articles', []):
                            published_at = None
                            if article.get('publishedAt'):
                                try:
                                    published_at = datetime.fromisoformat(article['publishedAt'].replace('Z', '+00:00'))
                                except ValueError:
                                    published_at = datetime.now()
                            else:
                                published_at = datetime.now()
                            
                            item = {
                                'title': article.get('title', 'No title'),
                                'description': article.get('description', ''),
                                'url': article.get('url', ''),
                                'published_at': published_at,
                                'source': article.get('source', {}).get('name', 'NewsAPI'),
                                'source_type': 'news'
                            }
                            
                            all_items.append(item)
                    else:
                        logger.error(f"NewsAPI error: {response.status_code} - {response.text}")
            
            except Exception as e:
                logger.error(f"Error fetching from NewsAPI: {e}")
        
        return all_items
