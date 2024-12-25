import json
from typing import Union, Tuple
import time

class JSONObjectIteratorNode:
    stored_index = 0
    last_update_time = 0
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_input": ("STRING", {"multiline": True}),
                "index": ("INT", {"default": 0, "min": 0}),
                "mode": (["fixed", "incr", "decr"], {"default": "fixed"}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "INT", "INT")
    RETURN_NAMES = ("key", "value", "current_index", "total_items")
    FUNCTION = "iterate_object"
    CATEGORY = "utils"

    @classmethod
    def IS_CHANGED(cls, **kwargs) -> float:
        mode = kwargs.get("mode", "fixed")
        if mode != "fixed":
            # 返回当前时间戳，确保节点会在每次执行时重新运行
            return time.time()
        return float("NaN")

    def iterate_object(self, json_input: str, index: int, mode: str) -> Tuple[str, str, int, int]:
        try:
            data = json.loads(json_input)
            if not isinstance(data, dict):
                raise ValueError("Input must be a JSON object")

            items = list(data.items())
            total_items = len(items)
            
            if total_items == 0:
                return ("", "", 0, 0)

            # 使用存储的索引或初始索引
            current_index = self.stored_index if mode != "fixed" else index
            current_index = current_index % total_items

            # 根据模式计算下一个索引
            if mode == "incr":
                next_index = (current_index + 1) % total_items
            elif mode == "decr":
                next_index = (current_index - 1) % total_items
            else:  # fixed
                next_index = current_index

            # 更新存储的索引
            if mode != "fixed":
                self.__class__.stored_index = next_index

            key, value = items[current_index]
            
            if isinstance(value, (dict, list)):
                value = json.dumps(value)
            else:
                value = str(value)
                
            return (str(key), value, current_index, total_items)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON input")

class JSONArrayIteratorNode:
    stored_index = 0
    last_update_time = 0
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "json_input": ("STRING", {"multiline": True}),
                "index": ("INT", {"default": 0, "min": 0}),
                "mode": (["fixed", "incr", "decr"], {"default": "fixed"}),
            },
        }

    RETURN_TYPES = ("STRING", "INT", "INT")
    RETURN_NAMES = ("item", "current_index", "total_items")
    FUNCTION = "iterate_array"
    CATEGORY = "utils"

    @classmethod
    def IS_CHANGED(cls, **kwargs) -> float:
        mode = kwargs.get("mode", "fixed")
        if mode != "fixed":
            # 返回当前时间戳，确保节点会在每次执行时重新运行
            return time.time()
        return float("NaN")

    def iterate_array(self, json_input: str, index: int, mode: str) -> Tuple[str, int, int]:
        try:
            data = json.loads(json_input)
            if not isinstance(data, list):
                raise ValueError("Input must be a JSON array")

            total_items = len(data)
            if total_items == 0:
                return ("", 0, 0)

            # 使用存储的索引或初始索引
            current_index = self.stored_index if mode != "fixed" else index
            current_index = current_index % total_items

            # 根据模式计算下一个索引
            if mode == "incr":
                next_index = (current_index + 1) % total_items
            elif mode == "decr":
                next_index = (current_index - 1) % total_items
            else:  # fixed
                next_index = current_index

            # 更新存储的索引
            if mode != "fixed":
                self.__class__.stored_index = next_index

            item = data[current_index]
            
            if isinstance(item, (dict, list)):
                item = json.dumps(item)
            else:
                item = str(item)
                
            return (item, current_index, total_items)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON input") 