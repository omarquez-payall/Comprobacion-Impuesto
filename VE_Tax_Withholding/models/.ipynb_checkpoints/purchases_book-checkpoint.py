# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchasesBook( models.Model):
    _name = 'tax.purchases_book'
    _description = 'Book of every purchase bill entry by period'
    
    name = fields.Char(string='Title', required=True)
    
    description = fields.Text(string='Description')