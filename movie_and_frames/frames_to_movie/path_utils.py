"""Utils module for paths."""
import os

def get_project_dir():
    """Get project directory."""
    return os.path.abspath(os.curdir)
