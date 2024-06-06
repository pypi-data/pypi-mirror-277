# -*- coding: utf-8 -*-
"""
============================================================
MongoDB Database & Collection
============================================================
"""

import inspect
import pprint
pp = pprint.PrettyPrinter(indent=2)
import os


import idebug as dbg


# ============================================================ MongoClient.
from pymongo import (
    MongoClient,
    ASCENDING,
    DESCENDING,
)
from pymongo.errors import ConnectionFailure


try:
    client = MongoClient(host='localhost', port=27017,
                        document_class=dict, tz_aware=True, connect=True, maxPoolSize=None, minPoolSize=100,
                        connectTimeoutMS=60000, waitQueueMultiple=None, retryWrites=True)
    # The ismaster command is cheap and does not require auth.
    client.admin.command('ismaster')
except ConnectionFailure as cf:
    dbg.exception(__file__, cf)
    raise
else:
    db = client['krx']
    bkdb = client['krxBackup']




# ============================================================ API.
def n_returned(cursor):
    return cursor.explain()['executionStats']['nReturned']




#
