# -*- coding: utf-8 -*-

import pprint
pp = pprint.PrettyPrinter(indent=2)
import inspect
from datetime import datetime
import re


import idebug as dbg


import pandas as pd


# from krx import trddt



# ============================================================ Utility Parser.
def parse_reqdata(s):
    p = re.compile('([A-Za-z_0-9]+):(.+)')
    li = p.findall(string=s)

    d = {}
    for t in li:
        d.update({t[0].strip() : t[1].strip()})
    return d


def clean_strcol(v):
    if isinstance(v, str):
        if len(v) is 0:
            return None
        else:
            return v
    else:
        return None



# ============================================================ KRX JSON Data Parser.
def clean_dtcols(df, dt_cols):
    """
    어떠한 형태의 스트링 날짜일시를 datetime 타입으로 변환한다.
    로컬 시간대를 반드시 적용한다. 항상 한국 기준으로. 왜냐? KRX 는 한국에 있거든.
    """
    for c in dt_cols:
        try:
            df[c] = df[c].apply(trddt.parse)
        except Exception as e:
            # dbg.exception(e, f"{__name__}.{inspect.stack()[0][3]}")
            # print(e)
            pass
    return df

def clean_numcols(df, num_cols):
    """int, float 모두 다룬다."""
    for c in num_cols:
        try:
            df[c] = df[c].str.replace(pat='-', repl='0')
        except Exception as e:
            pass
        try:
            df[c] = df[c].apply(parse_numStr)
        except Exception as e:
            # dbg.exception(e, f"{__name__}.{inspect.stack()[0][3]}")
            pass
    return df

def clean_floatcols(df, float_cols):
    for c in float_cols:
        try:
            df[c] = df[c].apply(lambda x: float(x.replace(',', '')))
        except Exception as e:
            # dbg.exception(e, f"{__name__}.{inspect.stack()[0][3]}")
            pass
    return df

p_pct = re.compile('%$')
def clean_pctcols(df, pct_cols):
    """단위가 %인 수를 소수점으로 변환."""
    def _clean_(x):
        if isinstance(x, str):
            x = p_pct.sub(string=x, repl='')
            x = float(x.strip().replace(',', ''))
        return x / 100

    for c in pct_cols:
        try:
            df[c] = df[c].apply(_clean_)
        except Exception as e:
            # dbg.exception(e, f"{__name__}.{inspect.stack()[0][3]}")
            print(e)
    return df

def parse_rawdata(rawdata, **kw):
    """
    파싱을 하는 함수기 때문에 반환값에 대한 일관적인 규칙을 적용해야 한다.
    즉, rawdata가 None 이든 정상이든 반환값은 json-list 여야 한다.
    파싱 순서는 매우 중요하다.
    """
    # pp.pprint(kw)
    if rawdata is None:
        return rawdata
    else:
        if len(rawdata) is 0:
            return rawdata
        else:
            df = pd.DataFrame(rawdata)
            if 'cols_map' in kw: df = df.rename(columns=kw['cols_map'])
            if 'dt_cols' in kw: df = clean_dtcols(df, kw['dt_cols'])
            if 'num_cols' in kw: df = clean_numcols(df, kw['num_cols'])
            if 'pct_cols' in kw: df = clean_pctcols(df, kw['pct_cols'])
            return df.to_dict('records')




# ============================================================ DataStructureParser.
def parseBySep(s):
    """
    좌(code) | Seperator | 우(name)
    """
    loc = f"{__name__}.{inspect.stack()[0][3]}"
    # print(loc)
    p_sep = re.compile('[:=]|//')
    p_edge1 = re.compile('^"|"$')
    p_edge2 = re.compile("^'|'$")
    d = {}
    for line in s.splitlines():
        line = line.strip()
        if len(line) > 0:
            # print(f"{'-'*50} | line-> {line}")
            elems = p_sep.split(line)
            if len(elems) == 2:
                k = elems[0].strip()
                v = elems[1].strip()
                k = p_edge1.sub(string=k, repl='')
                k = p_edge2.sub(string=k, repl='')
                v = p_edge1.sub(string=v, repl='')
                v = p_edge2.sub(string=v, repl='')
                # print(f"k: {k}")
                # print(f"v: {v}")
                d.update({k:v})
            else:
                raise
        else:
            pass
    return d


def parse_CodeNamePair(s):
    """KOA 함수 설명란에 파라미터당 옵션."""
    elems = re.findall('(\d+)[ \t\n\r\f\v]*([:=]|//)[ \t\n\r\f\v]*([가-힣A-Za-z\(\)\d+-]+)', s)
    # print(f"'\n\n'{elems}")
    data = []
    for e in elems:
        data.append({'code': e[0], 'name': e[2]})
    # pp.pprint(data)
    return data


# ============================================================ ValueParser.
from datetime import datetime, date, time, tzinfo, timezone, timedelta
def date_to_dt(v, pat):
    d = datetime.strptime(str(v).strip(), pat)
    dt = datetime.today().astimezone().replace(hour=0, minute=0, second=0, microsecond=0)
    return dt.replace(year=d.year, month=d.month, day=d.day)


def time_to_dt(v, pat):
    t = datetime.strptime(str(v).strip(), pat)
    dt = datetime.today().astimezone()
    return dt.replace(hour=t.hour, minute=t.minute, second=t.second, microsecond=0)


def parse_numStr(s, pct=False):
    if isinstance(s, str):
        s, n = re.subn('%$', '', s.strip())
        _pct = False if n == 0 else True

        s = s.replace(',', '')
        m = re.search('([\+-])*(\d+)(\.\d+)*', s)
        if m.group(3) == None:
            v = int(m.group(2))
        else:
            v = int(m.group(2)) + float(m.group(3))
        if m.group(1) != None:
            sign = int(f"{m.group(1)}1")
            v *= sign

        return v / 100 if _pct or pct else v
    elif isinstance(s, int):
        return s / 100 if pct else s
    elif isinstance(s, float):
        return s / 100 if pct else s
    else:
        return s


def parse_value(v, dtype, pat=None, ndigits=4):
    if v is None:
        return None
    else:
        try:
            if dtype == 'int':
                return parse_numStr(v)
            elif dtype == 'int_abs':
                return abs(parse_numStr(v))
            elif dtype == 'float':
                return round(parse_numStr(v), ndigits)
            elif dtype == 'pct':
                return round(parse_numStr(v, True), ndigits)
            elif dtype == 'date':
                return date_to_dt(v, pat)
            elif dtype == 'time':
                return time_to_dt(v, pat)
            elif dtype == 'dt':
                return datetime.strptime(str(v).strip(), pat)
            else:
                # dtype이 미리정의되어 있지 않다면, 문자열로 가정하고 그대로 반환한다.
                return v
        except Exception as e:
            # dbg.exception(__file__, "파싱 에러가 발생하면, 입력된 값을 그대로 반환한다.", locals())
            return v





#
