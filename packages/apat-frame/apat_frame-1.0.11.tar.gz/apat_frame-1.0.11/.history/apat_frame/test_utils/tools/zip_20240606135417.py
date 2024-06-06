import os
import py7zr
import shutil

def compress_to_7z(input_dir, output_file):
    with py7zr.SevenZipFile(output_file, 'w') as archive:
        archive.writeall(input_dir, os.path.basename(input_dir))

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
input_dir = cp.get_chromium_path()  # 要压缩的目录路径
output_file = cp.get_chromium_7z_path()  # 压缩文件路径

if check_file_exists(output_file):
    print(f"文件 '{output_file}' 已存在。")
else:
    print(f"正在压缩目录: {input_dir}")
    create_directory(os.path.dirname(output_file))  # 创建输出目录（如果不存在）
    compress_to_7z(input_dir, output_file)
    print("压缩完成")
