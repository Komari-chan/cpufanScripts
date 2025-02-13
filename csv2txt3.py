import csv
import re

def process_artist_name(artist_name):
    # 去除artist:前缀和所有{}、[]符号
    artist_name = re.sub(r'artist:', '', artist_name)
    artist_name = re.sub(r'[\[\]\{\}]', '', artist_name)
    
    # 将单词间的空格替换为下划线，并将所有字符转为小写
    artist_name = artist_name.replace(' ', '_').lower()
    
    return artist_name

def read_and_process_csv(input_csv, output_txt):
    processed_artists = set()  # 存储处理后的艺术家提示词

    with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row:
                continue  # 跳过空行
            
            # 获取每行的第一列数据
            line = row[0]
            # 以逗号分隔，提取艺术家提示词
            artist_prompts = line.split(',')
            for prompt in artist_prompts:
                prompt = prompt.strip()  # 去除前后空格
                processed_prompt = process_artist_name(prompt)
                if processed_prompt:
                    processed_artists.add(processed_prompt)

    # 写入已处理的艺术家提示词到output_txt文件
    with open(output_txt, 'w', encoding='utf-8') as output_file:
        for artist in sorted(processed_artists):
            output_file.write(artist + '\n')

if __name__ == '__main__':
    input_csv = 'input.csv'  # 输入的CSV文件路径
    output_txt = 'processed_artists2.txt'  # 输出的TXT文件路径

    read_and_process_csv(input_csv, output_txt)
