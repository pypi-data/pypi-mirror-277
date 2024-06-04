# apat_frame
 
版本信息：1.0.0
版本描述：该库将提供一个全面的、通用的自动化测试框架，旨在完成webUI自动化、接口自动化以及移动端自动化测试。
版本详情：app_plugin中安装appium库，web_plugin中安装playwright和aiohttp库，然后通过test_utils进行pytest集成与二次封装和单元测试。后续依赖库playwright、aiohttp、playwright、pytest需要更新的时候，对组件进行整体覆盖，然后跑单元测试，单元测试通过后再进行发布；test_utils中还包含各类工具。
测试用例字段：
code-编号：以当前时间戳生成
name-名称：用例名称
desccription-描述：用例描述，可为空
category1-分类：用例大分类，不可为空，分为webui、interface、mobile
category2-分类：用例小分类，可为空，自定义分类
status-状态：用例状态
script-脚本：用例脚本，不可为空
expected-预期结果：用例预期结果，可为空
actual-实际结果：用例实际结果，可为空
result-结果：用例结果，可为空
create_time-创建时间：用例创建时间，可为空
update_time-更新时间：用例更新时间，可为空
creator-创建人：用例创建人，可为空
updater-更新人：用例更新人，可为空


对于任意测试用例，都存在编号、名称、用例大分类
当该用例属于webui和移动端Ui时，script字段中存入json格式为
{
    "script": "",
    "kargs": {
        "number": "",
        "password": "",
        ...

    }
}
当该用例属于接口自动化用例时，script字段中存入json格式为
{
    "method": "",
    "url": "",
    "kwargs": {
        "Content-Type": "application/json",
        ...
    }
}

ceshi1