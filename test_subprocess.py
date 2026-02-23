import subprocess

result = subprocess.run("echo hello", shell=True, capture_output=True, text=True)
print(result.returncode)
print(result.stdout)
