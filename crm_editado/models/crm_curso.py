# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_crm(models.Model):
    _inherit = 'crm.lead'
    

    @api.depends('order_ids')
    def _compute_sale_amount_total(self):
        print '************************* before'
        res = super(x_crm, self)._compute_sale_amount_total()        
        if self.sale_number > 0:            
            self.stage_id = 3
        print "Stage %s" % self.stage_id
        return res

    #x_status_number = fields.Integer(string=u'Actual', compute="_compute_sale2")

    """

    
    @api.onchange('sale_number')
    def _change_status_(self):
        if self.sale_number > 0:
            self.stage_id = 4
            print "***************Stage %s" % self.stage_id
    """
