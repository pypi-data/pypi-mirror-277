# -*- coding: utf-8 -*-

import inspect
import pprint
pp = pprint.PrettyPrinter(indent=2)


import idebug as dbg


from krx.mongo import *


# ============================================================
import math
import pandas as pd


def title_format(title, width=100):
    spaceLen = int((width - len(title)) / 2)
    space = " " * spaceLen
    print()
    print('=' * width)
    print(f"{space}{title}{space}")
    print('=' * width)


def print_table_title(collName, width=100):
    lineLen = int((width - len(collName) - 2) / 2)
    line = '#' * lineLen
    print(f"\n{line} {collName} {line}")



def view_collection(collName, filter=None, projection=None, sort=(), limit=0, tz=False,
    detail=False, dfT=False, info=False, describe=False):
    loc = f"{__name__}.{inspect.stack()[0][3]}"
    dbg.PartGubun(f"collName: {collName}")


    cursor = db[collName].find(filter, projection, limit=limit)
    df = pd.DataFrame(list(cursor))

    if len(df) == 0:
        dbg.timeline(loc, f"len(df): {len(df)}")
    else:
        # ------------------------------------------------------------ 정렬.
        if len(sort) > 0:
            df = df.sort_values(sort[0], ascending=sort[1]).reset_index(drop=True)
        # ------------------------------------------------------------ 시간대.

        # ------------------------------------------------------------ 자세히.
        if detail:
            dbg.SectionGubun("LoopingData:")
            _len = len(df)
            for i, d in enumerate(df.to_dict('records'), start=1):
                print()
                dbg.loop(loc, i, _len, f"collName: {collName}")
                for k, v in d.items():
                    print(f"{k}: {v}")

        # ------------------------------------------------------------
        print_table_title(collName)
        if info: print(df.info())
        if describe: print(df.describe())
        if dfT: return df.T
        else: return df


def view_BackupCollection(collName, jupyter=False):
    cursor = bkdb[collName].find()
    df = pd.DataFrame(list(cursor))
    if jupyter:
        return df
    else:
        print(df)
        df.info()



#
