
import logging
import requests
from datetime import datetime
from sources import ContentSource

logger = logging.getLogger(__name__)

class TwitterFetcher(ContentSource):
    """Fetches content from Twitter/X API."""
    
    def fetch(self):
        """Fetch content from Twitter/X API."""
        all_items = []
        
        try:
            if not self.config.get('bearer_token'):
                logger.error("Twitter/X API bearer token not provided")
                return all_items
            
            headers = {
                'Authorization': f"Bearer {self.config['bearer_token']}",
                'User-Agent': 'ContentAggregator/1.0'
            }
            
            # Fetch tweets from search queries
            for query_config in self.config.get('searches', []):
                query = query_config['query']
                max_items = query_config.get('max_items', 10)
                
                logger.info(f"Searching Twitter/X for: {query}")
                
                # Using Twitter API v2
                url = "https://api.twitter.com/2/tweets/search/recent"
                params = {
                    'query': query,
                    'max_results': max_items,
                    'tweet.fields': 'created_at,author_id,public_metrics'
                }
                
                response = requests.get(url, headers=headers, params=params)
                if response.status_code == 200:
                    data = response.json()
                    
                    for tweet in data.get('data', []):
                        try:
                            published_at = datetime.fromisoformat(tweet['created_at'].replace('Z', '+00:00'))
                        except (ValueError, KeyError):
                            published_at = datetime.now()
                        
                        item = {
                            'title': tweet.get('text', '')[:50] + '...',
                            'description': tweet.get('text', ''),
                            'url': f"https://twitter.com/i/web/status/{tweet['id']}",
                            'published_at': published_at,
                            'source': 'Twitter/X',
                            'source_type': 'twitter',
                            'tweet_id': tweet.get('id'),
                            'author_id': tweet.get('author_id'),
                            'likes': tweet.get('public_metrics', {}).get('like_count', 0),
                            'retweets': tweet.get('public_metrics', {}).get('retweet_count', 0)
                        }
                        
                        all_items.append(item)
                else:
                    logger.error(f"Twitter/X API error: {response.status_code} - {response.text}")
        
        except Exception as e:
            logger.error(f"Error fetching from Twitter/X: {e}")
        
        return all_items
