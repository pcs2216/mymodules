import functools
import xmlrpclib
HOST = '172.17.0.3'
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

"""
# 2. Read the sessions
model = 'openacademy.session'
method_name = 'search_read'
domain = []
sessions = call(model,method_name,domain, ['name','seats'])
for session in sessions:
    print "Session %s (%s seats)" % (session['name'], session['seats'])

# 3.create a new session
course_id = call('openacademy.curso', 'search', [('name','ilike','curso')])[0]
responsible_id = call('res.partner','search',[('name','=','Delta PC')])[0]
session_id = call('openacademy.session', 'create', {
    'name' : 'My session from ws',
    'instructor_id':responsible_id,
    'course_id' : course_id,
    'attendee_ids':[(4,46),(4,47)],
})"""
permisos = call('res.partner', 'check_access_rights',
                ['read'])
print " Permisos %s" % permisos

id = call('res.partner', 'search', [
          ('is_company', '=', True), ('customer', '=', True)])
print "\n partner ids %s" % id

ids = call('res.partner', 'search_read', [
           ('is_company', '=', True), ('customer', '=', True)], ['name'])
print "\n partner ids %s" % ids

fields = call('res.partner', 'fields_get', [
              'name', 'id', 'image'], ['string', 'help', 'type'])
print "\n fields ids %s" % fields

buscar_leer = call('res.partner', 'search_read', [(
    'is_company', '=', True), ('customer', '=', True)], ['name', 'country_id', 'comment'])
print "\n buscar leer %s" % buscar_leer

"""
crear = call('res.partner', 'create', {
    'name': 'Partner from WS',
})
print "\n ID creado %s" % crear

escribir = call('res.partner', 'write',[crear], {
    'name': 'xxx',
    'street': 'unknown',
})

obtener_nombre = call('res.partner', 'name_get',[crear])
print "\n Modificado %s" % obtener_nombre
"""

eli = call('res.partner', 'search', [('name', '=', 'xxx')])
print "B %s" % eli

#eliminar = call('res.partner', 'unlink',[51])

modelo = call('openacademy.curso', 'fields_get', [], ['string', 'help', 'type'])
print "\n campos de  %s" % modelo
"""
#crear nuevo modelo
new_model = call('ir.model','create',{
    'name' : "Custom Model",
    'model' :"x_custom_model",
    'state' :'manual',
})
"""

modelo2 = call('res.partner', 'fields_get', ['partner_latitude'], ['string', 'help', 'type'])
print "\n campos de  %s" % modelo2