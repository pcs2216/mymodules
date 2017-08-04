# -*- coding: utf-8 -*-
from odoo import models, fields


class Session (models.Model):
    _name = 'openacademy.session' #Model odoo name

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")