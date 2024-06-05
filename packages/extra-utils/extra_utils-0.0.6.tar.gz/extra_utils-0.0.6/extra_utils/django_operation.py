# -*- coding:utf-8 -*-
"""
@Time : 2023/3/24
@Author : skyoceanchen
@TEL: 18916403796
@File : django_operation.py 
@PRODUCT_NAME : PyCharm 
"""

import datetime as dt
import json
import re

import pandas as pd
from basic_type_operations.date_operation import DateOperation
from django.apps import apps
from django.contrib import messages
from django.contrib.auth.hashers import make_password as mk_password, check_password as ch_password
from django.core.exceptions import ValidationError
from django.db import connection, connections
from django.db.models import Aggregate, CharField
from django.db.models import Count
from django.db.models import Q
from django.db.models.functions import ExtractMonth, ExtractYear
from django.forms.models import model_to_dict as model_dict
from django.utils.translation import gettext_lazy as _


# <editor-fold desc="自定义分组函数">
class Concat(Aggregate):
    """ORM用来分组显示其他字段 相当于group_concat"""
    function = 'GROUP_CONCAT'
    template = "%(function)s(%(delimit)s,%(distinct)s %(expressions)s,%(delimit)s ORDER BY %(order_by)s ASC)"

    def __init__(self, expression, distinct=False, delimit="\"'\"", order_by="''", **extra):
        super(Concat, self).__init__(
            expression,
            distinct='DISTINCT ' if distinct else '',
            delimit=delimit,
            order_by=order_by,
            output_field=CharField(),
            **extra)

    """
    list_raw = EarlyWarning.objects.filter() \
    .extra(select={create_time: f"DATE_FORMAT({create_time}, '%%Y-%%m-%%d')"}).values('create_time').annotate(
    all_value1=Concat(create_time)).order_by("-create_time").values_list("all_value1",
                                                                                                  'create_time', 'car',
                                                                                                  )
    """


# </editor-fold>


