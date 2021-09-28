# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TaxWithholdingVoucher( models.Model):

    _name = 'tax.withholding_voucher'
    _description = 'Tax Withholding Voucher Info'


    code = fields.Char( string = 'Identifier Code', required = True)

    notes = fields.Text( string = 'Internal Notes about Voucher')

    active = fields.Boolean( string = 'Active', default = True)

    tax_rate = fields.Float( string = 'Withholding Tax rate')

    related_invoice = fields.One2many( string = 'Referencia de la Factura',
                                        comodel_name = 'account.move',
                                        inverse_name = 'related_tax_withholding',
                                        required = True)

    