# -*- coding: utf-8 -*-
from odoo import api, fields, models


class x_crm(models.Model):
    _inherit = 'crm.lead'

    @api.depends('order_ids')
    @api.one
    def _compute_sale_amount_total(self):  # nombre de la funcion heredada
        # un print para que se muestre en la consola, Si se muestra entonces is esta compilando esta parte del codigo
        print '********GBM*****************'
        # llamamos a la función padre para que ejecute su código original
        super(x_crm, self)._compute_sale_amount_total()
        # agregamos nuestro código
        # asignamos para evitar error de asignacióny poder hacer estavariable dentro de nuestro código
        self.sale_number = self.sale_number
        if self.sale_number != 0 and (str(self.stage_id) == 'crm.stage(1,)'):
            self.write({'stage_id': 3})
        # else:
            #self.write({'stage_id': 3})
        # volvemos a asignar para corregir el error que sale al comentar la línea "return res"
        self.sale_number = self.sale_number
        # return res
