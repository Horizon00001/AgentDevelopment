from pathlib import Path
import os


def _resolve(path):
    """解析为绝对路径（基于当前工作目录）。"""
    path = Path(path)
    return path if path.is_absolute() else Path(os.getcwd()) / path


def read_file(file_path):
    try:
        with open(_resolve(file_path), "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"文件 {file_path} 不存在"


def write_file(file_path, content):
    try:
        path = _resolve(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"文件 {file_path} 写入成功"
    except Exception as e:
        return f"写入文件 {file_path} 时出错：{e}"

def run_command(command):
    try:
        import subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"执行命令 {command} 时出错：{e}"
