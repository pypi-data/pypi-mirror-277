from tortoise.models import Model
from tortoise import fields
# 定义一个Tortoise-ORM模型类
class CaseManageModel(Model):
    # 定义模型的字段
    code = fields.CharField(pk=True, max_length=255)  # 字符串主键
    name = fields.CharField(max_length=255)  # 最大长度为255的字符字段
    description = fields.TextField()  # 文本字段，没有长度限制
    category1 = fields.CharField(max_length=50)
    category2 = fields.CharField(max_length=50, null=True)  # 允许为NULL，与数据库表定义匹配
    status = fields.IntField(null=True)  # 允许为NULL，与数据库表定义匹配
    script = fields.TextField()
    expected = fields.TextField()  # 修正拼写错误
    actual = fields.TextField()
    result = fields.CharField(max_length=50, null=True)  # 允许为NULL，与数据库表定义匹配
    create_time = fields.DatetimeField(auto_now_add=True)
    update_time = fields.DatetimeField(auto_now=True)
    creator = fields.CharField(max_length=50, null=True)  # 允许为NULL，与数据库表定义匹配
    updater = fields.CharField(max_length=50, null=True)  # 允许为NULL，与数据库表定义匹配


    # 定义元数据类，用于配置模型
    class Meta:
        table = "casemanage"  # 表名，需要替换为实际的表名
        # 如果需要指定数据库连接，可以通过 `db_url` 指定，例如
        # db_url = 'postgres://user:password@host:port/dbname'
        # 注意：在这个例子中，我们通过 `Tortoise.init` 在外部设置数据库连接
