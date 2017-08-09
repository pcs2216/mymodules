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

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]