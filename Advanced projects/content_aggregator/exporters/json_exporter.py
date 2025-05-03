import json
import logging
from datetime import datetime
from exporters import Exporter

logger = logging.getLogger(__name__)

class JSONExporter(Exporter):
    """Exports content to JSON format."""
    
    def export(self, content, output_path):
        """Export content to JSON file."""
        try:
            # Convert datetime objects to ISO format strings
            serializable_content = []
            for item in content:
                serializable_item = {}
                for key, value in item.items():
                    if isinstance(value, datetime):
                        serializable_item[key] = value.isoformat()
                    else:
                        serializable_item[key] = value
                serializable_content.append(serializable_item)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(serializable_content, f, indent=2, ensure_ascii=False)
            
            logger.info(f"Exported {len(content)} items to {output_path}")
            return True
        
        except Exception as e:
            logger.error(f"Error exporting to JSON: {e}")
            return False