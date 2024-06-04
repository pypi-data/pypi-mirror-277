# py脚手架

## 安装
python版本号: ```3.10.12```

pip安装: ```pip install binmao_libs```

## 相关模块
### orm
使用```peewee```orm框架

代码样例:
```python
from binmao_libs import db
from peewee import *

# 创建database实例
mysql_db = db.connect(config.mysql_connection)
# 创建orm对象(表访问对象)
class MetaMoment(Model):
	"""动态实体类
    """
	id = IntegerField(unique=True)
	uid = CharField()
	text = CharField()
	category_id = IntegerField(column_name="categoryId")
	created_at = DateTimeField(column_name="createdAt")
	class Meta:
		database = mysql_db
		table_name = "moment__moment"

class MetaUserInfo(Model):
	"""用户信息
	"""
	id = IntegerField(unique=True)
	nickname = CharField()
	class Meta:
		database = mysql_db
		table_name = "metacat__user_info"

# 表查询
cursor = MetaMoment.select().limit(10)
for record in cursor:
	print(f"text: {record.text}")
	
# 设置特定返回字段(prject)
cursor = MetaMoment.select(MetaMoment.id.alias("_id")).limit(10)
for record in cursor:
	print(f"_id: {record._id}")

# 返回使用函数
cursor = MetaMoment.select(fn.COUNT(MetaMoment.id))
print(f"总数: {next(iter(cursor))}")

# 带游标查询
# 偏移10条数据，返回后续5条
cursor = MetaMoment.select().offset(10).limit(5)
for record in cursor:
	print(f"id: {record.id}")

# 简单的联合查询
# 注意使用.dicts方法，将返回结果字典化
cursor = MetaMoment.select(MetaUserInfo.nickname).join(MetaUserInfo, on=(MetaUserInfo.id == MetaMoment.uid)).limit(1).dicts()
for record in cursor:
	print(f"{record}")

# 更新操作
MetaMoment.update(text = "Hello World. 12345").where(MetaMoment.id == 1).execute()
  
# 插入
# MetaMoment.create(text = "Hello World. 12345").execute()

```
参考：
* [peewee orm使用文档](http://docs.peewee-orm.com/en/latest/peewee/quickstart.html)

### http服务
http服务包含对以下框架的封装：
* Flask
  http服务框架
* Flasgger
  swagger服务框架
* prometheus_flask_exporter
  发布prometheus格式指标

举例：
```python
from binmao_libs import https
from flask import request

# post请求
@https.app.post("/hello")
def hello():
    """hello
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          required:
            - name
          properties:
            name:
              type: string
              description: name.
              default: "csj"
    response:
        200:
            description: 成功返回
            examples:
                {"state": "0", "msg": "success"}
    """
    name = request.json["name"]
    return json.dumps({"state": "0", "msg": "success", "data": {"name": name}})

https.run(application_name="binmaolibs")
```
参考：
* [flask](https://flask.palletsprojects.com/en/2.3.x/)
* [flasgger](https://github.com/flasgger/flasgger)
* [prometheus-flask-exporter](https://pypi.org/project/prometheus-flask-exporter/)

### oss服务
oss服务封装了七牛云存储对象的接口

使用举例
```python


import base_test
import qiniu
from binmao_libs.oss import OssClient

# 构建oss_client
bucket_name = ''
oss_gateway = ""
access_key = ""
secret_key = ""
oss_client = OssClient(access_key, secret_key, bucket_name)

localfile = r"d:\BaiduSyncdisk\DatasetId_1864493_1687253829.zip"
key = "models/demo/1.png"
progress_handler = lambda progress: print(f"progress: {progress}")
oss_client.upload(localfile, key, progress_handler = progress_handler)
url = oss_gateway + "/" + key
print(url)

```

### 模型文件上传/下载服务
提供中心化管理模型方案，为公司内部模型共享提供便利
#### binmao-libs.yaml
项目目录中引入binmao-libs.yaml配置
```
model:
  ftp:
    host: "192.168.9.19"
    usr: "wallan"
    pwd: "wallan1702"
```
#### 上传模型文件
```
from binmao_libs.model import download_model, upload_model
import logging
import os

models_dir = os.path.realpath(os.path.join(os.path.pardir, "models"))

logging.basicConfig(level="DEBUG")
download_model("rmbg", models_dir)
download_model("ViT-B-32", models_dir)
download_model("ViT-H-14", models_dir)
```

#### 下载模型文件
```
from binmao_libs.model import download_model, upload_model
import logging
import os

models_dir = os.path.realpath(os.path.join(os.path.pardir, "models"))
logging.basicConfig(level="DEBUG")
upload_model(os.path.join(models_dir, "rmbg"), "rmbg")
upload_model(os.path.join(models_dir, "ViT-B-32"), "ViT-B-32")
upload_model(os.path.join(models_dir, "ViT-H-14"), "ViT-H-14")
```