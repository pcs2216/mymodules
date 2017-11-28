# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_sale(models.Model):
    _inherit = 'sale.order'

    
    x_status_number = fields.Integer(compute='_compute_sale_amount_total', string="Number of Quotations")
    
    
    @api.depends('sale_number')
    def _compute_sale(self):
        for record in self:
            record.x_status_number = record.sale_number
    """    
    @api.onchange('sale_number')
    def _change_status_(self):
        if self.sale_number > 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
    """        
            
        
