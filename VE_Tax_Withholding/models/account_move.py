# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMove( models.Model):
    _inherit = 'account.move'


    related_tax_withholding = fields.Many2One( string = 'Comprobante de Retencion',
                                                comodel_name = 'tax.withholding_voucher')