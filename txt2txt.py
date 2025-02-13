import os

def merge_txt_files(output_file):
    unique_lines = set()  # 存储所有不重复的行

    # 遍历当前目录的所有文件
    for file_name in os.listdir('.'):
        if file_name.endswith('.txt') and file_name != output_file:
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()  # 去除行首尾空格和换行符
                    if line:  # 忽略空行
                        unique_lines.add(line)

    # 将所有不重复的内容写入新的文件
    with open(output_file, 'w', encoding='utf-8') as output:
        for line in sorted(unique_lines):  # 按字母顺序写入
            output.write(line + '\n')

if __name__ == '__main__':
    output_file = 'merged_unique_lines.txt'  # 输出的文件名
    merge_txt_files(output_file)
    print(f'所有TXT文件已合并并去重，结果保存在 {output_file} 中。')
