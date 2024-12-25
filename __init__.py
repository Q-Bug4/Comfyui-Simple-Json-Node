from .json_node import SimpleJSONParserNode
from .random_json_node import RandomJSONValueNode
from .json_iterator_node import JSONObjectIteratorNode, JSONArrayIteratorNode
from .json_merge_node import JSONMergeNode
from .json_modifier_node import JSONModifierNode
from .json_generator_node import JSONGeneratorNode
from .json_utility_nodes import JSONLengthNode, JSONKeyCheckerNode, JSONStringifierNode

NODE_CLASS_MAPPINGS = {
    "JSONParserNode": SimpleJSONParserNode,
    "RandomJSONValueNode": RandomJSONValueNode,
    "JSONObjectIteratorNode": JSONObjectIteratorNode,
    "JSONArrayIteratorNode": JSONArrayIteratorNode,
    "JSONMergeNode": JSONMergeNode,
    "JSONModifierNode": JSONModifierNode,
    "JSONGeneratorNode": JSONGeneratorNode,
    "JSONLengthNode": JSONLengthNode,
    "JSONKeyCheckerNode": JSONKeyCheckerNode,
    "JSONStringifierNode": JSONStringifierNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "JSONParserNode": "Simple JSON Parser",
    "RandomJSONValueNode": "Random JSON Value",
    "JSONObjectIteratorNode": "JSON Object Iterator",
    "JSONArrayIteratorNode": "JSON Array Iterator",
    "JSONMergeNode": "JSON Merge",
    "JSONModifierNode": "JSON Modifier",
    "JSONGeneratorNode": "JSON Generator",
    "JSONLengthNode": "JSON Length",
    "JSONKeyCheckerNode": "JSON Key Checker",
    "JSONStringifierNode": "JSON Stringifier"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]