import pathlib
with open(pathlib.Path(__file__).parent / "prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read()
    print(prompt)