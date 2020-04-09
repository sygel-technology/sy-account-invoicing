# Copyright 2019 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Invoicing Inside Account Menu",
    "summary": "Put the Invoicing Menu inside the Accounting Menu",
    "version": "13.0.1.0.0",
    "category": "Accounting, Invoicing",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'account',
    ],
    'data': [
        'views/invoicing_in_accouting.xml',
    ],
}
