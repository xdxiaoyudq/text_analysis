# @author xiaoyu
# @date 2023/12/20
# @file 百度指数数据.py
import gopup as gp
import streamlit as st
from datetime import date
cookie='BIDUPSID=1092D7BCB72CAEE33151E65338A4AA8A; PSTM=1698913581; ab_jid=f2551d762a80dd73f434261dbfb9f18fa570; ab_jid_BFESS=f2551d762a80dd73f434261dbfb9f18fa570; MAWEBCUID=web_EtbVjRoPcdFyYBtTqwtmibkrGybccBhhrZaQbLbhgryGgIOueU; __bid_n=18c3c7dadc445124ebcf82; ZFY=cv9ukA5jSWX5Sk5hepnMUjGfpeq8JyqmhkD1vrtVKdU:C; BDUSS=YyNkpFYnFaTTlyNGg4SjlWYmIzaU9GbS0xWmozZkpKV0tsSEZZWThneVU0YUZsSVFBQUFBJCQAAAAAAQAAAAEAAADtp~4Qz8TT6sn5OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJRUemWUVHpldH; H_PS_PSSID=39712_39817_39841_39904_39909_39936_39933_39946_39940_39939_39930_39732_39999_40012; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; bdindexid=l9readbn054san9npc5au4k846; BAIDUID=90AA7C4BF0C67610C5E1E40838D7BD08:FG=1; BAIDUID_BFESS=90AA7C4BF0C67610C5E1E40838D7BD08:FG=1; BDUSS_BFESS=YyNkpFYnFaTTlyNGg4SjlWYmIzaU9GbS0xWmozZkpKV0tsSEZZWThneVU0YUZsSVFBQUFBJCQAAAAAAQAAAAEAAADtp~4Qz8TT6sn5OAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJRUemWUVHpldH; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04530711877Ourr89GMvhzutpNvxfzuSc25TNxTjmR4Mas14PIk2XSx1MleD0AfQNCYmZhKyCDeQ%2FVgkqTnF1oOg6aNV3LKZqEDV8T8nSfGYJDvwVuz0Wq4Os8MZ74mZnjY1TU%2F%2Bq9BsnLCoR5l28PO3pbrPUt%2BuwZAy%2Fp9R%2BB6VSopZX20G6UsXm5T5Vf1kBTVNdNLl7ze0Lv%2Fc7gc%2BDmG6EFhNB%2FpkMW3n1mKogNcwdXDyppBqTRRCYmx7CrAoipC2nkhAruRAFPRdfm7WEjvDwT9ODj0yE0x1jhGY6kP5TBtE9I0c9Q%3D25365309277024382140645594657952; ab_bid=429f35b5f5e7df817bb351673324874fa85c; ab_sr=1.0.1_OGRjNjQ5MTFiMDIyMzNlM2FkMjRmMzRlNmMyY2ZhODE4YWM4ZmJlMjk3YmE4NzE3N2EyNGNiNmFiZTkwYjAyZGI0OWU2ZjllYzliYzQ5OWZjYzI5MDg2YWQ2NzcwMTQ5ZmUzNWE5OGY4ODY1NDczNDYzZjQzNmY2Yzk5YzJjOTY5MzViOWQxMzNmZTk3MjUzNjc5NmIxNGNjM2NkODEwOQ==; RT="z=1&dm=baidu.com&si=6cd3a554-ec34-4d9d-a354-c8b0ee3d0e58&ss=lqdh725z&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf'

