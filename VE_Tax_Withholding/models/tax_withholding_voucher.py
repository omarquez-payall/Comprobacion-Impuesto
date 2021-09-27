# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TaxWithholdingVoucher( models.Model):

    _name = 'tax.withholding_voucher'
    _description = 'Tax Withholding Voucher Info'


    code = fields.Char( string = 'Identifier Code', required = True)

    notes = fields.Text( string = 'Internal Notes about Voucher')

    active = fields.Boolean( string = 'Active', default = True)

    