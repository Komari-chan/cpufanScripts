import csv
import re

def process_artist_name(artist_name):
    # 去除artist:前缀和所有{}、[]符号
    artist_name = re.sub(r'artist:', '', artist_name)
    artist_name = re.sub(r'[\[\]\{\}]', '', artist_name)
    
    # 将单词间的空格替换为下划线，并将所有字符转为小写
    artist_name = artist_name.replace(' ', '_').lower()
    
    return artist_name

def read_and_process_csv(input_csv, recognized_txt, unrecognized_txt):
    recognized_artists = set()  # 存储已识别的艺术家提示词
    unrecognized_lines = []     # 存储未识别的行

    with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row:
                continue  # 跳过空行
            
            # 获取每行的第一列数据
            line = row[0]
            # 检查year 2023的位置
            year_index = line.find('year 2023')
            
            if year_index != -1:
                # 去掉year 2023及其后面的内容
                line = line[:year_index]
                # 以逗号分隔，提取艺术家提示词
                artist_prompts = line.split(',')
                for prompt in artist_prompts:
                    prompt = prompt.strip()  # 去除前后空格
                    processed_prompt = process_artist_name(prompt)
                    if processed_prompt:
                        recognized_artists.add(processed_prompt)
            else:
                # 如果未找到year 2023，则将整个行内容加入未识别列表
                unrecognized_lines.append(line)

    # 写入已识别的艺术家提示词到recognized_txt文件
    with open(recognized_txt, 'w', encoding='utf-8') as recog_file:
        for artist in sorted(recognized_artists):
            recog_file.write(artist + '\n')

    # 写入未识别的行到unrecognized_txt文件
    with open(unrecognized_txt, 'w', encoding='utf-8') as unrecog_file:
        for line in unrecognized_lines:
            unrecog_file.write(line + '\n')

if __name__ == '__main__':
    input_csv = 'input.csv'  # 输入的CSV文件路径
    recognized_txt = 'recognized_artists.txt'  # 存储已识别艺术家提示词的文件路径
    unrecognized_txt = 'unrecognized_lines.txt'  # 存储未识别行的文件路径

    read_and_process_csv(input_csv, recognized_txt, unrecognized_txt)
