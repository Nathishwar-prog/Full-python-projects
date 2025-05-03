"""
File storage functionality.
"""

import json
import os

class FileStorage:
    def __init__(self, base_path):
        self.base_path = base_path
        
    def save(self, data, filename):
        """
        Save data to a file.
        
        Args:
            data (dict): Data to save
            filename (str): Name of the file
        """
        filepath = os.path.join(self.base_path, filename)
        with open(filepath, 'w') as f:
            json.dump(data, f)
            
    def load(self, filename):
        """
        Load data from a file.
        
        Args:
            filename (str): Name of the file
            
        Returns:
            dict: Loaded data
        """
        filepath = os.path.join(self.base_path, filename)
        with open(filepath, 'r') as f:
            return json.load(f) 