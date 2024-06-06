import os
import py7zr
import shutil
from commonpath import commonpath

def extract_7z(input_file, output_dir):
    with py7zr.SevenZipFile(input_file, 'r') as archive:
        archive.extractall(output_dir)

def check_file_exists(file_path):
    return os.path.exists(file_path)

def create_directory(dir_path):
    os.makedirs(dir_path, exist_ok=True)

def clear_directory(dir_path):
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

# 示例用法
cp = commonpath()
file_path = os.path.join(cp.get_chromium_path(), 'Chromium.app')  # 文件路径
seven_zip_path = cp.get_chromium_7z_path()   # 第一个分卷文件路径
output_dir = os.path.dirname(file_path)     # 输出目录

if check_file_exists(file_path):
    print(f"文件 '{file_path}' 存在。")
else:
    print(f"文件 '{file_path}' 不存在。")
    print(f"解压文件路径: {seven_zip_path}")
    if check_file_exists(seven_zip_path):
        create_directory(output_dir)  # 创建输出目录
        clear_directory(output_dir)   # 清空输出目录
        extract_7z(seven_zip_path, output_dir)
        print("解压完成")
    else:
        print(f"分卷文件 '{seven_zip_path}' 不存在。")
