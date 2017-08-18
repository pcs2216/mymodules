# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """manage trainings""",

    'description': """
        primera practica de  odoo
    """,

    'author': "soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/vista_curso.xml',
        'views/vista_session.xml',
        'views/vista_partner.xml',
        'workflow/session_workflow.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        #'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo_curso.xml',
    ],
    'intallable': True,
    'auto_install': False,
}
