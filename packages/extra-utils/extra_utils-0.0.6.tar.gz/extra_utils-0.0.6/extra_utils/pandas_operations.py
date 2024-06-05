"""
@Time : 2023/5/29 14:21 
@Author : skyoceanchen
@TEL: 18916403796
@项目：JYairports
@File : pandas_operations.by
@PRODUCT_NAME :PyCharm
"""
from functools import reduce

import numpy as np
import pandas as pd


class PandasOperations(object):
    @staticmethod
    def group(data: list, group_fileds: list, orient="records"):
        """
        :param data:分组数据
        :param group_filed: 分组字段
        orient : str {'dict', 'list', 'series', 'split', 'records', 'index'}
            Determines the type of the values of the dictionary.

            - 'dict' (default) : dict like {column -> {index -> value}}  {'DD001': {'post_construction_settlement': {2: -1.248, 5: -1.664, 8: -2.08, 11: -1.664, },'DD002': {'post_construction_settlement': {2: -1.248, 5: -1.664, 8: -2.08, 11: -1.664, },}
            - 'list' : dict like {column -> [values]} {'DD001': {'post_construction_settlement': [-1.248, -1.664, -2.08, -1.664,]},'DD002': {'post_construction_settlement': [-1.248, -1.664, -2.08, -1.664,]}}
            - 'series' : dict like {column -> Series(values)}
            - 'split' : dict like
              {'index' -> [index], 'columns' -> [columns], 'data' -> [values]}
            - 'records' : list like
              [{column -> value}, ... , {column -> value}]
            - 'index' : dict like {index -> {column -> value}}

            Abbreviations are allowed. `s` indicates `series` and `sp`
            indicates `split`.
        :return:
        """
        # g = pd.DataFrame(data).groupby(['get_time'])
        g = pd.DataFrame(data).groupby([*group_fileds])
        dic = {}
        for k, v in g:
            if len(k) == 1:
                dic[k[0]] = v.to_dict(orient)
            else:
                dic[k] = v.to_dict(orient)
        return dic

    @staticmethod
    def group_size(p_data: list, group_fileds: list, orient="records"):
        #   dic = pd.DataFrame(obj_lis).groupby("day")['value'].mean().round(2)
        data = {
            "amount": 0,
            "on_line": 0,
            "off_line": 0
        }
        p_data = [{"if_survive": 1}, {"if_survive": 1}, {"if_survive": 1}]
        g = pd.DataFrame(p_data).groupby(["if_survive"]).size()  # .sort_values(ascending=True)
        dic = g.to_dict()
        on_line = dic.get(1) if dic.get(1) else 0
        off_line = dic.get(0) if dic.get(0) else 0
        data['amount'] = on_line + off_line
        data['on_line'] = on_line
        data['off_line'] = off_line

    # <editor-fold desc="列最大值所在的行">
    @staticmethod
    def max_columns(data: list, filed, orient):
        pf = pd.DataFrame(data)
        return pf[pf[filed] == pf[filed].max()].to_dict()

    # </editor-fold>
    # <editor-fold desc="列最小值所在的行">
    @staticmethod
    def min_columns(data: list, filed, orient):
        pf = pd.DataFrame(data)
        return pf[pf[filed] == pf[filed].min()].to_dict()

    # </editor-fold>
    # <editor-fold desc="连接表">
    def many_merge(self, dfs, how='inner', on=None, left_on=None, right_on=None,
                   left_index=False, right_index=False, sort=True, suffixes=('_x', '_y'),
                   copy=True, indicator=False, validate=None):  # 多表合并
        """
        left、right:需要连接的两个DataFrame或Series，一左一右
        how:两个数据连接方式，默认为inner，可设置inner、outer、left或right
        on:作为连接键的字段，左右数据中都必须存在，否则需要用left_on和right_on来指定
        left_on:左表的连接键字段
        right_on:右表的连接键字段
        left_index:为True时将左表的索引作为连接键，默认为False
        right_index:为True时将右表的索引作为连接键，默认为False
        suffixes:如果左右数据出现重复列，新数据表头会用此后缀进行区分，默认为_x和_y
        df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],'A': ['A0', 'A1', 'A2', 'A3'],'B': ['B0', 'B1', 'B2', 'B3']})
        df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],  'C': ['C0', 'C1', 'C2', 'C3'],'D': ['D0', 'D1', 'D2', 'D3']})
        df3 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],  'E': ['E0', 'E1', 'E2', 'E3'],   'F': ['F0', 'F1', 'F2', 'F3']})
        dfs = [df1,df2,df3]
        """

        df_final = reduce(lambda left, right: pd.merge(left, right, how=how, on=on), dfs)
        df_final = df_final.fillna(method='ffill')  ## 使用前一个值进行填充
        df_final = df_final.fillna(method='bfill')  # 后向填充此时无效
        # columns = df_final.columns
        return df_final

    # </editor-fold>
    # <editor-fold desc="合并表">
    def concat(self, dfs):
        # return pd.concat([df1, df2,df1, df2])
        result = pd.concat(dfs)
        result = result.reset_index()
        result.pop('index')
        return result

    # </editor-fold>
    # <editor-fold desc="n取1-行">
    def partition_n_of_1(self, df, step, start=None, end=None, ):
        """
        :param df:
        :param step:取值 m 个
        :param start:
        :param end:
        :return:
        """
        if start and end:
            result = df.iloc[start:end:step]
        elif start:
            result = df.iloc[start::step]
        elif end:
            result = df.iloc[:end:step]
        else:
            result = df.iloc[::step]
        result = result.reset_index()
        result.pop('index')
        return result

    # </editor-fold>
    # <editor-fold desc="pf查询">
    def pd_query(self, df, query):
        # 需要选取每隔4行的数据，可以按照如下方式实现：
        # every_fourth_row = df.query('index % 4 == 0')
        # data.query('index >= 0 and index <= 5')  # 第1-6行
        # result =data.query('index >= 7 and index <= 11')  # 第8-12行
        result = df.query(query)  # 第8-12行
        result = result.reset_index()
        result.pop('index')
        return result

    # </editor-fold>
    # <editor-fold desc="去重">
    def drop_duplicates(self, pf, subset=['number'], keep='last', inplace=True):
        """
        参数说明如下：
        subset：表示要进去重的列名，默认为 None。
        keep：有三个可选参数，分别是 first、last、False，默认为 first，表示只保留第一次出现的重复项，删除其余重复项，
        last 表示只保留最后一次出现的重复项，False 则表示删除所有重复项。
        inplace：布尔值参数，默认为 False 表示删除重复项后返回一个副本，若为 Ture 则表示直接在原数据上删除重复项。
        """
        pf.drop_duplicates(subset=subset, keep=keep, inplace=inplace)
        return pf

    # </editor-fold>
    # <editor-fold desc="替换全部为0的列为前一列的值">
    def null_ffill(self, df, value=0):
        """
        df = pd.DataFrame({
            'A': [0, 1, 0, 2],
            'B': [0, 0, 0, 0],
            'C': [0, 0, 0, 0],
            'D': [0, 0, 0, 0]
        })
        """
        df.replace(value, np.nan, inplace=True)
        # axis=0表示在垂直方向填充(axis值：0为垂直，1为水平),
        df = df.fillna(method='ffill', axis=1)
        # # 找出全部为0的列
        # all_zero_cols = df.columns[df.eq(value).all()]
        # # 替换全部为0的列为前一列的值
        # for col in all_zero_cols:
        #     prev_col = df.columns.get_loc(col) - 1
        #     df[col] = df.iloc[:, prev_col]
        #
        return df
    # </editor-fold>

# data = {
#     'Name': ['Tom', 'Tom', 'Mary', 'Mary', 'John', 'John', 'John'],
#     'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'History'],
#     'Score': [80, 90, 85, 95, 90, 85, 75]
# }
