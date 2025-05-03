import csv
import logging
from datetime import datetime
from exporters import Exporter

logger = logging.getLogger(__name__)

class CSVExporter(Exporter):
    """Exports content to CSV format."""
    
    def export(self, content, output_path):
        """Export content to CSV file."""
        try:
            if not content:
                logger.warning("No content to export")
                return False
            
            # Determine all fields from all items
            all_fields = set()
            for item in content:
                all_fields.update(item.keys())
            
            # Sort fields to ensure consistent order
            fields = sorted(list(all_fields))
            
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                
                for item in content:
                    # Convert datetime objects to strings
                    row = {}
                    for key, value in item.items():
                        if isinstance(value, datetime):
                            row[key] = value.isoformat()
                        else:
                            row[key] = value
                    
                    writer.writerow(row)
            
            logger.info(f"Exported {len(content)} items to {output_path}")
            return True
        
        except Exception as e:
            logger.error(f"Error exporting to CSV: {e}")
            return False
