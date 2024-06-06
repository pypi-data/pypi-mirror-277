import os
from pathlib import Path

class commonpath:
    """
    This class is used to store all the paths used in the project.
    """
    # ALLURE_BIN为allure的bin目录，调用方式为    subprocess.run([ALLURE_BIN, 'generate', results_dir, '-o', report_dir, '--clean'])
    def __init__(self):
        self.allure_bin = os.path.join(Path(__file__).parents[2], 'plugins', 'allure', 'bin', 'allure')
        self.playwright_driver_path_for_mac = os.path.join(Path(__file__).parents[2], 'plugins', 'ms-playwright')
        self.chromium_path = os.path.join(self.playwright_driver_path_for_mac, 'chromium-1117', 'chrome-mac')

        self.appium_path = os.path.join(Path(__file__).parents[2], 'plugins', 'appium')
        self.appium_path = os.path.join(Path(__file__).parents[2], 'plugins', 'appium')

        self.plugins_path = os.path.join(Path(__file__).parents[2], 'plugins')
        
        self.chromium_7z_path = os.path.join(self.playwright_driver_path_for_mac, 'chromium-1117', 'chrome-mac', 'Chromium.app.7z.001')



    def get_appium_path(self):
        return self.appium_path
    def get_appium_7z_path(self):
        return os.path.join(self.plugins_path,'appium.7z')


    def get_allure_path(self):
        return self.allure_path
    def get_allure_7z_path(self):
        return os.path.join(self.plugins_path,'allure.7z')
    


    def get_plugins_path(self):
        return self.plugins_path

        
        # self.tortoise_path = os.path.join(Path(__file__).parents[2], 'plugins', 'tortoise')
        # self.aiohttp_path = os.path.join(Path(__file__).parents[2], 'plugins', 'aiohttp')
        # self.appium_path = os.path.join(Path(__file__).parents[2], 'plugins', 'appium')
        # self.playwright_path = os.path.join(Path(__file__).parents[2], 'plugins', 'playwright')
    def get_allure_bin(self):
        return self.allure_bin

    def get_playwright_driver_path_for_mac(self):
        return self.playwright_driver_path_for_mac

    def get_chromium_path(self):
        return self.chromium_path



if __name__ == '__main__':
    # from appium import webdriver
    import time
    commonpath = commonpath()
    os.environ['PLAYWRIGHT_BROWSERS_PATH'] = commonpath.get_playwright_driver_path_for_mac()

