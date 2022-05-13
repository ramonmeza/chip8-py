import json5

from pathlib import Path
from typing import Any, Dict, Optional


class Settings:
    
    # methods
    @staticmethod
    def load(path: Path, section: Optional[str] = None) -> Dict[str, Any]:
        '''Loads a settings JSON file.'''
        with open(path, 'r') as fp:
            js: dict = dict(json5.load(fp))
        
        if section in js.keys():
            return js[section]
        
        return js
