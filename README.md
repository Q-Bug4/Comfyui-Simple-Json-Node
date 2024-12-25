# JSON Management Nodes for ComfyUI

A collection of custom nodes for ComfyUI to manipulate and process JSON data.

为ComfyUI提供的一套JSON数据处理节点集合。

[中文版 README](README-zh.md)

## Features

1. Parse and extract JSON data
2. Random value selection
3. JSON object and array iteration
4. JSON merging and modification
5. JSON generation and formatting
6. Key checking and length calculation

## Installation

1. Go to your ComfyUI custom nodes directory:
   ```
   cd ComfyUI/custom_nodes/
   ```
2. Clone the repository:
   ```
   git clone git@github.com:Q-Bug4/Comfyui-Json-Nodes.git
   ```
3. Restart ComfyUI or reload custom nodes.

## Available Nodes

### 1. Simple JSON Parser
- **Inputs**: 
  - `json_string`: JSON string
  - `path`: Data path (optional)
- **Outputs**: 
  - `parsed_data`: Parsed JSON or specific value
  - `array_size`: Size if result is array

### 2. Random JSON Value
- **Inputs**:
  - `json_input`: JSON string
  - `max_depth`: Maximum depth for random selection
- **Outputs**:
  - `random_value`: Randomly selected value

### 3. JSON Object Iterator
- **Inputs**:
  - `json_input`: JSON object
  - `index`: Current index
  - `mode`: Iteration mode (fixed/incr/decr)
- **Outputs**:
  - `key`: Current key
  - `value`: Current value
  - `current_index`: Current position
  - `total_items`: Total number of items

### 4. JSON Array Iterator
- **Inputs**:
  - `json_input`: JSON array
  - `index`: Current index
  - `mode`: Iteration mode (fixed/incr/decr)
- **Outputs**:
  - `item`: Current item
  - `current_index`: Current position
  - `total_items`: Total number of items

### 5. JSON Merge
- **Inputs**:
  - `json_input_1`: First JSON
  - `json_input_2`: Second JSON
  - `merge_strategy`: Override/Preserve/Concat
- **Outputs**:
  - `merged_json`: Combined JSON result

### 6. JSON Modifier
- **Inputs**:
  - `json_input`: JSON to modify
  - `path`: Path to modify
  - `new_value`: New value
- **Outputs**:
  - `modified_json`: Updated JSON

### 7. JSON Generator
- **Inputs**:
  - `key_value_pairs`: Key-value pairs
  - `is_array`: Generate array instead of object
- **Outputs**:
  - `generated_json`: New JSON structure

### 8. JSON Length
- **Inputs**:
  - `json_input`: JSON input
- **Outputs**:
  - `length`: Number of items

### 9. JSON Key Checker
- **Inputs**:
  - `json_input`: JSON object
  - `key`: Key to check
- **Outputs**:
  - `exists`: Boolean result
  - `value`: Value if exists

### 10. JSON Stringifier
- **Inputs**:
  - `json_input`: JSON input
  - `indent`: Indentation spaces
  - `sort_keys`: Sort keys alphabetically
- **Outputs**:
  - `json_string`: Formatted JSON string

## Path Syntax

- Nested objects: `object.nestedObject.property`
- Array elements: `array[0]` or `array.0`
- Complex structures: `object.array[2].property`

## Examples

### 1. Iterating Through JSON
```python
# Input JSON
{
    "users": [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25}
    ]
}

# Using Array Iterator with mode="incr"
# Will output each user object in sequence
```

### 2. Merging JSON Objects
```python
# First input
{"name": "John", "age": 30}

# Second input
{"age": 31, "city": "New York"}

# Result with strategy="override"
{"name": "John", "age": 31, "city": "New York"}
```

### 3. Random Value Selection
```python
# Input JSON
{
    "colors": ["red", "blue", "green"],
    "sizes": {"S": 10, "M": 20, "L": 30}
}

# Random value might return any color or size value
```

## Error Handling

ValueError is raised for:
- Invalid JSON strings
- Invalid paths or keys
- Type mismatches
- Array index out of bounds

## Contributing

Improvements are welcome! Steps:
1. Fork the repository
2. Create a new branch
3. Make changes
4. Push to your fork
5. Submit a Pull Request

## License

MIT License. See [LICENSE](LICENSE) file for details.