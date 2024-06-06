# -*- coding: utf-8 -*-


import inspect
import pprint
pp = pprint.PrettyPrinter(indent=2)


import idebug as dbg


from krx.mongo import *
from krx.modelschema import (
    Schematizer,
    has_schema,
)


# ============================================================ BaseModels.

class BaseModel(object):
    def __init__(self, modelName):
        self.modelName = modelName
        if has_schema(modelName):
            self.schema = Schematizer(modelName)

    def _attr(self, dic):
        for k, v in dic.items():
            setattr(self, k, v)
        return self

    def astimezone(self, df, c='dt'):
        df[c] = df[c].apply(lambda x: trddt.astimezone(x))
        return df


class DataModel(BaseModel):
    """
    Database & Schema 기반 모델.
    collName, Schematizer 을 반드시 보유한다.
    """
    def __init__(self, modelName, test=False):
        super().__init__(modelName)
        self.collName = f"_Test_{modelName}" if test else modelName

    def show_tbl(self, dfT=False, info=False, desc=False):
        cursor = db[self.collName].find(None, {'_id':0})
        df = pd.DataFrame(list(cursor))

        title = f"Collection: {self.modelName}"
        print_table_title(title)
        self._show_df(df, dfT, info, desc)

    def load(self, filter=None, projection=None, **kw):
        cursor = db[self.collName].find(filter, projection, **kw)
        self.data = list(cursor)
        return self

    def insert_data(self, data):
        try:
            db[self.collName].insert_many(data)
        except Exception as e:
            dbg.exception(self, e)

    def parse_data(self, data):
        self.data = self.schema.parse_data(data)
        return self

    def get_df(self):
        return pd.DataFrame(self.data)

    def attr(self, **filter):
        try:
            cursor = db[self.collName].find(filter).limit(1)
            self._attr(list(cursor)[0])
        except Exception as e:
            msg = f"요청조건({filter})으로 attributize할 수 없다."
            dbg.exception(self, e, msg)

        return self


class CidModel(DataModel):
    """
    CompanyID-Model.
    [cid, ... ,data] 기반으로 schema 가 결정되는 Models를 위한 모델베이스.
    """
    def __init__(self, modelName):
        super().__init__(modelName)

    def identify(self, **kw):
        self.Company = DataModel('Company').attr(**kw)
        try:
            self.cid = self.Company._id
        except Exception as e:
            dbg.exception(self, e, f"요청조건({kw})으로 identify 실패.")
        return self


class CidExModel(CidModel):
    """
    eXtended-CID-Model.
    modelName에 cid를 추가하여 collName을 만듦으로써, 컬렉션을 확장하는 모델.
    """
    def __init__(self, modelName, **kw):
        super().__init__(modelName)
        self.identify(**kw)
        self.collName = f"{self.modelName}__{self.cid}"


class DataSelector(DataModel):
    def __init__(self, modelName, viewCols=None):
        super().__init__(modelName)
        if viewCols is None and hasattr(self, 'schema'):
            self.viewCols = self.schema.get_schemaCols()

    def repr(self):
        dbg.timeline(self, self.modelName)
        for c in self.viewCols:
            try:
                print(f"{self.modelName} | {c} = {getattr(self, c)}")
            except Exception as e:
                dbg.exception(self, e, "Schema를 수정하라.")

    def select(self, **filter):
        return self.attr(**filter)
# ============================================================ DerivedModels.


#
