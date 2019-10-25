# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os


class CeshiPipeline(object):

    def process_item(self, item, spider):
        curPath = 'D:\全书网小说'
        tempPath = str(item['name'])
        targetPath = curPath + os.path.sep + tempPath
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)

        filename_path = 'D:\全书网小说' + os.path.sep + str(item['name']) + os.path.sep + str(item['chapter_name']) + '.txt'
        with open(filename_path, 'w', encoding='utf-8') as f:
            f.write(item['chapter_content'] + "\n")
        return item
