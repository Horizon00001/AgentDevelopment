# Agent Development

一个简单的 AI Agent 开发测试项目，基于 DeepSeek API 实现文件操作和命令执行功能。

## 功能特性

- **文件读取** - 读取指定文件内容
- **文件写入** - 将内容写入指定文件
- **命令执行** - 执行终端命令

## 项目结构

```
Agent Development/
├── test_main.py        # 主程序入口
├── test_openai_api.py  # API 调用封装
├── test_utils.py       # 文件操作和命令执行工具函数
├── prompt.txt          # 系统提示词
├── .env                # 环境变量（API 密钥）- 需自行创建
├── .env.example        # 环境变量模板
├── .gitignore          # Git 忽略文件配置
└── README.md           # 项目说明文档
```

## 环境要求

- Python 3.8+
- OpenAI 兼容的 API 密钥（DeepSeek、OpenAI 等）

## 安装依赖

```bash
pip install openai python-dotenv
```

## 配置

1. 复制 `.env.example` 文件为 `.env`：
   ```bash
   cp .env.example .env
   ```
2. 编辑 `.env` 文件，填入你的真实 API 密钥

```env
OPENAI_API_KEY=your_api_key_here
BASE_URL=https://api.deepseek.com
```

### 支持的 API 提供商

| 提供商       | BASE_URL                      |
| ------------ | ----------------------------- |
| DeepSeek     | `https://api.deepseek.com`  |
| OpenAI       | `https://api.openai.com/v1` |
| 其他兼容 API | 对应的 base_url               |

**注意**：默认使用 `deepseek-chat` 模型，如需更换请修改 `test_openai_api.py` 中的 `model` 参数。

## 使用方法

运行主程序：

```bash
python test_main.py
```

程序会调用 AI 模型，根据用户输入的任务自动执行文件操作。

### 示例

```python
content = "hello,world"
print(run_agent(f"我要在当前文件夹下的test.txt写入{content}"))
```

AI 会自动解析任务并执行相应的文件写入操作。

## AI 交互格式

AI 按照以下格式与系统交互：

```xml
<thought>思考过程</thought>
<action>工具名称(参数1, 参数2)</action>
```

任务完成后输出：

```xml
<final_answer>最终结果</final_answer>
```

## 可用工具

| 工具                               | 功能     | 示例                             |
| ---------------------------------- | -------- | -------------------------------- |
| `read_file(file_path)`           | 读取文件 | `read_file("a.txt")`           |
| `write_file(file_path, content)` | 写入文件 | `write_file("a.txt", "hello")` |
| `run_command(command)`           | 执行命令 | `run_command("ls -la")`        |

## 注意事项

- 文件操作默认在脚本所在目录进行
- `.env` 文件包含敏感信息，已添加到 `.gitignore`，请勿提交到版本控制
- 确保 API 密钥安全，不要泄露给他人

## License

MIT
