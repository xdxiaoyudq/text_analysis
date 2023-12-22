# @author xiaoyu
# @date 2023/12/20
# @file 网页关键词分析.py
import logic
import table
import utils
import streamlit as st

#主函数
def pa_keyword_analysis():
    # 设置页面标题
    st.title("网页关键词分析")
    # 添加文本输入框，让用户输入URL
    url = st.text_input("输入网址", "https://www.gov.cn/xinwen/2022-10/25/content_5721685.htm")
    # 添加下拉框，让用户选择图表类型
    chart_type = st.selectbox("Select Chart Type", ["折线图", "饼图", "柱状图"])
    keywords=logic.del_key_web_word(url)
    # 创建一个多选下拉菜单
    keys_list = list(keywords.keys())
    selected_options = st.multiselect(
        "选择你想要分析的关键词:",
        keys_list
    )
    #用户自己输入关键词
    dict2=logic.del_key_self_word(url,st)
    # 添加按钮，点击后进行统计和绘图
    if st.button("分析"):
        dict1={option: keywords.get(option) for option in selected_options if option in keywords}
        dict={key: value for d in [dict1, dict2] for key, value in d.items()}#合并字典1和字典2
        if not dict:
            dict = utils.ut_get_first_n_indict(keywords, 8)
        table.tb_generate(chart_type,dict,st)
# 运行主函数
if __name__ == '__main__':
    pa_keyword_analysis()