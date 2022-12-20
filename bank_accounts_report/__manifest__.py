# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# Copyright 2020-2022 Valentin Vinagre <valentin.vinagre@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Bank Accounts Report",
    "summary": "Choose which bank accounts will be displayed on invoice and sale order reports",
    "version": "15.0.1.0.1",
    "category": "Account",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account",
        "account_payment_mode",
        "account_payment_sale",
        "account_banking_mandate",
        "sale"
    ],
    "data": [
        "views/account_payment_mode.xml",
        "reports/account_invoice.xml",
        "reports/sale_order.xml"
    ],
}
