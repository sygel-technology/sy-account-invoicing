# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Invoice Paid Before",
    "summary": "Field set to True when an invoice is paid.",
    "version": "14.0.1.0.0",
    "category": "Invoicing",
    "website": "https://www.sygel.es",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account",
    ],
    "post_init_hook": "post_init_hook"
}
