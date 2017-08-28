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

# 2. Read the sessions
model = 'openacademy.session'
method_name = 'search_read'
domain = []
sessions = call(model,method_name,domain, ['name','seats'])
for session in sessions:
    print "Session %s (%s seats)" % (session['name'], session['seats'])

# 3.create a new session
course_id = call('openacademy.curso', 'search', [('name','ilike','curso')])[0]
session_id = call('openacademy.session', 'create', {
    'name' : 'My session',
    'course_id' : course_id,
})