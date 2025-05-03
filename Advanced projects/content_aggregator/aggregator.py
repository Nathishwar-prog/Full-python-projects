import logging
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Import source modules
from sources.rss import RSSFetcher
from sources.news import NewsFetcher
from sources.reddit import RedditFetcher
from sources.twitter import TwitterFetcher

# Import exporters
from exporters.json_exporter import JSONExporter
from exporters.csv_exporter import CSVExporter

logger = logging.getLogger(__name__)

class ContentAggregator:
    """Core class for aggregating content from multiple sources."""
    
    def __init__(self, config):
        """Initialize the aggregator with configuration."""
        self.config = config
        self.sources = []
        self._initialize_sources()
        self.exporters = {
            'json': JSONExporter(),
            'csv': CSVExporter()
        }
    
    def _initialize_sources(self):
        """Initialize content sources based on configuration."""
        if 'rss' in self.config:
            self.sources.append(RSSFetcher(self.config['rss']))
        
        if 'news' in self.config:
            self.sources.append(NewsFetcher(self.config['news']))
        
        if 'reddit' in self.config:
            self.sources.append(RedditFetcher(self.config['reddit']))
        
        if 'twitter' in self.config:
            self.sources.append(TwitterFetcher(self.config['twitter']))
    
    def fetch_all(self):
        """Fetch content from all sources in parallel."""
        all_content = []
        
        with ThreadPoolExecutor(max_workers=len(self.sources)) as executor:
            future_to_source = {executor.submit(source.fetch): source for source in self.sources}
            
            for future in future_to_source:
                source = future_to_source[future]
                try:
                    content = future.result()
                    logger.info(f"Fetched {len(content)} items from {source.__class__.__name__}")
                    all_content.extend(content)
                except Exception as e:
                    logger.error(f"Error fetching from {source.__class__.__name__}: {e}")
        
        # Sort by date (newest first)
        all_content.sort(key=lambda x: x.get('published_at', datetime.min), reverse=True)
        
        return all_content
    
    def filter_by_keywords(self, content, keywords):
        """Filter content based on keywords."""
        filtered = []
        for item in content:
            # Check if any keyword appears in title or description
            title = item.get('title', '').lower()
            description = item.get('description', '').lower()
            
            if any(keyword.lower() in title or keyword.lower() in description 
                   for keyword in keywords):
                filtered.append(item)
        
        logger.info(f"Filtered {len(filtered)} items out of {len(content)}")
        return filtered
    
    def export(self, content, format_type, output_path):
        """Export content using the appropriate exporter."""
        if format_type in self.exporters:
            try:
                self.exporters[format_type].export(content, output_path)
                logger.info(f"Content exported to {output_path}")
                return True
            except Exception as e:
                logger.error(f"Error exporting content: {e}")
                return False
        else:
            logger.error(f"Unsupported export format: {format_type}")
            return False
