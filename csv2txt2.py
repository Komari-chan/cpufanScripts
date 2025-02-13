import csv

def convert_csv_to_txt(input_csv, output_txt):
    # 读取CSV文件并写入到TXT文件中
    with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        with open(output_txt, 'w', encoding='utf-8') as txtfile:
            for row in reader:
                if row:
                    # 获取每行的第一个元素（单个提示词），去除前后空格后写入TXT文件
                    txtfile.write(row[0].strip() + '\n')

if __name__ == '__main__':
    input_csv = 'single_word.csv'  # 输入的CSV文件路径
    output_txt = 'converted_words.txt'  # 输出的TXT文件路径

    convert_csv_to_txt(input_csv, output_txt)
