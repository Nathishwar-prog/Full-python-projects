from abc import ABC, abstractmethod

class Exporter(ABC):
    """Abstract base class for content exporters."""
    
    @abstractmethod
    def export(self, content, output_path):
        """Export content to the specified output path."""
        pass
