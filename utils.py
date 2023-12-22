# @author xiaoyu
# @date 2023/12/20
# @file utils.py
def ut_get_first_n_indict(dct, n):
    # 获取字典中前n个键值对
    first_n_elements = {key: dct[key] for key in list(dct)[:n]}
    return first_n_elements