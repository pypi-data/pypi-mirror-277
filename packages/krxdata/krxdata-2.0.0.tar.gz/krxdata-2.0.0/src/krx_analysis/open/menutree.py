# -*- coding: utf-8 -*-
"""
============================================================
좌측 메뉴트리 정보 수집파싱.
============================================================
"""

import pprint
pp = pprint.PrettyPrinter(indent=2)
import json
import re


import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


import idebug as dbg


from krx.mongo import *
from krx.parser import parse_reqdata


# ============================================================ Request.
def CREATE_OpenSvcMenuDirURL():
    """Menu-URLs 수집."""
    url = "http://open.krx.co.kr/contents/OPN/01/01010101/OPN01010101.jsp"
    try:
        r = requests.get(url)
    except Exception as e:
        dbg.exception(__file__, e)
    else:
        s = BeautifulSoup(r.text, 'html.parser')
        clickables = s.find_all('li', class_=re.compile('^depth\d+'))

        for clickable in clickables:
            atag = clickable.find('a', attrs={'href':re.compile('^/contents.+')})
            if atag is None:
                pass
            else:
                if atag.find('span') is None:
                    svc_nm = atag.get_text().strip()
                    svc_url = atag.attrs['href']

                    parents = clickable.find_parents('li', class_=re.compile('^depth\d+'))
                    parents.reverse()
                    d = {}
                    for i, parent in enumerate(parents, start=1):
                        a = parent.find('a', attrs={'href':re.compile('^/contents.+')})
                        menuName = None if a is None else a.get_text().strip()
                        menuName = re.sub('펼침|접힘', repl='', string=menuName)
                        d.update({f'Lv{i}':menuName})

                    d.update({'svc_nm':svc_nm, 'svc_url':svc_url})
                    db.OpenSvcMenuDirURL.insert_one(d)
                else:
                    pass


def update_rqdata(svc_nm, **rqdata):
    filter = {'svc_nm':svc_nm}
    doc = {}
    for k, v in rqdata.items():
        doc.update({k: parse_reqdata(v)})
        break
    update = {'$set':doc}
    db.OpenSvcMenuDirURL.update_one(filter, update)
