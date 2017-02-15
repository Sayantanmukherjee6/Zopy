#!/usr/bin/env python
# coding: utf8
from crm import CRM


crm = CRM(authToken=authToken, scope="ZohoCRM/crmapi")

crm_insert = crm.insertRecords(
    module="CustomModule3",
    xmlData=data,
    version=2,
    duplicateCheck=2
)
