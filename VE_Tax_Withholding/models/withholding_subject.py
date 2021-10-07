# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WithholdingSubject( models.Model):

    _name = 'tax.withholding_subject'

    _description = 'Subject of Withholding Voucher'

    subject = fields.Char( string = 'Concepto de la Retención',
                            required = True)

    code = fields.Integer( string = 'Código',
                            required = True)

    notes = fields.Text( string = 'Notas internas')

    active = fields.Boolean( string = 'Active', default = True)

