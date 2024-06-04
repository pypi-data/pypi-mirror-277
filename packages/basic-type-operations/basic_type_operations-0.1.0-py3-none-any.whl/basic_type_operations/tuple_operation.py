# -*- coding:utf-8 -*-
"""
@Time : 2023/3/29
@Author : skyoceanchen
@TEL: 18916403796
@File : tuple_operation.py 
@PRODUCT_NAME : PyCharm 
"""


# <editor-fold desc="元组操作">
class TupleOperation(object):
    @staticmethod
    # def tuple_to_list_key(data, key1, key2=None):
    def tuple_to_list_key(data, *args):
        lis = []
        for li in data:
            lens = len(li)
            obj = {}
            for i in range(lens):
                obj[args[i]] = li[i]
            lis.append(obj)
        return lis

    @staticmethod
    def tuple_to_dict_key(data):
        return dict(data)

    @staticmethod
    def tuple_to_dict_of_key(data, value):
        dic = {}
        for k, v in data:
            dic[v] = k
        return dic.get(value)

    @staticmethod
    def tuple_to_dict_of_value(data, key):
        dic = {}
        for k, v in data:
            dic[k] = v
        return dic.get(key)
# </editor-fold>
