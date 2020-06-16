# Copyright 2020 Valentin Vinagre <valentin.vinagre@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Invoices Menu Item',
    'version': '12.0.1.0.0',
    'category': 'Account',
    'summary': 'Add two menu items with customer and supplier invoices.',
    'author': 'Sygel',
    'website': 'https://www.sygel.es',
    'license': 'AGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'views/account_invoice.xml'
    ],
    'installable': True,
}
