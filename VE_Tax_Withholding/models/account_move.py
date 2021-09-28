# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMove( models.Model):
    _inherit = 'account.move'


    related_tax_withholding = fields.One2many( string = 'Comprobante de Retencion',
                                                comodel_name = 'tax.withholding_voucher',
                                                inverse_name = 'related_invoice')