# @author xiaoyu
# @date 2023/12/20
# @file data.py
#输入url 爬虫获取文本对象
import requests
from bs4 import BeautifulSoup
def getdata_base_text(url):
    """
    :param url: 浏览器地址
    :return: 以字符串的形式返回一个文本
    """
    response = requests.get(url)
    encoding = response.encoding if 'charset' in response.headers.get('content-type', '').lower() else None
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding=encoding)
    text = soup.get_text()
    return text



