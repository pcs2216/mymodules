#!/usr/bin/env python
import csv
import functools
import xmlrpclib
HOST = '70.35.200.126'
#HOST = '172.17.0.2'
PORT = 8069
DB = 'CMT_1_0'
USER = 'gbarrientos@soluciones4g.com'
PASS = 'Happy2016*'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print "Logged in as %s (uid:%d)" % (USER, uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)
#*****************************************************************************************
#*****************************************************************************************
reader = csv.reader(open('CSuprema.csv', 'rb'))

#actualizar campos de contactos comparando por nombre
for row in reader:
    nome=row[0]
    nombre = call('res.partner', 'search', [('name', '=', nome)])
    
    if len(nombre)>0 :
        print nombre[0]
        partner_id = call('res.partner', 'write', [nombre[0]], {'x_cmt_prospeccion': 2})
        
    