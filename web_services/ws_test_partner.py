import functools
import xmlrpclib
HOST = '172.17.0.2'
PORT = 8069
DB = 'encuesta'
USER = 'pcs@soluciones4g.com'
PASS = 'seguridad2017'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print "Logged in as %s (uid:%d)" % (USER, uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

#------------Mapeo
mapeo = call('res.partner', 'fields_get', ['child_ids'], [])
print mapeo