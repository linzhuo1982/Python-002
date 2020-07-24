# coding:utf-8
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


# 获取maoyan.com/board页面的全部源代码
# useragent使用多过，请求到的html都是乱码，更换其他useragent值能恢复
#user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)'
user_agent = "User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Connection': 'keep-alive','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'"
header = {'user-agent': user_agent}
my_top10_url = 'https://maoyan.com/films?showType=3'


response = requests.get(my_top10_url, headers = header)
# print(response.text)
# 解析出页面的影片名称和上映时间
# 用bs功能对response的内容，使用bs4自带的解释器html.parser的方式进行解析，并引入到变量bs_info
bs_info = bs(response.text,'html.parser')
# print(bs_info)
# # 循环中使用findall方法来找指定的元素"div,并使用attrs附上属性
target = bs_info.find_all('div', attrs={'class':'movie-hover-info'})

mv_list = []
for i in target[:10]:
    mv_name = i.find('span').text
    # print(mv_name)
    cont = i.find_all('div')
    mv_type = cont[1].text.replace('\n', '').replace(' ', '')
    # print(mv_type.replace('\n', '').replace(' ', ''))
    mv_time = cont[3].text.replace('\n', '').replace(' ', '')
    # print(mv_time.replace('\n', '').replace(' ', ''))
   
    mv_list.append({'电影名称':mv_name, '电影类型':mv_type, '上映时间':mv_time})
# print(mv_list)

mv_10 = pd.DataFrame(data = mv_list)
# windows需要使用gbk字符集，不然会有乱码
mv_10.to_csv('./week1_result1.csv', encoding='utf-8', index=False, header=True)