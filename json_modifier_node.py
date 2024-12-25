import json
from typing import Union, Any

class JSONModifierNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_input": ("STRING", {"multiline": True}),
                "path": ("STRING", {"default": ""}),
                "new_value": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("modified_json",)
    FUNCTION = "modify_json"
    CATEGORY = "utils"

    def modify_json(self, json_input: str, path: str, new_value: str) -> tuple[str]:
        try:
            data = json.loads(json_input)
            try:
                new_val = json.loads(new_value)
            except json.JSONDecodeError:
                new_val = new_value
                
            if not path:
                return (json.dumps(new_val, indent=2),)
                
            self._set_by_path(data, path, new_val)
            return (json.dumps(data, indent=2),)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON input")

    def _set_by_path(self, data: Any, path: str, value: Any) -> None:
        keys = path.split('.')
        current = data
        
        for i, key in enumerate(keys[:-1]):
            if key.isdigit():
                key = int(key)
            elif '[' in key and ']' in key:
                list_key, index = key[:-1].split('[')
                current = current[list_key][int(index)]
                continue
                
            if key not in current:
                raise ValueError(f"Path {'.'.join(keys[:i+1])} does not exist")
            current = current[key]
            
        last_key = keys[-1]
        if last_key.isdigit():
            last_key = int(last_key)
        elif '[' in last_key and ']' in last_key:
            list_key, index = last_key[:-1].split('[')
            current[list_key][int(index)] = value
            return
            
        current[last_key] = value 