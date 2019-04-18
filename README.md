# flaskKendo
[![travis-ci.org](https://travis-ci.org/zhuangyan/flaskKendo.svg?branch=master)](https://travis-ci.org/zhuangyan/flaskKendo)
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)
[![GitHub Repo](https://img.shields.io/badge/GitHub%20Repo-%20-fff.svg?logo=GitHub&style=social)](https://github.com/zhuangyan/flaskKendo)
[![码云仓库](https://img.shields.io/badge/码云仓库-%20-fff.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAABmklEQVRIie1VS0sCYRQ9M6OOzoBWi8EgoclCK4N2vWkV/YLCFgUR1KJFEEHQok2LVgVC0J+oVSWG0YOIfkBhYAtbKAWWWpEPdGZaBGPwjTOIiBCd1b1z75xz75lv+Khbl1tBHUHXk/xvCJj0ivbhIQj+KXAeDyiL2ZAsvhvA29GJsQDFMBC3tyD4p6sZFlyPlxDQtKhtdaVqcgCAQh5IYgNTcxNaFxfUvJTOIHlwCOnjU58bQOo4aCzgGB0BzbI/iawgMjOLbOTBcPhKICyyOJ1qXHh5rokc0PrINFWOJVkNm8bH4Fpf0yVL7O0jFQwZCFQA1+0F7+vV7eH7fIRAY3+030idhkHzHICyhRTDwDk/B4bnaxfIx54Q3wkQz1smJ2Dr6gQAyLkcUde1iGYtAEVVrNsHB2B1d6j519090aO7gVkQ0H8ZhpTVmMzKwiaK6qkrJBJ4v76pTgAArGK7UQsUSUJsYxNKqUQOYvi2AYrJV0SXlpG5uNKsExukQ2GYHA5d7wFAKRaRiz4ifXYOOZ+v2Ef938kNF/gGPW5tTil3KhwAAAAASUVORK5CYII=&style=social)](https://gitee.com/arcgis2016/flaskKendo)

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
