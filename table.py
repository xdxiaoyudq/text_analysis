# @author xiaoyu
# @date 2023/12/20
# @file table.py
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

#生成图表
def tb_generate(chart_type,keyword_counts,st):
    '''
    :param chart_type: 生成的图表类型
    :param keyword_counts: 需要展示的数据。类型为字典
    :return: 返回fig和ax对象
    '''
    fig, ax = plt.subplots()
    if chart_type == "折线图":
        plt.plot(keyword_counts.keys(), keyword_counts.values())
        plt.xlabel("关键字")
        plt.ylabel("数量")
        plt.xticks(rotation='vertical')
        plt.title("Tag Text Count Line Chart")
        st.pyplot(fig)
    elif chart_type == "饼图":
        plt.pie(keyword_counts.values(), labels=keyword_counts.keys(), autopct='%1.1f%%')
        plt.title("Tag Text Count Pie Chart")
        st.pyplot(fig)
    elif chart_type == "柱状图":
        plt.bar(keyword_counts.keys(), keyword_counts.values())
        plt.xlabel("关键字")
        plt.ylabel("数量")
        plt.xticks(rotation='vertical')
        plt.title("Tag Text Count Bar Chart")
        st.pyplot(fig)