class DjangoOrmSelectOperation(object):
    @staticmethod
    def dataformat_y(file, as_file=None):
        if not as_file:
            as_file = file
        select = {as_file: f'DATE_FORMAT({file}, "%%Y")'}  # 格式化时间
        return select

    @staticmethod
    def dataformat_ym(file, as_file=None):
        if not as_file:
            as_file = file
        select = {as_file: f'DATE_FORMAT({file}, "%%Y-%%m")'}  # 格式化时间
        return select

    @staticmethod
    def dataformat_ymd(file, as_file=None):
        if not as_file:
            as_file = file
        #     {'file': 'DATE(file)'},
        select = {as_file: f'DATE_FORMAT({file}, "%%Y-%%m-%%d")'}  # 格式化时间
        return select

    @staticmethod
    def dataformat_ymdh(file, as_file=None):
        if not as_file:
            as_file = file
        select = {as_file: f'DATE_FORMAT({file}, "%%Y-%%m-%%d %%H")'}  # 格式化时间
        return select

    @staticmethod
    def dataformat_ymdhm(file, as_file=None):
        if not as_file:
            as_file = file
        select = {as_file: f'DATE_FORMAT({file}, "%%Y-%%m-%%d %%H:%%i")'}  # 格式化时间
        return select

    @staticmethod
    def dataformat_ymdhms(file, as_file=None):
        if not as_file:
            as_file = file
        select = {as_file: f'DATE_FORMAT({file}, "%%Y-%%m-%%d %%T")'}  # 格式化时间
        return select

    @staticmethod
    def dataformat_hm(file, as_file=None):
        if not as_file:
            as_file = file
        select = {as_file: f'DATE_FORMAT({file}, "%%H:%%i")'}  # 格式化时间
        return select

    @staticmethod
    def round(file, as_file=None, keep_decimal=2, ):
        if not as_file:
            as_file = file
            # 'abs': 'round(abs,2)'
        select = {as_file: f'round({file},{keep_decimal})'}
        return select

    @staticmethod
    def round_list(file_list, as_file=None, keep_decimal=2):
        select = {}
        if as_file:
            if len(file_list) != len(as_file):
                return None
        for i in range(len(file_list)):
            if as_file:
                as_files = as_file[i]
            else:
                as_files = file_list[i]
            select.update({as_files: f'round({file_list[i]},{keep_decimal})'})
        return select

    @staticmethod
    def file_as(file, as_file=None, ):
        if not as_file:
            as_file = file
        select = {as_file: f'{file}'}
        return select

    # <editor-fold desc="按天分组">
    @staticmethod
    def day_group_count_many(model, date_field="create_time", value=['id', ], data_type=Count, **kwargs, ):
        """
        :param model: 模块
        :param field:
        :param kwargs:
        :return:
        """
        many_kwargs = {}
        for index, v in enumerate(value):
            many_kwargs[v] = data_type(v)
        # select = {'day': connection.ops.date_trunc_sql('day', date_field)}
        select = DjangoOrmSelectOperation.dataformat_ymd(date_field, 'day')
        count_data = model.objects.filter(
            **kwargs,
            # create_time__year=this_year,
            # create_time__month=this_month
        ).extra(
            select=select).values('day').annotate(**many_kwargs)
        count_data = pd.DataFrame(count_data).to_dict("list")
        XAxis = count_data.get('day')
        if not XAxis:
            XAxis = []
        if len(value) == 1:
            YAxis = count_data.get(value[0])
            if not YAxis:
                YAxis = []
            data = {"XAxis": XAxis, "YAxis": YAxis}
        else:
            data = {}
            for index, v in enumerate(value):
                YAxis = count_data.get(v)
                if not YAxis:
                    YAxis = []
                data[v] = {
                    "XAxis": XAxis,
                    "YAxis": YAxis
                }
        return data

    @staticmethod
    def day_group_count_many_other(model, date_field="create_time", group_field="sign", group_field_dic={}, value=[],
                                   data_type=Count, **kwargs, ):
        """
        :param model: 模块
        :param field:
        :param kwargs:
        :return:
        """
        many_kwargs = {}
        for index, v in enumerate(value):
            many_kwargs[v] = data_type(v)
        # select = {'day': connection.ops.date_trunc_sql('day', date_field)}
        select = DjangoOrmSelectOperation.dataformat_ymd(date_field, 'day')
        count_data = model.objects.filter(
            **kwargs,
            # create_time__year=this_year,
            # create_time__month=this_month
        ).extra(
            select=select).values('day', group_field).annotate(**many_kwargs).order_by(date_field)
        count_data_g = pd.DataFrame(count_data).groupby([group_field])
        count_data_dic = {}
        for k, v in count_data_g:
            count_data_dic[k] = v.to_dict("list")
        keys_lis = list(count_data_dic.keys())
        data = {}
        for key in keys_lis:
            XAxis = count_data_dic.get(key).get('day')
            YAxis = count_data_dic.get(key).get(value[0])
            if not XAxis:
                XAxis = []
            if not YAxis:
                YAxis = []
            data[group_field_dic.get(key)] = {
                "XAxis": XAxis,
                "YAxis": YAxis,
            }
        return data

    # </editor-fold>
    # <editor-fold desc="按月分组">
    @staticmethod
    def mouth_group_count_many(model, date_field="create_time", value=['id', ], data_type=Count, **kwargs, ):
        many_kwargs = {}
        for index, v in enumerate(value):
            many_kwargs[v] = data_type(v)
        count_res = model.objects.filter(
            **kwargs
            # create_time__gte=time_ago
        ).annotate(
            year=ExtractYear(date_field),
            month=ExtractMonth(date_field)) \
            .values('year', 'month').order_by('year', 'month').annotate(**many_kwargs)
        # 封装数据格式
        data = {}
        if not count_res:
            if len(value) == 1:
                data = {"XAxis": [], "YAxis": []}
            else:
                for index, v in enumerate(value):
                    data[v] = {
                        "XAxis": [],
                        "YAxis": []
                    }
            return data
        count_data = pd.DataFrame(count_res).to_dict("list")
        year_list = count_data.get("year")
        XAxis = ["%s-%s" % (year_list[index], month) for index, month in enumerate(count_data.get('month'))]
        if not XAxis:
            XAxis = []
        if len(value) == 1:
            YAxis = count_data.get(value[0])
            if not YAxis:
                YAxis = []
            data = {"XAxis": XAxis, "YAxis": YAxis}
        else:
            for index, v in enumerate(value):
                YAxis = count_data.get(v)
                if not YAxis:
                    YAxis = []
                data[v] = {
                    "XAxis": XAxis,
                    "YAxis": YAxis
                }

        return data

    @staticmethod
    def mouth_group_count_many_other(model, date_field="create_time", group_field="sign", group_field_dic={}, value=[],
                                     data_type=Count, **kwargs, ):
        """
        :param model: 模块
        :param field:
        :param kwargs:
        :return:
        """
        many_kwargs = {}
        for index, v in enumerate(value):
            many_kwargs[v] = data_type(v)
        # select = {'day': connection.ops.date_trunc_sql('day', date_field)}
        select = DjangoOrmSelectOperation.dataformat_ymd(date_field, 'day')
        count_data = model.objects.filter(
            **kwargs,
            # create_time__year=this_year,
            # create_time__month=this_month
        ).annotate(year=ExtractYear(date_field),
                   month=ExtractMonth(date_field)) \
            .values('year', 'month', group_field).order_by('year', 'month').annotate(**many_kwargs)
        count_data_g = pd.DataFrame(count_data).groupby([group_field])

        count_data_dic = {}
        for k, v in count_data_g:
            count_data_dic[k] = v.to_dict("list")
        keys_lis = list(count_data_dic.keys())
        data = {}
        for key in keys_lis:
            year_list = count_data_dic.get(key).get("year")
            XAxis = ["%s-%s" % (year_list[index], month) for index, month in
                     enumerate(count_data_dic.get(key).get('month'))]
            YAxis = count_data_dic.get(key).get(value[0])
            if not XAxis:
                XAxis = []
            if not YAxis:
                YAxis = []
            data[group_field_dic.get(key)] = {
                # "XAxis": count_data_dic.get(key).get('day'),
                "XAxis": XAxis,
                "YAxis": YAxis
            }
        return data

    # </editor-fold>
    # </editor-fold>
    # <editor-fold desc="按照每日时间格式化分组求个数">
    @staticmethod
    def date_group(obj, create_time):
        # '%%Y-%%m-%%d %%H:%%i:%%s'
        return obj.objects.filter() \
            .extra(select={create_time: f"DATE_FORMAT({create_time}, '%%Y-%%m-%%d')"}).values(create_time).annotate(
            num=Count(create_time))

    # </editor-fold>
    # <editor-fold desc="针对一个对象的数据进行json化">
    @staticmethod
    def model_to_dict(obj):
        return model_dict(obj)

    # </editor-fold>
    # <editor-fold desc="创造密码">
    @staticmethod
    def make_password(password):
        pwd = mk_password(password)
        return pwd

    # </editor-fold>
    # <editor-fold desc="核对密码">
    @staticmethod
    def check_password(old_password, password):
        return ch_password(old_password, password)

    # </editor-fold>
    # <editor-fold desc="用户验证-密码">
    @staticmethod
    def user_check_password(user_obj, password):
        return user_obj.check_password(password)

    # </editor-fold>
    # <editor-fold desc="设置-密码">
    @staticmethod
    def user_set_password(user_obj, password):
        return user_obj.set_password(password)

    # </editor-fold>

    def Q_or(self, qwargs):
        """
        qwargs = {
        'username':"小王",
        'truename':"小王",
        ...
        }
        q = Q()
        q1.connector = 'OR'              #连接方式
        q1.children.append(('id', 1))
        q1.children.append(('id', 2))
        q1.children.append(('id', 3))

        """
        # 模糊查询
        q = Q()
        # q.connector
        for i in qwargs:
            q.add(Q(**{i: qwargs[i]}), Q.OR)
        return q

    def Q_and(self, qwargs):
        """
        qwargs = {
        'username':"小王",
        'truename':"小王",
        ...
        }
        """
        # 模糊查询

        q = Q()
        for i in qwargs:
            q.add(Q(**{i: qwargs[i]}), Q.AND)
        return q

    def Q_XOR(self, qwargs):
        """
        qwargs = {
        'username':"小王",
        'truename':"小王",
        ...
        }
        """
        # 模糊查询

        q = Q()
        for i in qwargs:
            q.add(Q(**{i: qwargs[i]}), Q.XOR)
        return q

    def Q_many(self, qs: list, connector=Q.AND):
        """
        qs:多个q对象，[Q(),Q(),Q()]
        """
        con = Q()
        for q in qs:
            con.add(q, connector)
        return con

    def Q_children(self, data, connector=Q.AND):
        """
        data = ('id', 1), ('id', 2), ('id', 3)
        """
        q = Q()
        q.connector = connector  # 连接方式
        for dat in data:
            q.children.append(dat)
        return q


