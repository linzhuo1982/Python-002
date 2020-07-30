# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql as pms


results =[]
class Week2ProxyPipeline:
    def process_item(self, item, spider):
        result = item['result']
        # print(result)
        sql = 'INSERT into week2_proxy1(proxy) VALUES ("' + result + '")'
        # print(sql)
        # sql = 'select VERSION()'
        conn = pms.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'rootroot',
            db = 'geek_practice',
            charset = 'utf8'
            )
        cur = conn.cursor()
        try:
            cur.execute(sql)
            results.append(cur.fetchone())
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        conn.close()

