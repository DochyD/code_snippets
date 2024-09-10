"""Utils module for paths."""
import os

def get_project_dir():
    """Get project directory."""
    return os.path.dirname(os.path.abspath(__file__))