class DjangoConnectOperation(object):
    def __init__(self, db_alias="default"):
        self.conn = connections[db_alias]
        self.cursor = self.conn.cursor()

    def dictfetchall(self):
        """
            以字典格式返回数据
        :param cursor:
        :return:
        """
        desc = self.cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in self.cursor.fetchall()
        ]

    def query_dict(self, sql, params: list):
        """
            手动查询sql
        :param sql:
        :param params:
        :return:

        res = TKConnect('postgis').query(" select * from light ", [])
        """
        with  self.cursor:
            self.cursor.execute(sql, params)
            result = self.dictfetchall()
        return result

    def query(self, sql, params):
        """    # 执行原生语句，查询所有分组的数据
        sql_select = '''select number, group_concat(get_time),group_concat(`value`),group_concat(rain_value)
        from gw_waterlevelgauge where runway='%s' and get_time >= '%s' and get_time<= '%s' group by number;''' % (
        runway, date_start, date_end)
        :param sql_select:
        :return:
        """

        """
        :param sql: sql语句
        :param params: 替换参数  (par1,par2)
        :return: 列表
        """
        """
        max()：最大值
        min()：最小值
        avg()：平均值
        sum()：和
        count()：记数
        group_concat()：组内字段拼接，用来查看组内其他字段
        升序：order by 字段名  asc
        降序：order by 字段名 desc
        多个排序条件：order by 字段名 asc,字段名 desc
        限制 limit
        limit 1; 查询一条
        limit 5,3;  # 先偏移5条满足条件的记录，再查询3条
        """
        # 查询
        # 单个分组查询
        # """SELECT id,endMark,createTime,KValue,PCN FROM DynamicStrainometertableFiveFun where createTime>=%s AND createTime<%s GROUP BY endMark ORDER BY createTime;"""
        # 分组查询最大值，最小值，平均值
        # """SELECT location, MAX(desiredValue),AVG(desiredValue) FROM DynamicStrainometertableTwo GROUP BY location ORDER BY -createTime limit 30;""")
        # 分组查询这一组的所有数据
        # """SELECT horizon,group_concat(createTime),group_concat(avgTemValue) FROM ThermometerTableTwo  where createTime>=%s AND createTime<%s  group by horizon""",
        # 更新
        # UPDATE project_device as t SET t.roadsection_id = %s WHERE t.id =%s AND (T.roadsection_id != %s OR T.roadsection_id IS NULL)
        #             """, [int(roader_id), int(device_id), int(roader_id)])
        with  self.cursor:
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
        return result

    # <editor-fold desc="修改表名">
    def alter_table_name(self, old_name, new_name):
        self.cursor.execute(f"alter table {old_name} rename {new_name};")
        self.cursor.fetchall()

    # </editor-fold>
    # <editor-fold desc="复制表结构">
    def copy_table_structure(self, new_name, old_name, ):
        self.cursor.execute(f"CREATE TABLE {new_name} LIKE {old_name};")
        self.cursor.fetchall()

    # </editor-fold>
    '''
        connect = DjangoConnectOperation()
        connect.alter_table_name('pavement_surface_status','pavement_surface_status_2', )
        connect.copy_table_structure('pavement_surface_status','pavement_surface_status_2', )
        connect.close()
    '''

    def get_day_range_tables(self, date_start, date_end, table):
        """
            start_day 开始日期
            end_day   结束日期
            return: List
                例：['2016-10-01','2016-10-02',....]
        """
        date_list = DateOperation().get_day_range(date_start, date_end)
        now_s = dt.datetime.now().strftime('%Y%m%d')
        tables = []
        for mouth in date_list:
            if mouth == now_s:
                tables.append(table)
            else:
                tables.append(f'{table}_{mouth}')
        return tables

    # 查多表返回数据
    def get_response_data(self, date_start, date_end, table, number, if_damage, all_tables_row='Tables_in_jialiu_pro'):
        tables = self.get_day_range_tables(date_start, date_end, table)
        if date_start and date_end:
            sql = f"""SELECT DATE_FORMAT(create_time, "%Y-%m-%d %T") as create_time,`value`,`number`   FROM {table} where
                            create_time>'{date_start}' and create_time<'{date_end}' and number = '{number}' and if_damage={if_damage}  order by create_time """
        elif date_start:
            sql = f"""SELECT DATE_FORMAT(create_time, "%Y-%m-%d %T") as create_time,`value`,`number`   FROM {table} where
                        create_time>'{date_start}' and number = '{number}' and if_damage={if_damage}  order by create_time """
        elif date_end:
            sql = f"""SELECT DATE_FORMAT(create_time, "%Y-%m-%d %T") as create_time,`value`,`number`   FROM {table} where
                            create_time<'{date_end}' and number = '{number}' and if_damage={if_damage}  order by create_time """
        else:
            sql = f"""SELECT DATE_FORMAT(create_time, "%Y-%m-%d %T") as create_time,`value`,`number`   FROM {table} where
                                and number = '{number}' and if_damage={if_damage}  order by create_time """
        pfs = []
        table_pd = list(pd.read_sql('show tables;', con=connection)[all_tables_row])
        for now_table in tables:
            if now_table in table_pd:
                now_sql = sql.replace(table, now_table)
                pf = pd.read_sql(now_sql, con=connection)
                pfs.append(pf)
        result = pd.concat(pfs)
        result = result.reset_index()
        result.pop('index')
        yAxis = result['value'].round(2)
        xAxis = result['create_time'].values.tolist()
        maxvalue = yAxis.max()
        minvalue = yAxis.min()
        data = {
            'number': number,
            'maxvalue': maxvalue,
            'minvalue': minvalue,
            'time_range': f"{xAxis[0]} - {xAxis[-1]}",
            'xAxis': xAxis,
            'yAxis': yAxis
        }
        return data

    # 查询单表数据返回
    def get_response_data_type2(self, kwargs, date_start, date_end, table, number, if_damage):
        if not date_start and not date_end:
            firstDay, lastDay = DateOperation.month_top_tail()
            kwargs['create_time__range'] = (firstDay, lastDay - dt.timedelta(days=1))
        if date_end:
            kwargs['create_time__lte'] = date_end - dt.timedelta(days=1)
        kwargs.pop('if_damage')
        select = {'create_time': connection.ops.date_trunc_sql('day', 'create_time')}
        obj = table.objects.filter(**kwargs, ).extra(
            select=select).values('value', 'create_time', 'number', ).order_by('create_time')
        if obj:
            pf = pd.DataFrame(obj)
            yAxis = pf['value'].round(2)
            maxvalue = yAxis.max()
            minvalue = yAxis.min()
            xAxis = pf['create_time'].values.tolist()
            data = {
                'number': number,
                'maxvalue': maxvalue,
                'minvalue': minvalue,
                'time_range': f"{xAxis[0]} - {xAxis[-1]}",
                'xAxis': xAxis,
                'yAxis': yAxis
            }
        else:
            data = {
                'number': number,
                'maxvalue': 0,
                'minvalue': 0,
                'time_range': 0,
                'xAxis': [],
                'yAxis': []
            }
        return data

    def close(self):
        self.cursor.close()
        self.conn.close()


