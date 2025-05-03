import logging
import requests
from datetime import datetime
from sources import ContentSource

logger = logging.getLogger(__name__)

class RedditFetcher(ContentSource):
    """Fetches content from Reddit."""
    
    def fetch(self):
        """Fetch content from Reddit subreddits."""
        all_items = []
        
        for subreddit_config in self.config.get('subreddits', []):
            try:
                subreddit = subreddit_config['name']
                category = subreddit_config.get('category', 'hot')
                max_items = subreddit_config.get('max_items', 10)
                
                logger.info(f"Fetching from r/{subreddit}, category: {category}")
                
                url = f"https://www.reddit.com/r/{subreddit}/{category}.json"
                headers = {'User-Agent': 'ContentAggregator/1.0'}
                
                response = requests.get(url, headers=headers, params={'limit': max_items})
                if response.status_code == 200:
                    data = response.json()
                    
                    for post in data['data']['children']:
                        post_data = post['data']
                        
                        published_at = datetime.fromtimestamp(post_data['created_utc'])
                        
                        item = {
                            'title': post_data.get('title', 'No title'),
                            'description': post_data.get('selftext', '')[:500],
                            'url': f"https://www.reddit.com{post_data['permalink']}",
                            'published_at': published_at,
                            'source': f"r/{subreddit}",
                            'source_type': 'reddit',
                            'score': post_data.get('score', 0),
                            'comments': post_data.get('num_comments', 0)
                        }
                        
                        all_items.append(item)
                else:
                    logger.error(f"Reddit API error: {response.status_code} - {response.text}")
            
            except Exception as e:
                logger.error(f"Error fetching from Reddit r/{subreddit_config.get('name')}: {e}")
        
        return all_items
