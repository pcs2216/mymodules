# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_crm(models.Model):
    _inherit = 'crm.lead'

    #x_status_number = fields.Integer(string='Actual', compute='_compute_sale2')

    @api.depends('order_ids')
    def _compute_sale_amount_total(self):
        print '************************* before'
        print "Stage %s" % self.stage_id
        res = super(x_crm, self)._compute_sale_amount_total()
        self.sale_number = self.sale_number
        if self.sale_number == 0:
            self.write({'stage_id': 1})
        else:
            self.write({'stage_id': 4})
        print "Stage %s" % self.stage_id
        self.sale_number = self.sale_number 
        #return res

    #x_status_number = fields.Integer(string=u'Actual', compute=_compute_sale2)

    """

    
    @api.onchange('sale_number')
    def _change_status_(self):
        if self.sale_number > 0:
            self.stage_id = 4
            print "***************Stage %s" % self.stage_id
    """
