#!/use/bin/env python3
#coding=utf-8

import os
import requests
import json

loginurl='http://op.kdweibo.cn:8222/login'
logindata={'username':'admin','pwd':'123'}
s=requests.Session()
r=s.post(loginurl,data=logindata)
print(r.status_code)
print(r.json())

headers={
    'Content-Type':'application/json',
    'X-Token':'ac3217052063464d2b909471f915ac11'
}

for line in open("iplist.txt"):
    l=line.split(',')
    print(l)
    service=l[0]
    port=int(l[3])
    nodelist=l[7:]

    if '' in nodelist:
        nodelist.remove('')

    serviceurl='http://op.kdweibo.cn:8222/v2/service/node/upserts'
    node=[]
    for i in nodelist:
        d={"port":port,"ip":i}
        node.append(d)
    data={"service": service, "nodes": node}

    jsondata=json.dumps(data)
    jsondata
    print(jsondata)

    s.post(serviceurl,data=jsondata,headers=headers)


