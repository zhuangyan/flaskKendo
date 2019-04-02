# flaskKendo
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)

## 项目介绍
这个一个由后端程序员写的前后端分离示例项目．主要展示前后端分离项目的用户认证，权限管理，数据交互的方式．
虽然前后端代码都放在了一个工程中，但是前端代码都是以静态文件的方式放在static项目中的，可以完全拿出去做一个单独的项目．

## 使用方式
1)数据库
使用的是mongodb数据库,在settings.py中修改MONGO_URI为你自己的数据库连接地址．
在数据库中建立集合 user
2)python环境
~~~
pip install -r requirements.txt 
~~~
3)建立管理员账号
在项目要目录下执行
~~~
python manager.py createsuperuser
~~~
根据提示创建管理员账号
4)启动web服务
~~~
python manager.py runserver
~~~

## License
[![LICENSE](https://img.shields.io/badge/license-NPL%20(The%20996%20Prohibited%20License)-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
