#!/usr/bin/env python
import csv
import functools
import xmlrpclib
HOST = '172.17.0.2'
PORT = 8069
DB = 'encuesta'
#USER = 'pcs@soluciones4g.com'
#PASS = 'seguridad2017'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

USER = (raw_input('USUARIO: '))
PASS = (raw_input('PASWORD: '))
print "Logged in as %s " % (PASS)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print "Logged in as %s (uid:%d)" % (USER, uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)
ids = call('res.partner', 'search_read', [], ['name'])
print "\n partner ids %s" % ids
