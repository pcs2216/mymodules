# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_crm(models.Model):
    _inherit = 'crm.lead'

    @api.depends('order_ids')
    @api.one
    def _compute_sale_amount_total(self): # nombre de la funcion heredada
        print '********GBM***************** before' # un print para que se muestre en la consola, Si se muestra entonces is esta compilando esta parte del codigo
        super(x_crm, self)._compute_sale_amount_total() # llamamos a la función padre para que ejecute su código original
        #agregamos nuestro código    
        self.sale_number = self.sale_number #asignamos para evitar error de asignacióny poder hacer estavariable dentro de nuestro código    
        if self.sale_number == 0:   
            self.write({'stage_id': 1}) 
        else:
            self.write({'stage_id': 3})
        self.sale_number = self.sale_number #volvemos a asignar para corregir el error que sale al comentar la línea "return res"
        # return res
