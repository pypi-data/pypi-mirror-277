import subprocess
import sys
from .zip import pluliczip

def check_playwright():
    """
    检查 Playwright 及其关联浏览器（Chromium、Firefox、WebKit）是否已安装。
    
    通过调用系统当前的 Python 解释器和 Playwright 的命令行接口，本函数尝试：
    1. 验证 Playwright 是否已安装。
    2. 分别安装或验证 Chromium、Firefox、WebKit 浏览器是否已准备就绪。
    
    如果过程中遇到错误，将捕获异常并打印错误信息。
    """
    try:
        # 使用 sys.executable 确保调用的是当前运行脚本的Python解释器
        # "-m playwright install" 用于检查并安装Playwright自身
        subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)
        
        # 分别检查/安装 Chromium、Firefox、WebKit
        # "--check" 选项在此处未使用，因为早期反馈指出该选项不存在；
        # 直接尝试安装会智能判断是否已安装，避免重复安装
        subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
        subprocess.run([sys.executable, "-m", "playwright", "install", "firefox"], check=True)
        subprocess.run([sys.executable, "-m", "playwright", "install", "webkit"], check=True)
        
        print("Playwright 和所有关联浏览器（Chromium、Firefox、WebKit）已成功安装或已存在。")

        setzip = pluliczip(setzip.get_chromium_7z_path(),setzip.get_plugins_path(),setzip.get_chromium_path())
        
        
    except subprocess.CalledProcessError as e:
        # 如果上述任一命令执行失败，将抛出此异常
        print(f"检查 Playwright 或浏览器安装时发生错误: {e}")

    

# 确保当脚本直接被执行时（而非作为模块导入时）才运行 check_playwright 函数
if __name__ == "__main__":
    check_playwright()