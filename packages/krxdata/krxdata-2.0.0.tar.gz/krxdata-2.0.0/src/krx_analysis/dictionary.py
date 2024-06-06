# -*- coding: utf-8 -*-
"""
============================================================
용어 사전.
============================================================
"""

import inspect
import pprint
pp = pprint.PrettyPrinter(indent=2)


import idebug as dbg


from krx.mongo import *


# ============================================================
def add_one(ko, en, **kw):
    d = {'ko':ko, 'en':en}
    for k, v in kw.items():
        d.update({k:v})
    db.Dictionary.insert_one(d)


def add_bulk():
    cols = ['ko', 'en']
    data = [
        ('통계', 'stat'),
        ('기본통계', 'basestat')
    ]
    df = pd.DataFrame(data=data, columns=cols)
    df = df.assign(cate = 'svc_tree')
    db.Dictionary.insert_many(df.to_dict('records'))



def translate_colnames(df, svc, _from='en', to='ko'):
    cursor = db.Dictionary.find({'svc':svc}, {'_id':0, _from:1, to:1})
    dic = {}
    for d in list(cursor):
        dic.update({d[_from]:d[to]})

    return df.rename(columns=dic)


#
