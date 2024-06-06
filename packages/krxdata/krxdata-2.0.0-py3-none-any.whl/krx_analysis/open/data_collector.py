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
from krx.open import req
from krx.parser import parse_reqdata


# ============================================================
def fetch_holidays(year=None):
    cursor = db.OpenSvcMenuDirURL.find({'svc_nm':'휴장일'})
    d = list(cursor)[0]
    form = d['form']

    form.update({
        'search_bas_yy': datetime.now().year if year is None else year,
        'code': req.get_OTP(d['qs']),
    })
    return req.post_data(form)


def fetch_IR(year=None, month=None, market=None):
    cursor = db.OpenSvcMenuDirURL.find({'svc_nm':'IR'})
    d = list(cursor)[0]
    form = d['form']

    year = datetime.now().year if year is None else year
    month = datetime.now().month if month is None else month
    form.update({
        'sch_yymm': f"{year}{str(month).zfill(2)}",
        'code': req.get_OTP(d['qs']),
    })
    if market is not None: form.update({'market':market})

    return req.post_data(form)


#
