import csv
import os
import re

from django.core.wsgi import get_wsgi_application
from openpyxl import load_workbook
from system.utils.configread import config_read
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
application = get_wsgi_application()
import django
django.setup()

# 数据读取，数据清理，并写入DB
# 获取files目录下的所有.xlsx文件名
from business.models import Category, Topics, Topicstags, Tags

directory = 'files'  # 指定目录
for filename in os.listdir(directory):
    if filename.endswith(".csv"):  # 仅处理CSV文件
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)

            name = filename[:-4]

            # 取出分类ID
            category, created = Category.objects.get_or_create(name=name)
            if created:
                print("插入分类成功！")
            else:
                print('分类已存在')

            for row in reader:
                # 标题
                title = row[0]
                # 关键字
                keywords = row[1]
                print('文件名:', filename)
                print('标题:', title)
                print('关键字:', keywords)

                # 写入选题表
                topics, created = Topics.objects.get_or_create(
                    category_id=category.id,
                    name=title,
                    content=title
                )

                # 绑定选题标签
                keywords_list = eval(keywords)

                for keyword in keywords_list:
                    # 插入标签
                    tags, created = Tags.objects.get_or_create(
                        name=keyword
                    )
                    # 插入选题和标签关系表
                    Topicstags.objects.get_or_create(
                        topics_id=topics.id,
                        tags_id=tags.id
                    )

    else:
        continue