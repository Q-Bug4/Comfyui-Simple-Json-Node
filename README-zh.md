# ComfyUI JSON管理节点集

为ComfyUI提供的一套功能完整的JSON数据处理节点集合。

[English README](README.md)

## 功能特点

1. 解析和提取JSON数据
2. 随机值选择
3. JSON对象和数组遍历
4. JSON合并和修改
5. JSON生成和格式化
6. 键值检查和长度计算

## 安装方法

1. 进入ComfyUI自定义节点目录：
   ```
   cd ComfyUI/custom_nodes/
   ```
2. 克隆仓库：
   ```
   git clone git@github.com:Q-Bug4/Comfyui-Json-Nodes.git
   ```
3. 重启ComfyUI或重新加载自定义节点。

## 可用节点

### 1. JSON解析器
- **输入**: 
  - `json_string`: JSON字符串
  - `path`: 数据路径（可选）
- **输出**: 
  - `parsed_data`: 解析后的JSON或特定值
  - `array_size`: 结果为数组时的长度

### 2. JSON随机值选择器
- **输入**:
  - `json_input`: JSON字符串
  - `max_depth`: 随机选择的最大深度
- **输出**:
  - `random_value`: 随机选择的值

### 3. JSON对象迭代器
- **输入**:
  - `json_input`: JSON对象
  - `index`: 当前索引
  - `mode`: 迭代模式（固定/递增/递减）
- **输出**:
  - `key`: 当前键
  - `value`: 当前值
  - `current_index`: 当前位置
  - `total_items`: 总项目数

### 4. JSON数组迭代器
- **输入**:
  - `json_input`: JSON数组
  - `index`: 当前索引
  - `mode`: 迭代模式（固定/递增/递减）
- **输出**:
  - `item`: 当前项
  - `current_index`: 当前位置
  - `total_items`: 总项目数

### 5. JSON合并器
- **输入**:
  - `json_input_1`: 第一个JSON
  - `json_input_2`: 第二个JSON
  - `merge_strategy`: 合并策略（覆盖/保留/连接）
- **输出**:
  - `merged_json`: 合并后的JSON

### 6. JSON修改器
- **输入**:
  - `json_input`: 待修改的JSON
  - `path`: 修改路径
  - `new_value`: 新值
- **输出**:
  - `modified_json`: 更新后的JSON

### 7. JSON生成器
- **输入**:
  - `key_value_pairs`: 键值对
  - `is_array`: 是否生成数组而不是对象
- **输出**:
  - `generated_json`: 新的JSON结构

### 8. JSON长度计算器
- **输入**:
  - `json_input`: JSON输入
- **输出**:
  - `length`: 项目数量

### 9. JSON键检查器
- **输入**:
  - `json_input`: JSON对象
  - `key`: 待检查的键
- **输出**:
  - `exists`: 布尔结果
  - `value`: 存在时的值

### 10. JSON字符串格式化器
- **输入**:
  - `json_input`: JSON输入
  - `indent`: 缩进空格数
  - `sort_keys`: 是否按字母顺序排序键
- **输出**:
  - `json_string`: 格式化后的JSON字符串

## 路径语法

- 嵌套对象: `object.nestedObject.property`
- 数组元素: `array[0]` 或 `array.0`
- 复杂结构: `object.array[2].property`

## 使用示例

### 1. 遍历JSON
```python
# 输入JSON
{
    "users": [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25}
    ]
}

# 使用数组迭代器，mode="incr"
# 将依次输出每个用户对象
```

### 2. 合并JSON对象
```python
# 第一个输入
{"name": "John", "age": 30}

# 第二个输入
{"age": 31, "city": "New York"}

# 使用覆盖策略的结果
{"name": "John", "age": 31, "city": "New York"}
```

### 3. 随机值选择
```python
# 输入JSON
{
    "colors": ["red", "blue", "green"],
    "sizes": {"S": 10, "M": 20, "L": 30}
}

# 可能返回任意颜色或尺寸值
```

## 错误处理

会在以下情况抛出ValueError：
- 无效的JSON字符串
- 无效的路径或键
- 类型不匹配
- 数组索引越界

## 参与贡献

欢迎改进！步骤如下：
1. Fork本仓库
2. 创建新分支
3. 进行修改
4. 推送到你的Fork
5. 提交Pull Request

## 许可证

MIT许可证。详见[LICENSE](LICENSE)文件。


