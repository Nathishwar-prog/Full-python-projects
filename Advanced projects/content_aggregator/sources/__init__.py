
from abc import ABC, abstractmethod

class ContentSource(ABC):
    """Abstract base class for content sources."""
    
    def __init__(self, config):
        """Initialize the source with configuration."""
        self.config = config
    
    @abstractmethod
    def fetch(self):
        """Fetch content from the source."""
        pass