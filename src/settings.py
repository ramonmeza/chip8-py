import json5

from pathlib import Path
from typing import Any, Optional


class Settings:
    
    @staticmethod
    def load(path: Path, section: Optional[str] = None) -> Any:
        '''Loads a settings JSON file.'''
        with open(path, 'r') as fp:
            js: dict = dict(json5.load(fp))
        
        if section in js.keys():
            return js[section]
        
        return js