def pa_sidebar(wide=None,hige=None):
    #侧边栏标题
    st.sidebar.title("百度指数数据")
    #侧边栏选项
    list_baidu_project=["百度搜索数据","百度咨询数据","百度媒体数据","百度人群画像年龄分别","百度人群画像性别分别","百度人群画像兴趣分别"]
    selected_option = st.sidebar.selectbox("",list_baidu_project)
    # 根据侧边栏选择显示不同的内容
    if selected_option == "百度搜索数据":
        pa_baidu_search_index(wide,hige)
    elif selected_option == "百度咨询数据":
        pa_baidu_info_index(wide,hige)
    elif selected_option == "百度媒体数据":
        pa_baidu_media_index(wide,hige)
    elif selected_option == "百度人群画像年龄分别":
        pa_baidu_age_index(wide,hige)
    elif selected_option == "百度人群画像性别分别":
        pa_baidu_gender_index(wide,hige)
    elif selected_option == "百度人群画像兴趣分别":
        pa_baidu_interest_index(wide,hige)

def pa_baidu_search_index(wide=None,hige=None):
    st.title("获取指定词语的百度搜索指数")
    word=st.text_input("输入词语","雨伞")
    start_date=st.date_input("输入初始日期",date(2023,1,1))
    end_date=st.date_input("输入截至日期",date(2023,4,1))
    df=gp.baidu_search_index(word,start_date,end_date,cookie)
    column_mapping={"date":"日期","keyword":"词语","type":"类型","index":"指数"}
    df.rename(columns=column_mapping, inplace=True)
    st.dataframe(df,wide,hige)

def pa_baidu_info_index(wide=None,hige=None):
    st.title("获取指定词语的百度资讯指数")
    word=st.text_input("输入需要查看的数据词","口罩")
    start_date=st.date_input("输入开始日期",date(2020,1,1))
    end_date=st.date_input("输入截至日期",date(2020,4,1))
    df=gp.baidu_info_index(word,start_date,end_date,cookie)
    column_mapping={"date":"日期","keyword":"词语","index":"指数"}
    df.rename(columns=column_mapping, inplace=True)
    st.dataframe(df,wide,hige)

def pa_baidu_media_index(wide=None,hige=None):
    st.title("获取指定词语的百度媒体指数")
    word=st.text_input("输入需要查看的数据词","股票")
    start_date=st.date_input("输入初始日期",date(2021,1,1))
    end_date=st.date_input("输入截至日期",date(2021,4,1))
    df=gp.baidu_media_index(word,start_date,end_date,cookie)
    column_mapping={"date":"日期","keyword":"词语","index":"指数"}
    df.rename(columns=column_mapping, inplace=True)
    st.dataframe(df,wide,hige)

def pa_baidu_age_index(wide=None,hige=None):
    st.title("获取指定词语的百度人群画像年龄分布")
    word=st.text_input("输入需要查看的数据词","股票")
    df=gp.baidu_age_index(word,cookie)
    column_mapping={"desc":"年龄范围","tgi":"TGI指数","word_rate":"关键词分布比率","all_rate":"全网分布比率","period":"周期范围"}
    df.rename(columns=column_mapping, inplace=True)
    st.dataframe(df,wide,hige)

def pa_baidu_gender_index(wide=None,hige=None):
    st.title("获取指定词语的百度人群画像性别分布")
    word=st.text_input("输入需要查看的数据词","股票")
    df=gp.baidu_gender_index(word,cookie)
    column_mapping={"desc":"年龄范围","tgi":"TGI指数","word_rate":"关键词分布比率","all_rate":"全网分布比率","period":"周期范围"}
    df.rename(columns=column_mapping, inplace=True)
    st.dataframe(df,wide,hige)



def pa_baidu_interest_index(wide=None,hige=None):
    st.title("获取指定词语的百度人群画像兴趣分布")
    word=st.text_input("输入需要查看的数据词","股票")
    df=gp.baidu_interest_index(word,cookie)
    column_mapping={"desc":"年龄范围","tgi":"TGI指数","word_rate":"关键词分布比率","all_rate":"全网分布比率","period":"周期范围"}
    df.rename(columns=column_mapping, inplace=True)
    st.dataframe(df,wide,hige)
# 运行主函数
if __name__ == '__main__':
    pa_sidebar(2000,2000)