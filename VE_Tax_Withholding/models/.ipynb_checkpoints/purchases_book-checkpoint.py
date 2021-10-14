# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchasesBook( models.Model):
    _name = 'tax.purchases_book'
    _description = 'Book of every purchase bill entry by period'
    
    name = fields.Char(string='Title', required=True)
    
    description = fields.Text(string='Description')
    
    date_from = fields.Date(string='Fecha desde')
    
    date_to = fields.Date(string='Fecha hasta', default=fields.Date.today)
    
    related_invoices = fields.One2many(string='Facturas', comodel_name='account.move', inverse_name='name')