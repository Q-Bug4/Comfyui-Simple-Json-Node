# Simple JSON Parser Node for ComfyUI

A custom node for ComfyUI to parse and extract data from JSON strings.

[中文版 README](README-zh.md)

## Features

1. Parse JSON strings
2. Access specific JSON content using paths
3. Output formatted JSON or simple string values

## Installation

1. Go to your ComfyUI custom nodes directory:
   ```
   cd ComfyUI/custom_nodes/
   ```
2. Clone the repository:
   ```
   git clone https://github.com/yourusername/comfyui-simple-json-parser.git
   ```
3. Restart ComfyUI or reload custom nodes.

## Usage

Find the "Simple JSON Parser" node in the "utils" category of ComfyUI.

Inputs:
- `json_string`: JSON string (multiline supported)
- `path`: Data path (optional)

Output: Parsed JSON data or specific value

### Path Syntax

- Nested objects: `object.nestedObject.property`
- Array elements: `array[0]`
- Complex structures: `object.array[2].property`

## Examples

1. Parse JSON:
   - Input: `{"name": "John", "age": 30}`
   - Path: (empty)
   - Output: Formatted JSON

2. Access property:
   - Input: `{"user": {"name": "Alice", "email": "alice@example.com"}}`
   - Path: `user.email`
   - Output: `alice@example.com`

3. Access array:
   - Input: `{"items": ["apple", "banana", "cherry"]}`
   - Path: `items[1]`
   - Output: `banana`

## Error Handling

ValueError is raised for:
- Invalid JSON string
- Invalid path or key not found

## Contributing

Improvements are welcome! Steps:
1. Fork the repository
2. Create a new branch
3. Make changes
4. Push to your fork
5. Submit a Pull Request

## License

MIT License. See [LICENSE](LICENSE) file for details.