class DjangoErrorOperation(object):
    @staticmethod
    def django_obj_error(obj):
        errors_dic = obj.errors.as_json()
        errors_dic: dict = json.loads(errors_dic)
        keys = list(errors_dic.keys())
        values = list(errors_dic.values())
        error = str()
        for index, key in enumerate(keys):
            error += key
            error += ':'
            for value in values[index]:
                error += value.get('message')
            error += '\t'
        return error


class DjangoMessageOperation(object):
    # 你可以使用add_message()方法创建新的messages或用以下任意一个快捷方法：
    # • success()：当操作成功后显示成功的messages
    # • info()：展示messages
    # • warning()：某些还没有达到失败的程度但已经包含有失败的风险，警报用
    # • error()：操作没有成功或者某些事情失败
    # • debug()：在生产环境中这种messages会移除或者忽略
    # 让我们显示messages给用户。。因为messages框架是被项目全局应用，我们可以在主模板（template）给用户展示messages。
    # 打开base.html模板（template）在id为header的<div>和id为content的<div>之间添加

    # messages框架带有一个上下文环境（context）处理器用来添加一个messages变量给请求的上下文环境（context）。
    # 所以你可以在模板（template）中使用这个变量用来给用户显示当前的messages。
    # 现在，让我们修改edit视图（view）来使用messages框架。编辑应用中的views.py文件，edit视图（view）
    @staticmethod
    def message_error(request, msg):
        messages.error(request, msg)

    @staticmethod
    def message_success(request, msg):
        messages.success(request, msg)

    @staticmethod
    def message_info(request, msg):
        messages.info(request, msg)

    @staticmethod
    def message_warning(request, msg):
        messages.warning(request, msg)

    @staticmethod
    def message_debug(request, msg):
        messages.debug(request, msg)


