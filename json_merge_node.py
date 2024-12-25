import json
from typing import Union, Any

class JSONMergeNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_input_1": ("STRING", {"multiline": True}),
                "json_input_2": ("STRING", {"multiline": True}),
                "merge_strategy": (["override", "preserve", "concat"], {"default": "override"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("merged_json",)
    FUNCTION = "merge_json"
    CATEGORY = "utils"

    def merge_json(self, json_input_1: str, json_input_2: str, merge_strategy: str) -> tuple[str]:
        try:
            data1 = json.loads(json_input_1)
            data2 = json.loads(json_input_2)
            
            if isinstance(data1, list) and isinstance(data2, list):
                result = data1 + data2
            elif isinstance(data1, dict) and isinstance(data2, dict):
                result = self._merge_dicts(data1, data2, merge_strategy)
            else:
                raise ValueError("Both inputs must be of the same type (either objects or arrays)")
                
            return (json.dumps(result, indent=2),)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON input")

    def _merge_dicts(self, dict1: dict, dict2: dict, strategy: str) -> dict:
        result = dict1.copy()
        
        for key, value in dict2.items():
            if key not in result:
                result[key] = value
            else:
                if strategy == "override":
                    result[key] = value
                elif strategy == "preserve":
                    continue
                elif isinstance(result[key], dict) and isinstance(value, dict):
                    result[key] = self._merge_dicts(result[key], value, strategy)
                elif isinstance(result[key], list) and isinstance(value, list):
                    result[key] = result[key] + value
                    
        return result 