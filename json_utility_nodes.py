import json
from typing import Union, Tuple

class JSONLengthNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_input": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("length",)
    FUNCTION = "get_length"
    CATEGORY = "utils"

    def get_length(self, json_input: str) -> tuple[int]:
        try:
            data = json.loads(json_input)
            if isinstance(data, (list, dict)):
                return (len(data),)
            return (1,)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON input")

class JSONKeyCheckerNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_input": ("STRING", {"multiline": True}),
                "key": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("BOOLEAN", "STRING")
    RETURN_NAMES = ("exists", "value")
    FUNCTION = "check_key"
    CATEGORY = "utils"

    def check_key(self, json_input: str, key: str) -> Tuple[bool, str]:
        try:
            data = json.loads(json_input)
            if not isinstance(data, dict):
                return (False, "")
                
            keys = key.split('.')
            current = data
            
            for k in keys:
                if k not in current:
                    return (False, "")
                current = current[k]
                
            if isinstance(current, (dict, list)):
                value = json.dumps(current)
            else:
                value = str(current)
                
            return (True, value)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON input")

class JSONStringifierNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_input": ("STRING", {"multiline": True}),
                "indent": ("INT", {"default": 2, "min": 0, "max": 8}),
                "sort_keys": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("json_string",)
    FUNCTION = "stringify"
    CATEGORY = "utils"

    def stringify(self, json_input: str, indent: int, sort_keys: bool) -> tuple[str]:
        try:
            data = json.loads(json_input)
            return (json.dumps(data, indent=indent, sort_keys=sort_keys),)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON input") 