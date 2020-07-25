# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class SpidersPipeline:
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, item, spider):
        m_name = item['m_name']
        m_type = item['m_type']
        m_time = item['m_time']
        m_list = [{'电影名称':m_name, '电影类型':m_type, '上映时间':m_time}]
        mv_10 = pd.DataFrame(data = m_list)
        # windows需要使用gbk字符集，不然会有乱码,按作业修改为utf-8
        mv_10.to_csv('./week1_result2.csv',mode = 'a', encoding='gbk', index=False, header=True)
        return item