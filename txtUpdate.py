#!/usr/bin/env python3

def process_file(input_file, output_file):
    # 读取文件中的所有行
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 处理每一行：去除首尾空格、转换为小写、替换下划线为空格
    processed = [line.strip().lower().replace('_', ' ') for line in lines if line.strip()]

    # 去除重复项并按字母顺序排序
    unique_sorted = sorted(set(processed))

    # 将处理后的结果写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in unique_sorted:
            f.write(item + '\n')

if __name__ == '__main__':
    # 设置输入文件和输出文件的文件名
    input_filename = 'merged_unique_lines.txt'
    output_filename = 'output.txt'
    
    process_file(input_filename, output_filename)
