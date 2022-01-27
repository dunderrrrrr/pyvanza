from terminaltables import SingleTable
import colorful as cf
import unicodedata
import json
import pprint

def FormatTable(data):
    header = ["Time", "Change"]
    data = [header] + data
    table = SingleTable(data)
    print (table.table)

def FormatTitle(title, type):
    if type == "title":
        table_instance = SingleTable([[cf.bold_white(title.text)]])
        print(table_instance.table)
    if type == "warning":
        table_instance = SingleTable([[cf.red(title)]], "Warning")
        print(table_instance.table)

def FormatJson(title, data):
    json_obj = {}
    json_obj['title'] = title
    json_obj['data'] = {}
    for k,v in data:
        k = unicodedata.normalize("NFKD",k)
        json_obj['data'][k] = v
    pprint.pprint(json_obj, indent=1, sort_dicts=False)
