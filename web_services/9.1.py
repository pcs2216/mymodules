#!/usr/bin/env python
import csv
import functools
import xmlrpclib
HOST = '172.17.0.2'
PORT = 8069
DB = 'odoo_curso'
USER = 'pcs@soluciones4g.com'
PASS = 'america666'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print "Logged in as %s (uid:%d)" % (USER, uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)
#*****************************************************************************************
#*****************************************************************************************
"""
reader = csv.reader(open('res.partner.csv', 'rb'))

campo=[]
partner_template={}
band=1
for row in reader:
        campo=row
        band=2
    else:
        cont=0  
        for col in campo:  
            partner_template.update({campo[cont]: row[cont]})
            cont=cont+1            
print partner_template
"""
#partner_id = call('res.partner', 'write',[25], partner_template)
#print partner_id
ids = call('crm.lead', 'search_read', [],['id','stage_id','sale_number'])
#print "\n partner ids %s" % ids
for x in ids:
    print x

