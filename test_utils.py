import pathlib

def read_file(file_path):
    # 确保在脚本所在目录下操作文件
    base_dir = pathlib.Path(__file__).parent
    full_path = base_dir / file_path
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(file_path, content):
    # 确保在脚本所在目录下操作文件
    base_dir = pathlib.Path(__file__).parent
    full_path = base_dir / file_path
    # 确保父目录存在
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"文件 {file_path} 写入成功"

def run_command(command):
    import subprocess
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout
