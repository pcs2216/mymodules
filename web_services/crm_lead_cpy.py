# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import date
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    sale_amount_total = fields.Monetary(compute='_compute_sale_amount_total', string="Sum of Orders", currency_field='c$
    sale_number=fields.Integer(
        compute='_compute_sale_amount_total', string="Number of Quotations")
    order_ids=fields.One2many('sale.order', 'opportunity_id', string='Orders')

    @api.depend('order_ids')
    def _compute_sale_amount_total(self):
        for lead in self:
            total=0.0
            nbr=0
            company_currency=lead.company_currency or self.env.user.company_id.currency_id
            for order in lead.order_ids:
                if order.state in ('draft', 'sent'):
                    nbr += 1
                if order.state not in ('draft', 'sent', 'cancel'):
                    total += order.currency_id.compute(
                        order.amount_untaxed, company_currency)
            lead.sale_amount_total=total
            lead.sale_number=nbr
    @api.model
    def retrieve_sales_dashboard(self):
        res=super(CrmLead, self).retrieve_sales_dashboard()
        date_today=date.today()

        res['invoiced']={
            'this_month': 0,
            'last_month': 0,
        }
        account_invoice_domain=[
            ('state', 'in', ['open', 'paid']),
            ('user_id', '=', self.env.uid),
            ('date', '>=', date_today.replace(day=1) - relativedelta(months=+1)),
            ('type', 'in', ['out_invoice', 'out_refund'])
        ]
        invoice_data=self.env['account.invoice'].search_read(account_invoice_domain, ['date', 'amount_untaxed_signed$

        for invoice in invoice_data:
            if invoice['date']:
                invoice_date=fields.Date.from_string(invoice['date'])
                if invoice_date <= date_today and invoice_date >= date_today.replace(day=1):
                    res['invoiced']['this_month'] += invoice['amount_untaxed_signed']
                elif invoice_date < date_today.replace(day=1) and invoice_date >= date_today.replace(day=1) - relative$
                    res['invoiced']['last_month'] += invoice['amount_untaxed_signed']

        res['invoiced']['target']=self.env.user.target_sales_invoiced
        return res




    < openerp >
    < data >
        < menuitem name="Otro Producto" id="prueba_main" sequence="90" / >
        < menuitem name="Producto distinto" id="prueba_main_main" parent="prueba_main" / >

        < record id="product_prueba_form_view" model="ir.ui.view" >
            <field name="name" > product.prueba < /field >
            < field name="model" > product.template < /field >
            < field name="mode" > primary < /field >
            < field name="priority" eval="8" / >
            < field name="inherit_id" ref="product.product_template_only_form_view" / >
            < field name="arch" type="xml" >
                < field name="name" position="after" >
                    < group >
                        < field name="campoprueba" / >
                    < /group >
                < / field >
           < / field >
        < / record >

        < record id="prueba_main_main_action" model="ir.actions.act_window" >
            < field name="name" > Main < /field >
            < field name="res_model" > product.template < /field >
            < field name="view_mode" > tree, form < /field >
        < / record >

        < menuitem action="prueba_main_main_action" id="prueba_main_main_menu" sequence="1" parent="prueba_main_main" / >
    < /data >
< / openerp >

< record model="ir.actions.act_window.view" id="prueba_main_main_action_form" >
            < field name="sequence" eval="2" / >
            < field name="view_mode" > form < /field >
            < field name="view_id" ref="product_prueba_form_view" / >
            < field name="act_window_id" ref="prueba_main_main_action" / >
        < /record >
