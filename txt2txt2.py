def convert_txt_to_comma_separated(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = [line.strip() for line in infile if line.strip()]  # 读取非空行并去除两端空格

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(', '.join(lines))  # 用逗号和空格连接所有行

if __name__ == '__main__':
    input_file = 'merged_unique_lines.txt'  # 输入的文件名
    output_file = 'comma_separated.txt'  # 输出的文件名
    convert_txt_to_comma_separated(input_file, output_file)
    print(f'{input_file} 文件已转换为逗号分隔格式，结果保存在 {output_file} 中。')
