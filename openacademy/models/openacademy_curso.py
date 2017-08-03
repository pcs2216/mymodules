from odoo import models, fields


class Curso (models.Model):
    _name = 'openacademy.curso' #Model odoo name

    name = fields.Char(string='Title',required=True) #Field reserved to identified name re
    description = fields.Text(string='Description')

