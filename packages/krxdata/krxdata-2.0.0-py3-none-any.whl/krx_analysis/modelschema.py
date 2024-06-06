# -*- coding: utf-8 -*-
"""
============================================================
Model's Schema Manager.
============================================================
"""

import inspect
import pprint
pp = pprint.PrettyPrinter(indent=2)


import idebug as dbg


from krx.mongo import *


# ============================================================
import os
import re
import pandas as pd
from krx.viewer import *

def schemaNaming(modelName):
    return f"_Schema_{modelName}"


def modelNaming(schemaName):
    return re.sub('^_Schema_', string=schemaName, repl='')


def get_schemaData(modelName, filter=None):
    schemaName = schemaNaming(modelName)
    cursor = db[schemaName].find(filter, {'_id':0})
    return list(cursor)


def view_Schema(modelName, filter=None):
    dbg.PartGubun(locals())

    data = get_schemaData(modelName, filter)
    df = pd.DataFrame(data)

    print_table_title(schemaNaming(modelName))
    print(df.info())
    return df


def has_schema(modelName):
    names = db.list_collection_names(filter={'name':schemaNaming(modelName)})
    if len(names) == 0:
        return False
    else:
        return True


# ============================================================ CreateModelSchema.
import re
# from krx.word_dtype import *
def CREATE_OneModelSchema():
    modelName = 'Holiday'

    sample_data = {
        'dt': '2019-01-01 00:00:00',
        'dayEN': 'TUE',
        'date': '2019-01-01',
        'day': '화요일',
        'name': '신정'
    }
    cols_map = {
        'calnd_dd': 'dt',
        'holdy_nm': 'name'
    }
    id_cols = ['date', 'name']
    dt_cols = ['dt', 'date']


    data = []
    for k, v in _schema_sample_.items():
        print(k, type(v))
        m = re.search("'([a-z]+)'", str(type(v)))
        print(m)
        print(m.group(1))
        role = 'key' if k in id_cols else None
        if k == 'dt':
            dtype = 'dt'
            pat = '%Y-%m-%d %H:%M:%S'
        elif k == 'date':
            dtype = 'date'
            pat = '%Y-%m-%d'
        else:
            dtype = m.group(1)
            pat = None

        data.append({'colName':k, 'dtype':dtype, 'role':role})
    pp.pprint(data)
    return

    coll = db[schemaNaming(modelName)]
    coll.drop()
    coll.insert_many(data)


def list_dataModels_missingSchema():
    names = db.list_collection_names(filter={'name':{'$regex':'^[A-Z]', '$options':'i'}})
    for modelName in names:
        if has_schema(modelName):
            pass
        else:
            print(modelName)


def CREATE_ALL_StaticModelSchema():
    pat = "^_Schema_|^_Test_|^Realtime|^TR|^op[tw]\d+|^OP[TW]\d+"
    names = db.list_collection_names(filter={'name':{'$not':{'$regex':pat}}})
    for modelName in names:
        if has_schema(modelName):
            # rollback_Collection()
            pass
        else:
            print(modelName)
            cols = ['colName','dtype','pat','def','role']

            if modelName == 'SampleData':
                data = [
                    ('modelName','str',None,'모델명 or 컬렉션명','key'),
                    ('data','records',None,'Raw 샘플데이터',None),
                    ('dt','datetime',None,'수집일시',None)
                ]
                for d in data:
                    doc = {}
                    for c, v in zip(cols, d):
                        doc.update({c:v})
                    print(doc)
                    db[schemaNaming(modelName)].insert_one(doc)



def initialize():
    dbg.timeline(__file__, "Static 모델 생성 중...")


    dbg.timeline(__file__, "TR ModelSchema 생성 중...")


    dbg.timeline(__file__, "실시간 목록 ModelSchema 생성 중...")



# from krx.data_util import *
# def backup_ALL_ModelSchema():
#     backup_Collections({'name':{'$regex':'^_Schema_'}})



# ============================================================ API.
from datetime import datetime, date, time
import pandas as pd
from krx.parser import parse_value

class Schematizer:
    def __init__(self, modelName):
        self.modelName = modelName
        self.schemaName = schemaNaming(modelName)

    def show_schema(self, filter=None):
        view_Schema(self.modelName, filter)

    def get_schemaCols(self, filter=None):
        return db[self.schemaName].distinct('colName', filter)

    def get_data(self, filter=None, projection=None):
        return get_schemaData(self.modelName, filter)

    # ------------------------------------------------------------ 파서.
    def parse_value(self, colName, value):
        """
        컬럼 하나하나마다 DB-Access를 하기 때문에 속도가 느려질 수 있다.
        벌크로 파싱하려고 할 경우, parse_data() 를 사용하라.
        """
        cursor = db[self.schemaName].find({'colName':colName}).limit(1)
        if n_returned(cursor) == 1:
            d = list(cursor)[0]
            return parse_value(value, d['dtype'], d['pat'])
        else:
            return value

    def parse_data(self, data):
        df = pd.DataFrame(data)
        df = df.dropna(axis=0, how='all')
        df = df.dropna(axis=1, how='all')

        if len(df) > 0:
            dataCols = list(df.columns)
            for d in get_schemaData(self.modelName, {'colName':{'$in':dataCols}}):
                c = d['colName']
                if c in dataCols:
                    try:
                        df[c] = df[c].apply(lambda x: parse_value(x, d['dtype'], d['pat']))
                    except Exception as e:
                        dbg.exception(self, e, d)
                else:
                    pass

            return df.to_dict('records')
        else:
            dbg.exception(__file__, "len(data) is 0.")
            # pp.pprint(data)
            return []



#
