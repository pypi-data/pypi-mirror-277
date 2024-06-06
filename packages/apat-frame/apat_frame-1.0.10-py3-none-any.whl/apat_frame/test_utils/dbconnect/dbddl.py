from tortoise.models import Model
from tortoise import fields, Tortoise
import asyncio
from dbsetting.app1 import CaseManageModel
import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
from datetime import datetime

def model_to_dict(instance):
    return {key: value for key, value in instance.__dict__.items() if not key.startswith('_')}

# 初始化Tortoise-ORM，配置数据库连接和模型注册
async def init_tortoise(url):
    # 设置数据库连接信息
    await Tortoise.init(
        {
            'connections': {
                'default': url,  # 或 MYSQL_URI, MSSQL_URI 根据需要
            },
            'apps': {
                'models': {
                    'models': ['dbsetting.app1'],  # 这里填你的模型所在的模块
                    'default_connection': 'default',
                }
            },
            'timezone': 'Asia/Shanghai',  # 添加这一行来设置时区

        },
    )
    # 设置日志配置
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    # 自动创建表，如果不存在的话
    # await Tortoise.generate_schemas()


# 使用Tortoise-ORM进行CRUD操作
# async def crud_operations():
#     # 增加记录
#     # await testcaseModel.create(column1='value1', column2='value2')

#     # 查询所有记录
#     instances = await CaseManageModel.all()
#     # 打印查询结果
#     for instance in instances:
        # for field_name, field_value in instance.__dict__.items():
        #     if not field_name.startswith('_'):  # 忽略Python的特殊属性（以下划线开头）
        #         print(f"{field_name}: {field_value}")
        # print(model_to_dict(instance))
        # print(instance.__dict__.items())

    # # 更新记录
    # instance = await testcaseModel.get(id=1)  # 获取id为1的记录
    # instance.column1 = 'new_value'  # 修改值
    # await instance.save()  # 保存更改

    # # 删除记录
    # await testcaseModel.filter(id=1).delete()  # 删除id为1的记录

# 进行搜索操作
async def selectall_operations():
    # 查询所有记录
    instances = await CaseManageModel.all()
    # 返回数组
    return model_to_dict(instances)
async def select_operations(filter1,value):
    # 查询对应记录
    instances = await CaseManageModel.filter(filter1 = value)
    # 返回数组
    return model_to_dict(instances)
async def update_operations(value,newvalue):
    # 查询对应记录
    instances = await CaseManageModel.get(code=value)
    # 更新对应记录
    instances.fiflter = newvalue
    # 保存更改
    await instances.save()

async def delete_operations(value):
    # 查询对应记录
    instances = await CaseManageModel.get(code=value)
    # 删除对应记录
    await instances.delete()

async def insert_operations(code,name,description,category1,category2, status, script, expected, actual, result, creator, updater):
    # 创建记录
    await CaseManageModel.create(code=code, name=name, description=description, category1=category1, category2=category2, status=status, script=script, expected=expected, actual=actual, result=result, creator=creator, updater=updater)
    return "success"
    # code = fields.CharField(pk=True, max_length=255)  # 字符串主键
    # name = fields.CharField(max_length=255)  # 最大长度为255的字符字段
    # description = fields.TextField()  # 文本字段，没有长度限制
    # category1 = fields.CharField(max_length=50)
    # category2 = fields.CharField(max_length=50, null=True)  # 允许为NULL，与数据库表定义匹配
    # status = fields.IntField(null=True)  # 允许为NULL，与数据库表定义匹配
    # script = fields.TextField()
    # expected = fields.TextField()  # 修正拼写错误
    # actual = fields.TextField()
    # result = fields.CharField(max_length=50, null=True)  # 允许为NULL，与数据库表定义匹配
    # create_time = fields.DatetimeField(auto_now_add=True)
    # update_time = fields.DatetimeField(auto_now=True)
    # creator = fields.CharField(max_length=50, null=True)  # 允许为NULL，与数据库表定义匹配
    # updater = fields.CharField(max_length=50, null=True)  # 允许为NULL，与数据库表定义匹配


# 主函数，用于运行整个程序
async def main():
    mysqlurl = 'mysql://root:123456@127.0.0.1:3306/zhangyuze'
    # 初始化Tortoise-ORM
    await init_tortoise(mysqlurl)
    # 执行CRUD操作
    
    # 获取当前时间
    current_time = datetime.now()

    # 格式化时间
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    await insert_operations('ceshi003','mingcheng001','kkkkkk','cate1','cate2','1','script','expected','actual','result','creator','updater')

# 当脚本直接运行时，执行主函数
if __name__ == "__main__":
    asyncio.run(main())