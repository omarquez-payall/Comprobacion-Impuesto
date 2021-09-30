# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TaxWithholdingVoucher( models.Model):

    _name = 'tax.withholding_voucher'
    _description = 'Tax Withholding Voucher Info'


    code = fields.Char( string = 'Identifier Code', required = True)

    notes = fields.Text( string = 'Internal Notes about Voucher')

    active = fields.Boolean( string = 'Active', default = True)

    tax_rate = fields.Char( string = 'Withholding Tax rate', readonly=True)

    withholding_amount = fields.Char( string = 'Withholding amount', readonly=True)

    related_invoice = fields.Many2one( string = 'Referencia de la Factura',
                                        comodel_name = 'account.move',
                                        required = True)

    customer = fields.Many2one(string='Cliente', related='related_invoice.partner_id')

    @api.onchange('related_invoice')
    def _onchange_related_invoice(self):
        if self.related_invoice.amount_by_group: 
            self.tax_rate = self.related_invoice.amount_by_group[1][1]*(100/self.related_invoice.amount_by_group[1][2])
            self.withholding_amount = self.related_invoice.amount_by_group[1][1] * (-1)




    