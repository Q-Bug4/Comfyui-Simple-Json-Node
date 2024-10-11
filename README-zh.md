# ComfyUI 简易 JSON 解析器节点

这是一个为 ComfyUI 设计的自定义节点，用于解析和提取 JSON 字符串中的数据。

## 功能

1. 解析 JSON 字符串
2. 通过路径访问特定 JSON 内容
3. 输出格式化 JSON 或简单字符串值

## 安装

1. 进入 ComfyUI 自定义节点目录：
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. 克隆仓库：
   ```bash
   git clone https://github.com/yourusername/comfyui-simple-json-parser.git
   ```
3. 重启 ComfyUI 或重新加载自定义节点。

## 使用方法

在 ComfyUI 的 "utils" 类别中找到 "Simple JSON Parser" 节点。

输入：
- `json_string`：JSON 字符串（支持多行）
- `path`：数据路径（可选）

输出：解析后的 JSON 数据或特定值

### 路径语法

- 嵌套对象：`object.nestedObject.property`
- 数组元素：`array[0]`
- 复杂结构：`object.array[2].property`

## 示例

1. 解析 JSON：
   - 输入：`{"name": "张三", "age": 30}`
   - 路径：（空）
   - 输出：格式化 JSON

2. 访问属性：
   - 输入：`{"user": {"name": "李四", "email": "lisi@example.com"}}`
   - 路径：`user.email`
   - 输出：`lisi@example.com`

3. 访问数组：
   - 输入：`{"items": ["苹果", "香蕉", "樱桃"]}`
   - 路径：`items[1]`
   - 输出：`香蕉`

## 错误处理

遇到以下情况会抛出 ValueError：
- 无效的 JSON 字符串
- 无效的路径或找不到键

## 贡献

欢迎改进此项目！步骤：
1. Fork 仓库
2. 创建新分支
3. 提交更改
4. 推送到 Fork
5. 提交 Pull Request

## 许可

MIT 许可证。详见 [LICENSE](LICENSE) 文件.