class DjangoOrmValidateOperation(object):
    # <editor-fold desc="偶数验证">
    @staticmethod
    def validate_even(value):
        if value % 2 != 0:
            raise ValidationError(
                _('%(value)s is not an even number'),
                params={'value': value},
            )

    # </editor-fold>
    @staticmethod
    def validate_decimals(value):
        try:
            return round(float(value), 3)
        except:
            raise ValidationError(
                _('%(value)s is not an integer or a float  number'),
                params={'value': value},
            )

    @staticmethod
    def person_id_validator(value):
        """
        对用户身份证进行自定义验证
        :param value:验证的字段值
        :return:身份格式不正确
        """
        ID_compile = re.compile(r'([A-Za-z](\d{6})\(\d\))|(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X|x)$')
        if not ID_compile.match(value):
            raise ValidationError(u"身份证格式不正确")

    @staticmethod
    def zip_code_validator(value):
        """
        对邮政编码进行自定义验证
        :param value: 验证的字段值
        :return:邮政编码格式不正确
        """
        zip_code = re.compile('^[0-9]\\d{5}$')
        if not zip_code.match(value):
            raise ValidationError(u"邮政编码格式不正确")

    @staticmethod
    def password_validator(value):
        """
        对密码进行自定义验证
        :param value: 验证的字段值
        :return:以字母开头，长度在6~18之间，只能包含字符、数字和下划线
        """
        password = re.compile('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z_]{8,16}$')
        if not password.match(value):
            raise ValidationError(u'以字母开头，长度在6~18之间，只能包含字符、数字和下划线')

        # models

    # password = models.CharField(validators=[password_validator], max_length=100, verbose_name=u'密码', null=True, blank=True)
    # zip_code = models.CharField(validators=[zip_code_validator], max_length=50, verbose_name=u'邮政编码', null=True, blank=True)


class DjangoAppsModelsOperation(object):
    def app_models(self, app):
        data = []
        for model, value in apps.get_app_config(app).models.items():
            class_name = value.__name__
            verbose_name = apps.get_app_config(app).get_model(class_name)._meta.verbose_name  # 获取models的名称
            data.append({
                class_name: verbose_name
            })
        return data

    def app_model_verbose_name(self, app, model_name):
        verbose_name = apps.get_app_config(app).get_model(model_name)._meta.verbose_name  # 获取models的名称
        return verbose_name

    def model_fields(self, model):
        return [field.name for field in model._meta.get_fields()]


class DjangoSql(object):
    # 执行原生语句，查询所有分组的数据
    @staticmethod
    def cursorsql(sql_select):
        """
        sql_select = '''select number, group_concat(get_time),group_concat(`value`),group_concat(rain_value)
        from gw_waterlevelgauge where runway='%s' and get_time >= '%s' and get_time<= '%s' group by number;''' % (
        runway, date_start, date_end)
        :param sql_select:
        :return:
        """
        cursor = connection.cursor()
        cursor.execute(sql_select)
        lis = cursor.fetchall()
        return lis
