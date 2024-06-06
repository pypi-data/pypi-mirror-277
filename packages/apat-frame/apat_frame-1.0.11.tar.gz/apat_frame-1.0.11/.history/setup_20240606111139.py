from setuptools import setup, find_packages
import os

VERSION = '1.0.4'
DESCRIPTION = '本库旨在完成全流程自动化测试，包括webUI自动化测试，移动端自动化测试，接口自动化测试，自动化测试报告生成，自动化测试用例管理，自动化测试数据管理，自动化测试用例执行，自动化测试用例执行结果展示，自动化测试用例执行结果统计，自动化测试用例执行结果导出，自动化测试用例执行结果导入，自动化测试用例执行结果对比，自动化测试用例执行结果对比结果展示，自动化测试用例执行结果对比结果导出，自动化测试用例执行结果对比结果导入，自动化测试用例执行结果对比结果对比，自动化测试用例执行'

with open("README.md","r") as f:
    long_description = f.read()


setup(
    name="apat_frame",
    version=VERSION,
    author="zhangyuze",
    author_email="zhangyuze1113@163.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['aiohttp==3.9.5', 'allure-pytest==2.13.5', 'setuptools==70.0.0', 'Appium-Python-Client==4.0.0', 'playwright==1.44.0', 'pytest==8.2.2', 'tortoise-orm==0.21.3', 'aiosqlite==0.17.0', 'asyncpg==0.29.0', 'aiomysql==0.2.0', 'pillow==10.3.0', 'aiofiles==23.2.1', 'numpy==1.26.4'],
    # keywords=['python', 'moviepy', 'cut video'],
    # data_files=[('cut_video', ['cut_video/clip_to_erase.json'])],
    # entry_points={
    # 'console_scripts': [
    #     'cut_video = cut_video.main:main'
    # ]
    # },
    license="MIT",
    url="",
    # scripts=['cut_video/cut_video.py'],
    # classifiers= [
    #     "Development Status :: 3 - Alpha",
    #     "Intended Audience :: Developers",
    #     "Programming Language :: Python :: 3",
    #     "Operating System :: Microsoft :: Windows"
    # ]
)


# setup()函数中定义了多个参数来配置项目：

# name: 项目名称。
# version: 项目的版本号。
# author: 作者名。
# author_email: 作者的电子邮件地址。
# description: 简短的项目描述。
# long_description_content_type: 长描述的类型，这里是Markdown格式。
# long_description: 项目的长描述，从README.md文件读取。
# packages: 通过find_packages()找到的项目包列表。
# install_requires: 项目依赖的Python包列表，这里是空的，意味着没有明确的外部依赖。
# classifiers: 项目分类，如开发状态、受众、编程语言和操作系统等。
# license: 项目使用的许可证类型，这里是MIT许可证。
# url: 项目链接，这里是空的。
# 注释掉的部分data_files和entry_points通常用于指定额外的数据文件和命令行脚本，但在这个例子中未使用。
# classifiers列表提供了关于项目的元数据，例如开发状态、预期受众和支持的Python版本等。

# # scripts=['cut_video/cut_video.py']: 如果这个未被注释，它会将cut_video.py添加为可执行脚本，但是在这个例子中，它被注释掉了。

# 最后的classifiers列表用于在PyPI上分类项目，便于用户搜索和过滤。