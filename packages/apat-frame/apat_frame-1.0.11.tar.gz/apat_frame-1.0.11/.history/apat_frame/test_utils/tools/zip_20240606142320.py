import os
import py7zr
import shutil
from commonpath import commonpath

class pluliczip:
    def __init__(self,input_file,output_dir,freepath):
        self.input_file = input_file  #目标文件路径
        self.output_dir = output_dir  #压缩文件路径
        self.freepath = freepath  #解压路径

    def extract_7z(input_file, output_dir):
        with py7zr.SevenZipFile(input_file, 'r') as archive:
            archive.extractall(output_dir)

    def check_file_exists(filepath):
        return os.path.exists(filepath)

    def compress_to_7z(input_dir, output_file):
        with py7zr.SevenZipFile(output_file, 'w') as archive:
            archive.writeall(input_dir, os.path.basename(input_dir))

    def compress(self):
        if self.check_file_exists(self.output_file):
            print(f"文件 '{self.output_file}' 已存在。")
        else:
            print(f"正在压缩目录: {self.input_dir}")
            self.compress_to_7z(self.input_dir, self.output_file)
            print("压缩完成")
        # 示例用法

    def extract(self):    
        if pluliczip.check_file_exists(self.input_dir):
            print(f"文件 '{self.input_dir}' 存在。")
        else:
            print(f"文件 '{self.input_dir}' 不存在。")
            print(f"解压文件路径: {self.app7z_file}")
            pluliczip.extract_7z(self.app7z_file, self.plugins_path)
            print("解压完成")

