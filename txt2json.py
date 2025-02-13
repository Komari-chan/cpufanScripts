import re
import uuid
import json

# 读取TXT文件并处理提示词
def process_txt(input_file, output_file):
    unique_prompts = set()

    # 读取并处理TXT文件
    with open(input_file, mode='r', encoding='utf-8') as txtfile:
        content = txtfile.read()
        # 将所有提示词按逗号分割，并去除前后空格
        prompts = [prompt.strip() for prompt in content.split(',')]
        # 添加不重复的提示词到集合中
        unique_prompts.update(prompts)

    # 去除空字符串
    unique_prompts = [prompt for prompt in unique_prompts if prompt]

    # 构建 JSON 结构
    json_data = {
        "cooling": 2,
        "realTimeSave": True,
        "autoDownloadZIP": False,
        "removeAnmition": False,
        "tasks": [
            {
                "uuid": str(uuid.uuid4()),
                "title": "",
                "activate": True,
                "random": False,
                "nums": len(unique_prompts),
                "fold": False,
                "size": {
                    "width": 832,
                    "height": 1216
                },
                "prompts": {
                    "splice": True,
                    "random": False,
                    "data": [
                        {
                            "uuid": str(uuid.uuid4()),
                            "data": [
                                {
                                    "uuid": str(uuid.uuid4()),
                                    "data": prompt,
                                    "ignore": False
                                } for prompt in unique_prompts
                            ],
                            "type": "combination",
                            "choices": 1,
                            "color": "rgba(255,255,255,0.63)",
                            "ignore": False
                        }
                    ]
                },
                "uprompts": {
                    "data": [
                        {
                            "uuid": str(uuid.uuid4()),
                            "data": "multiple boys, 1boy, male focus, pov hands, doll, chibi, toy, grayscale, text, deformed, @_@, multiple views, ", 
                            "ignore": False
                        }
                    ]
                }
            }
        ]
    }

    # 将数据写入 JSON 文件
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

    print(f"JSON 文件已生成：{output_file}")

if __name__ == '__main__':
    input_txt = "comma_separated.txt"  # 替换为你的TXT文件名
    output_json = "output.json"  # 生成的JSON文件名
    process_txt(input_txt, output_json)
