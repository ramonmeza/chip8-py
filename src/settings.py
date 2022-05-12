import json

from pathlib import Path
from typing import Optional


class Settings:
    
    @staticmethod
    def load(path: Path, section: Optional[str] = None) -> dict:
        '''Loads a settings JSON file.'''
        with open(path, 'r') as fp:
            js: dict = dict(json.load(fp))
        
        if section in js.keys():
            return dict(js[section])
        
        return js
