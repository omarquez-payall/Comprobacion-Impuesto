# -*- coding: utf-8 -*-

{
    'name': 'VE - Tax Withholding',
    
    'summary': """
        This is a module in which you can perform tax withholdings, generate the sales and purchase ledger required by Venezuelan law. 
    """,
    
    'description': """
        This is a module in which you can perform tax withholdings, generate the sales and purchase ledger required by Venezuelan law. 
    """,
    
    'author': 'Payall',
    
    'website': 'https://payall.com.ve/',
    
    'category': 'Accounting',
    
    'version': '1.0.0',
    
    'depends': ['account_accountant'],
    
    'data': [
        "views/tax_withholding_views.xml",
        "security/ir.model.access.csv",
        "security/tax_withholding_security.xml"
    ],
    
    'demo': [
    ],
}