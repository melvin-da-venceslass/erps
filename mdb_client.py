import pymongo 
from pymongo import MongoClient
from datetime import datetime
import re,time

mdb_client = MongoClient("mongodb+srv://mviis_admin:d5uNysSB0uiYT3pK@mviis.bbuf8.mongodb.net/myFirstDatabase?retryWrites=true")


mdb_dbms = mdb_client["mviis"]
mdb_incl = mdb_dbms["invoice_db"]
mdb_cscl = mdb_dbms["mviis_customer"]
mdb_cost = mdb_dbms["costings"]
mdb_pric = mdb_dbms["pricelist"]

def get_customers_name(keyname):
  name_list = []
  for x in mdb_cscl.find({},{ "_id": 0, keyname: 1}):
    name_list.append(x[keyname])
  return name_list

def reform_time(given):
  
  unixs  = time.mktime(datetime.strptime(given,"%d-%b-%Y").timetuple())
  return datetime.fromtimestamp(unixs).strftime("%Y-%m-%d") 
 
def reform_time_2(given):
  unixs  = time.mktime(datetime.strptime(given,"%d-%b-%Y").timetuple())
  return datetime.fromtimestamp(unixs).strftime("%d-%b-%Y") 

def get_documents(value):
  
  query = { "invoice_no": value }
  document = mdb_incl.find(query)[0]
  document["_id"] =None
  document["p_date"] =reform_time(document["p_date"])
  document["invoice_date"] =reform_time(document["invoice_date"])
  document["deliver_on"] =reform_time(document["deliver_on"])
  return document

def get_records(value):
  documents = mdb_incl.find({})
  records = []
  if value =="All":
    for document in documents:
      document["_id"] =None
      document["p_date"] =reform_time_2(document["p_date"])
      document["invoice_date"] =reform_time_2(document["invoice_date"])
      document["deliver_on"] =reform_time_2(document["deliver_on"])
      records.append(document)
   
  elif value =="Quotation":
    for document in documents:
      if "Q-"in str(document["invoice_no"]):
        document["_id"] =None
        document["p_date"] =reform_time_2(document["p_date"])
        document["invoice_date"] =reform_time_2(document["invoice_date"])
        document["deliver_on"] =reform_time_2(document["deliver_on"])
        records.append(document)

  elif value =="Invoice + DC":
    for document in documents:
      if "IN-" in str(document["invoice_no"]):
        document["_id"] =None
        document["p_date"] =reform_time_2(document["p_date"])
        document["invoice_date"] =reform_time_2(document["invoice_date"])
        document["deliver_on"] =reform_time_2(document["deliver_on"])
        records.append(document)
  elif value =="PRO FORMA":
    for document in documents:
      if "PI-" in str(document["invoice_no"]):
        document["_id"] =None
        document["p_date"] =reform_time_2(document["p_date"])
        document["invoice_date"] =reform_time_2(document["invoice_date"])
        document["deliver_on"] =reform_time_2(document["deliver_on"])
        records.append(document)

  return records


def get_customer_info(value):
  customer_objs = []
  query = { "name": value }
  getRes = mdb_cscl.find(query)
  for x in getRes:
    customer_objs.append(x)

  return customer_objs

def get_docment_nums(types):
  list_docs = []
  for x in mdb_incl.find({},{ "_id": 0, "invoice_no": 1}):
        if x["invoice_no"].startswith(types):
            list_docs.append(x["invoice_no"])
        else:
            pass
  return list_docs

def get_next_roll(rollType):
    rollType = rollType.upper()
    rollType = rollType + "-"
    month = (datetime.today().strftime("%b")).upper()
    year = datetime.today().strftime("%y")
    number = "-(\d+)-"

    query = { "invoice_no": { "$regex": rollType + month + number + year } }
    doc_count = mdb_incl.count_documents(query)
    
    if doc_count >0:
        documents = mdb_incl.find(query)
        num_list  = []
        for x in documents:
            match = re.findall(number, x['invoice_no'])
            num_list.append(int(match[0]))
        next_roll = max(num_list)+1
        new_roll  = rollType + month + "-" + str("{:02d}".format(next_roll)) + "-" + year
    else:
        new_roll = rollType + month + "-01-" + year
    return new_roll
  
def GetRowByName(columnName, value):
  dat_list = []
  query = { columnName: value }
  getRes = mdb_incl.find(query)
  for x in getRes:
    dat_list.append(x)
  return dat_list

def insert_new_document(dictDoc):
  dat_list = GetRowByName("invoice_no",dictDoc.get('invoice_no'))
  if dat_list:
    return False
  else:
    x = mdb_incl.insert_one(dictDoc)
    return True

def update_old_document(dictDoc):
  dat_list = GetRowByName("invoice_no",dictDoc.get('invoice_no'))
  if dat_list:
    query = { "invoice_no": dictDoc.get('invoice_no') }
    updatedValues = { "$set": dictDoc }
    mdb_incl.update_one(query, updatedValues)
    return True
  else:
    return False
  

def create_new_document(dictDoc):
  key = {"proj_name": dictDoc["proj_name"]}
  return mdb_cost.replace_one(key,dictDoc,True)


def get_proj_costing(key):
  try:
    d = mdb_cost.find({"proj_name": key})[0]
    del d["_id"]
    return d
  except:
    return False
  
def get_proj():
  try:
    l = []
    dd = mdb_cost.find({})
    for d in dd:
      l.append(d["proj_name"])
    return l


  except:
    return False
  
def get_products():
  l = []
  dd = mdb_pric.find({})
  for d in dd:
      l.append(d["desc"])
  return l


def get_product_price(key):
  d = mdb_pric.find_one({"desc":key})
  print(d)
  return d["price"]
