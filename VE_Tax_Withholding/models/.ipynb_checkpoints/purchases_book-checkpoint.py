# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchasesBook( models.Model):
    _name = 'tax.purchases_book'
    _description = 'Book of every purchase bill entry by period'
    
    related_invoice = fields.Many2one(string='Facturas', comodel_name='account.move', required=True)