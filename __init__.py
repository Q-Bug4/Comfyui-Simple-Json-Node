from .json_node import SimpleJSONParserNode


NODE_CLASS_MAPPINGS = {
    "JSONParserNode": SimpleJSONParserNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "JSONParserNode": "Simple JSON Parser"
}

__all__ = ["NODE_CLASS_MAPPINGS"]