import argparse
import json
import logging
from aggregator import ContentAggregator

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_config(config_file):
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading config file: {e}")
        return None

def main():
    """Main entry point for the content aggregator."""
    parser = argparse.ArgumentParser(description='Content Aggregator')
    parser.add_argument('--config', type=str, default='config.json',
                        help='Path to configuration file')
    parser.add_argument('--export', type=str, choices=['json', 'csv'],
                        help='Export format')
    parser.add_argument('--output', type=str, help='Output file path')
    parser.add_argument('--web', action='store_true',
                        help='Start web interface')
    parser.add_argument('--keywords', type=str, nargs='+',
                        help='Keywords to filter content')
    
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    if not config:
        logger.error("Failed to load configuration. Exiting.")
        return
    
    # Create aggregator
    aggregator = ContentAggregator(config)
    
    # Fetch content
    logger.info("Fetching content...")
    content = aggregator.fetch_all()
    
    # Filter content if keywords provided
    if args.keywords:
        logger.info(f"Filtering content with keywords: {args.keywords}")
        content = aggregator.filter_by_keywords(content, args.keywords)
    
    # Export content if requested
    if args.export:
        if not args.output:
            args.output = f"content.{args.export}"
        
        logger.info(f"Exporting content to {args.output}")
        aggregator.export(content, args.export, args.output)
    
    # Start web interface if requested
    if args.web:
        logger.info("Starting web interface...")
        from web.app import start_app
        start_app(content)
    else:
        # Print summary to console
        logger.info(f"Aggregated {len(content)} items")
        for i, item in enumerate(content[:5], 1):
            logger.info(f"{i}. {item['title']} - {item['source']}")
        
        if len(content) > 5:
            logger.info(f"... and {len(content) - 5} more items")

if __name__ == "__main__":
    main()