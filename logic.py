# @author xiaoyu
# @date 2023/12/20
# @file logic.py
import data
import re
from collections import Counter
import jieba
def del_key_web_word(url):
    """
    :param url: 网站的网站
    :return: 以字典的形式返回网站中出现次数前30的关键词
    """
    text=data.getdata_base_text(url)
    # 去除标点符号
    pattern = re.compile("[^\u4e00-\u9fa5a-zA-Z0-9]")
    text_without_punctuation = re.sub(pattern, "", text)
    # 使用 jieba 分词
    words = jieba.lcut(text_without_punctuation)
    # 筛选长度为二到五个字的词语
    filtered_words = [word for word in words if 2 <= len(word) <= 5]
    #统计
    word_count = Counter(filtered_words)
    #取前30个词语
    top_words = word_count.most_common(30)
    keywords = dict(top_words)
    return keywords

def del_key_self_word(url,st):
    '''
    :param url: 用户输入的地址
    :param st: streamlit对象st
    :return:
    '''
    #返回的字典
    item_counts = {}
    #输入
    key_ower = st.text_input("输入自己需要的关键词(可以以逗号、空格分开)")
    #除去逗号 空格
    items = re.split(r'[,，\s]+', key_ower)
    #过滤掉原始列表 items 中的空字符串元素，并且将每个非空元素两端的空白字符去除
    items = [item.strip() for item in items if item.strip()]
    #得到原始数据
    text = data.getdata_base_text(url)
    # 遍历列表中的每个元素
    for item in items:
        # 使用 count() 方法统计元素在文本中出现的次数，并存储到字典中
        item_counts[item] = text.lower().count(item.lower())
    return item_counts




