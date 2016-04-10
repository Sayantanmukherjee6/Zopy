Zopy: Zoho CRM Made Easy
--
Zopy is a library for make more easy the way you connect to Zoho CRM Api.

Zopy will provide some functions similar to Api REST queries. The library is in develop yet, feel free to send a pull request.

Installation:
--
Install using `pip`...

  pip install -e git+git@github.com:dhararon/Zopy.git

Example
--

First we have to declarate zopy

```python
from zopy.crm import CRM

authToken = ""
crm = CRM(authToken=authToken,scope="ZohoCRM/crmapi")
```

#Search some rows

```python
crm_search = crm.searchRecords(module="CustomModule3", criteria={"Correo Electronico":"dhararon@hotmail.com"})

print crm_search.result.CustomModule3.row.FL.custommodule3_id
```

####Note: All inputs in zoho will be convert to low string and space will be convert to underscore

#Insert a row

```python
crm_insert = crm.insertRecords(module="CustomModule3", xmlData=[data], version=2, duplicateCheck=1)

print crm_insert.result.recorddetail.FL.id
```

####Note: All params was sended to CRM, form example <font color="red">duplicateCheck=1</font> don't change an existing formulary, and <font color="red">duplicateCheck=2</font> update all data in an existing formulary.  For more information read https://www.zoho.com/crm/help/api/insertrecords.html