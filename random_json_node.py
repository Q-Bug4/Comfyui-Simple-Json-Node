import json
import random
from typing import Union, Any

class RandomJSONValueNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_input": ("STRING", {"multiline": True}),
                "max_depth": ("INT", {"default": -1, "min": -1, "max": 100}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("random_value",)
    FUNCTION = "get_random_value"
    CATEGORY = "utils"

    def get_random_value(self, json_input: str, max_depth: int) -> tuple[str]:
        try:
            data = json.loads(json_input)
            value = self._get_random_value(data, current_depth=0, max_depth=max_depth)
            return (str(value),)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON input")

    def _get_random_value(self, data: Any, current_depth: int, max_depth: int) -> Any:
        if max_depth != -1 and current_depth > max_depth:
            return data
            
        if isinstance(data, dict):
            key = random.choice(list(data.keys()))
            return self._get_random_value(data[key], current_depth + 1, max_depth)
        elif isinstance(data, list):
            if not data:
                return None
            return self._get_random_value(random.choice(data), current_depth + 1, max_depth)
        else:
            return data 