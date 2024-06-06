# -*- coding: utf-8 -*-

import pprint
pp = pprint.PrettyPrinter(indent=2)
import json


import requests


import idebug as dbg


HOST = 'data.krx.co.kr'
URI = f"http://{HOST}"


# ============================================================ Headers.
def _headers():
    return {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7,es;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': get_cookie(),
        'DNT': '1',
        'Host': HOST,
        'Referer': f'{URI}/mdi',
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'X-Requested-With': 'XMLHttpRequest',
    }

def get_cookie():
    return '__utma=139639017.1350543225.1569547430.1569547430.1569547430.1; __utmc=139639017; __utmz=139639017.1569547430.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=139639017.1.10.1569547430; JSESSIONID=379F3578E253019FFEEB7EBEA3DF71D9.103tomcat1; WMONID=5x_O32k4ksC; __utma=70557324.1111960620.1569547469.1569547469.1569547469.1; __utmc=70557324; __utmz=70557324.1569547469.1.1.utmcsr=krx.co.kr|utmccn=(referral)|utmcmd=referral|utmcct=/main/main.jsp; __utmb=70557324.2.10.1569547469'


# ============================================================ Request.
def getJsonData(data, **kw):
    url = f"{URI}/comm/bldAttendant/getJsonData.cmd"
    try:
        r = requests.post(url, data=data, **kw)
    except Exception as e:
        dbg.exception(__file__, e)
    else:
        try:
            d = json.loads(r.text)
        except Exception as e:
            dbg.exception(__file__, e)
            return []
        else:
            return list(d.values())[0]



def getMenuInfo(qs, **kw):
    url = f"{URI}/comm/menu/menuLoader/getMenuInfo.cmd"
    try:
        r = requests.get(url, params=qs, **kw)
    except Exception as e:
        dbg.exception(__file__, e)
    else:
        return json.loads(r.text)




#
