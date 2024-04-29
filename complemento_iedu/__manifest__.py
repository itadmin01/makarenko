# -*- coding: utf-8 -*-
##############################################################################
#                 @author IT Admin
#
##############################################################################

{
    'name': 'Complemento IEDU',
    'version': '16.01',
    'description': ''' Complemento en XML
    ''',
    'category': 'Accounting',
    'author': 'IT Admin',
    'website': 'www.itadmin.com.mx',
    'depends': [
        'base', 'account', 'cdfi_invoice'
    ],
    'data': [
        'views/account_invoice_view.xml',
        'views/custom_invoice_report.xml',
    ],
    'application': False,
    'installable': True,
    'price': 0.00,
    'currency': 'USD',
    'license': 'OPL-1',	
}
