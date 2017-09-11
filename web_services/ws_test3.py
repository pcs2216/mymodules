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
#----------Nombre de encuestas
encuesta_name = call('survey.survey', 'search_read', [], ['title'])
print "Encuestas %s" % encuesta_name

#------------Mapeo
mapeo = call('survey.page', 'fields_get', [], ['relation'])
print " \n paginas %s \n" % mapeo


#------------Crear pagina
encuesta_pagina = call('survey.page', 'unlink',[21,23])


#------------Paginas de la encuesta con ID=3
encuesta_pagina = call('survey.page', 'search_read', [
                       ('survey_id', '=', 1)], ['id', 'title'])

for session in encuesta_pagina:
    print "ID %d %s" % (session['id'], session['title'])


fields = call('res.partner', 'fields_get', ['country_id'], [])
print "\n fields ids %s" % fields
