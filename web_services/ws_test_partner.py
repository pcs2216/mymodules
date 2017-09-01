import functools
import xmlrpclib
HOST = '74.208.88.154'
PORT = 8069
DB = 'Seguridad'
USER = 'pcs@soluciones4g.com'
PASS = 'pedro2017'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print "Logged in as %s (uid:%d)" % (USER, uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

#------------Mapeo
mapeo = call('res.partner', 'fields_get', [], ['string','type'])

for session in mapeo:
    print session

