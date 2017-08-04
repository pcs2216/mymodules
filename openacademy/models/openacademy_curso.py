# -*- coding: utf-8 -*-
from odoo import models, fields


class Curso (models.Model):
    _name = 'openacademy.curso'  # Model odoo name

    # Field reserved to identified name re
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')

    responsible_id = fields.Many2one(
        'res.users', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")
