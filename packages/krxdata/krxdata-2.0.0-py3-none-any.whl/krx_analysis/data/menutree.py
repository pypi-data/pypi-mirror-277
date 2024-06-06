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
def CREATE_MenuDirId():
    """menuIds 수집."""
    cate = '통계'
    url = "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201"
    try:
        r = requests.get(url)
    except Exception as e:
        dbg.exception(__file__, e)
    else:
        try:
            s = BeautifulSoup(r.text, 'html.parser')
        except Exception as e:
            dbg.exception(__file__, e)
        else:
            s = s.find(id='jsMdiMenu')
            s = s.find('ul', class_="lnb_tree_wrap")
            for li in s.find_all('li', attrs={'data-depth-menu-id':re.compile('.+')}):
                menuId = li['data-depth-menu-id']
                print(menuId)
                a = li.find('a', attrs={'href':"javascript:void(0);"})
                menuName = a.get_text().strip()
                print(menuName)
                db.MenuDirId.insert_one({'cate':cate, 'menuId':menuId, 'menuName':menuName})



import pandas as pd
def collect_oneMenuIdTree(menuId='MDC0202'):
    """
    menuId 하위에 소속된 MenuTree를 수집한다.
    """
    url = f"http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId={menuId}"
    try:
        r = requests.get(url)
    except Exception as e:
        dbg.exception(__file__, e)
    else:
        try:
            s = BeautifulSoup(r.text, 'html.parser')
        except Exception as e:
            dbg.exception(__file__, e)
        else:
            s = s.find('li', attrs={'data-depth-menu-id':menuId})
            children = s.find_all('li', class_="CI-MDI-MENU-NO-CHILD")
            data = []
            for child in children:
                svc_nm = child.get_text().strip()
                # dbg.SectionGubun(svc_nm)

                parents = child.find_parents("li")
                parents.reverse()
                d = {}
                for i, parent in enumerate(parents, start=1):
                    atag = parent.find('a', attrs={'href':"javascript:void(0);"})
                    menuName = None if atag is None else atag.get_text().strip()
                    d.update({f'Lv{i}':menuName})

                a = child.find('a')
                try:
                    svc_id = a.attrs['data-menu-id']
                except Exception as e:
                    svc_id = None
                d.update({'svc':a.get_text().strip(), 'svc_id':svc_id})

                data.append(d)

            # df = pd.DataFrame(data)
            # cols = sorted(df.columns)
            # return df.reindex(columns=cols)
            db.DataServiceMenuTree.insert_many(data)


def collect_cate1menutree():
    menuIds = db.MenuDirId.distinct('menuId')
    for menuId in menuIds:
        collect_oneMenuIdTree(menuId)


def update_PostData(svc_id, form):
    filter = {'svc_id':svc_id}
    update = {'$set':{'form':parse_reqdata(form)}}
    db.DataServiceMenuTree.update_one(filter, update)
