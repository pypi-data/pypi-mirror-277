import os
import py7zr
import shutil
from commonpath import commonpath

class pluliczip:
    def __init__(self):
        self.commonpath = commonpath()
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

    def compress_to_7z(input_dir, output_file):
        with py7zr.SevenZipFile(output_file, 'w') as archive:
            archive.writeall(input_dir, os.path.basename(input_dir))

    def compress(input_dir, output_file):
        if check_file_exists(output_file):
            print(f"文件 '{output_file}' 已存在。")
        else:
            print(f"正在压缩目录: {input_dir}")
            create_directory(os.path.dirname(output_file))  # 创建输出目录（如果不存在）
            compress_to_7z(input_dir, output_file)
            print("压缩完成")
        # 示例用法

        
        if pluliczip.check_file_exists(input_dir):
            print(f"文件 '{input_dir}' 存在。")
        else:
            print(f"文件 '{input_dir}' 不存在。")
            print(f"解压文件路径: {app7z_file}")
            pluliczip.extract_7z(app7z_file, plugins_path)
            print("解压完成")

class setupzip:

# 示例用法
    cp = commonpath()
    input_dir = cp.get_appium_path()  # 要压缩的目录路径
    app7z_file = cp.get_appium_7z_path()  # 压缩文件路径
    plugins_path = cp.get_plugins_path()

    # if check_file_exists(output_file):
    #     print(f"文件 '{output_file}' 已存在。")
    # else:
    #     print(f"正在压缩目录: {input_dir}")
    #     create_directory(os.path.dirname(output_file))  # 创建输出目录（如果不存在）
    #     compress_to_7z(input_dir, output_file)
    #     print("压缩完成")
    # # 示例用法

    
    if pluliczip.check_file_exists(input_dir):
        print(f"文件 '{input_dir}' 存在。")
    else:
        print(f"文件 '{input_dir}' 不存在。")
        print(f"解压文件路径: {app7z_file}")
        pluliczip.extract_7z(app7z_file, plugins_path)
        print("解压完成")

