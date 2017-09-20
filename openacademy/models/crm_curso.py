# -*- coding: utf-8 -*-
from odoo import api, fields, models

class x_crm(models.Model):
    _inherit = 'crm.lead'
    print '***************************************************************************'
    @api.depends('order_ids')
    def _compute_sale_amount_total(self):
        print 'xxxxx****'
        """res=super(x_crm, self)._compute_sale_amount_total()
        print '*************************'
        return res"""
        #x_status_number = fields.Integer(string=u'Actual', compute="_compute_sale")
    print '***************************************************************************'

    x_status_number = fields.Integer(string="Number0")
    #x_order_ids = fields.One2many('sale.order', related = 'opportunity_id', string='Orders')

    #@api.depends('stage_id')
    # def _compute_sale_2(self):
    #    for record in self:
    #        record.x_status_number = record.stage_id
    """
    @api.onchange('sale_number')
    def _change_status_(self):
        if self.sale_number > 0:
            self.stage_id = self.sale_number
    """