import json
from typing import Union

class SimpleJSONParserNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_string": ("STRING", {"multiline": True}),
                "path": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "INT",)
    RETURN_NAMES = ("parsed_data", "array_size",)
    FUNCTION = "parse_json"
    CATEGORY = "utils"

    def parse_json(self, json_string: str, path: str) -> tuple[str, int]:
        try:
            data = json.loads(json_string)
            if not path:
                array_size = len(data) if isinstance(data, list) else -1
                return json.dumps(data, indent=2), array_size
            
            keys = path.split('.')
            for key in keys:
                if key.isdigit():
                    data = data[int(key)]
                elif '[' in key and ']' in key:
                    list_key, index = key[:-1].split('[')
                    data = data[list_key][int(index)]
                else:
                    data = data[key]
            
            array_size = len(data) if isinstance(data, list) else -1
            
            if isinstance(data, (dict, list)):
                return json.dumps(data, indent=2), array_size
            else:
                return str(data), array_size
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON string")
        except (KeyError, IndexError, TypeError):
            raise ValueError("Invalid path or key not found")

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")


