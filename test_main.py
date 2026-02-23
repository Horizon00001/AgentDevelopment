import pathlib
import test_openai_api
import test_utils
def run_agent(user_task: str) -> str:
    system_prompt = ""
    with open(pathlib.Path(__file__).parent / "prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    messages=[
            {"role": "system", "content": f"{system_prompt}"},
            {"role": "user", "content": f"{user_task}"}
        ]
    while True:
        answer = test_openai_api.call_ai(messages)
        if "<final_answer>" in answer:
            final_answer = answer.split("<final_answer>")[1].split("</final_answer>")[0]
            return final_answer
        if "<action>" in answer:
            action = answer.split("<action>")[1].split("</action>")[0]
            if "read_file" in action:
                file_path = action.split("read_file(")[1].rsplit(")", 1)[0].strip().strip('"\'')
                result = test_utils.read_file(file_path)
            elif "write_file" in action:
                # write_file("a.txt", "hello,world")
                args = action.split("write_file(")[1].rsplit(")", 1)[0]
                # 找到第一个逗号的位置，分隔文件名和内容
                first_comma = args.find(",")
                if first_comma != -1:
                    filename = args[:first_comma].strip().strip('"\'')
                    content = args[first_comma+1:].strip().strip('"\'')
                    result = test_utils.write_file(filename, content)
                else:
                    result = "错误：write_file 需要两个参数"
            elif "run_command" in action:
                command = action.split("run_command(")[1].rsplit(")", 1)[0].strip().strip('"\'')
                result = test_utils.run_command(command)
        messages.append({"role": "assistant", "content": answer})
        observation = f"<observation>{result}</observation>"
        messages.append({"role": "user", "content": f"{observation}"})
        print(messages)

content = "hello,world"
print(run_agent(f"我要在当前文件夹下的test.txt写入{content}"))