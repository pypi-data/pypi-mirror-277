# -*- coding: utf-8 -*-

import pprint
pp = pprint.PrettyPrinter(indent=2)
import inspect
from datetime import datetime, timezone, timedelta
import json


import requests
import pandas as pd


import idebug as dbg


from krx.mongo import *
from krx.data import req
from krx.parser import parse_reqdata


# ============================================================
def fetch(svc, Lv1=None, Lv2=None, Lv3=None, Lv4=None, **rqdata):
    filter = {'svc':{'$regex':svc}}
    if Lv1 is not None: filter.update({'Lv1':Lv1})
    if Lv2 is not None: filter.update({'Lv2':Lv2})
    if Lv3 is not None: filter.update({'Lv3':Lv3})
    if Lv4 is not None: filter.update({'Lv4':Lv4})
    cursor = db.DataServiceMenuTree.find(filter, {'svc_id':1, 'form':1})
    try:
        d = list(cursor)[0]
    except Exception as e:
        dbg.exception(__file__, e)
    else:
        _form = d['form'].copy()
        for k, v in rqdata.items():
            _form.update({k:v})

        pp.pprint(_form)
        return req.getJsonData(_form)




# ============================================================
def collect_IssueBaseInfo():
    data = fetch(svc='전종목 기본정보', Lv1='기본 통계', Lv3='주식', Lv4='종목정보')
    """컬럼명을 소문자로 더 간결하게 바꿀 필요가 있다."""
    db.IssueBaseInfo.drop()
    db.IssueBaseInfo.insert_many(data)


def collect_InvestorTrdAmt():
    data = fetch(svc='개별종목', Lv1='기본 통계', Lv3='주식', Lv4='거래실적')
    return data
    # db.InvestorTrdAmt.drop()
    db.InvestorTrdAmt.insert_many(data)

#
